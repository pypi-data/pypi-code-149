# system modules
import logging
import os
import subprocess
import shutil
import shlex
import pathlib
import re
import json
import collections
import threading
import time

# internal modules
from thunar_plugins import l10n
from thunar_plugins.log import console, Notify
from thunar_plugins.version import __version__
from thunar_plugins.log import console, Notify

# external modules
from rich.pretty import Pretty
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import GObject, Gtk, Thunarx

logger = logging.getLogger(__name__)


METADATA_CACHE = collections.defaultdict(lambda: collections.defaultdict(set))


class GitAnnexSubmenu(GObject.GObject, Thunarx.MenuProvider):
    def __init__(self):
        logger.debug(f"GitAnnexSubmenu is initialized")

    @property
    def counter(self):
        try:
            return self._counter
        except AttributeError:
            self._counter = collections.Counter()
        return self._counter

    @classmethod
    def name(cls):
        s = _("Git Annex Context-Menu")
        if not shutil.which("git-annex"):
            s = _("[Unavailable]") + " " + s
        return s

    @classmethod
    def description(cls):
        s = _(
            "This plugin adds a context menu item "
            "for managing Git Annex repositories."
        )
        if not shutil.which("git-annex"):
            s += " " + _(
                "Install Git Annex to use this plugin: "
                "https://git-annex.branchable.com"
            )
        return s

    def make_metadata_cache(self, path, cache=None):
        """
        Make/Update a ``dict[file][field] = {'val3','val2'}``
        """
        notification = Notify.Notification.new(
            _("Git Annex Thunar Plugin"), None, "git-annex"
        )
        self.notification = notification
        if cache is None:
            cache = collections.defaultdict(
                lambda: collections.defaultdict(set)
            )
        notification.update(
            _("Git Annex Thunar Plugin"),
            "⏳ " + _("Determining amount of files..."),
            "git-annex",
        )
        notification.show()
        for n_files, f in enumerate(
            self.subprocess(
                subprocess.Popen,
                ["git", "-C", path, "ls-files"],
                stdout=subprocess.PIPE,
            ).stdout,
            start=1,
        ):
            pass
        try:
            git_annex = self.subprocess(
                subprocess.Popen,
                ["git", "-C", path, "annex", "metadata", "--json"],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
            )

            time_last_notification_update = 0
            time_begin = time.time()
            for i, line in enumerate(git_annex.stdout, start=1):
                if time.time() - time_last_notification_update > 1:
                    # couldn't get a stop button to work, callback was never
                    # called, don't know why 🤷
                    notification.update(
                        _("Git Annex Thunar Plugin"),
                        "⏳ "
                        + _(
                            "Reading metadata from Git Annex... ({n}/{n_files} files in {path})"
                        ).format(
                            n=i, n_files=n_files, path=pathlib.Path(path).name
                        )
                        + (
                            "\n\n{}".format(
                                _(
                                    "Sorry, you can't interrupt this "
                                    "and Thunar is frozen until it's finished."
                                )
                                + "🙂 "
                            )
                            if time.time() - time_begin > 5
                            else ""
                        ),
                        "git-annex",
                    )
                    notification.show()
                    time_last_notification_update = time.time()
                try:
                    m = json.loads(line)
                    cache.pop(m["file"], None)
                    for k, v in m["fields"].items():
                        for x in v:
                            if not k.endswith("lastchanged"):
                                # file-specific field
                                cache[m["file"]][k].add(x)
                                # overall list of fields
                                cache["/"][k].add(x)
                except Exception as e:
                    logger.error(
                        f"Something didn't work while reading metadata: "
                        f"{type(e).__name__}: {e}"
                    )
        except subprocess.CalledProcessError as e:
            logger.error(f"Couldn't get annex metadata from {path!r}: {e}")
            return cache
        finally:
            if git_annex.poll():
                logger.warning(f"Killing {git_annex}")
                git_annex.kill()
        notification.update(
            _("Git Annex Thunar Plugin"),
            "✅ "
            + _("Read metadata from {n} files in {path}").format(
                n=i, path=pathlib.Path(path).name
            )
            + "\n\n"
            + _("There are {n_fields} unique metadata fields.").format(
                n_fields=len(cache["/"])
            ),
            "git-annex",
        )
        notification.show()
        if logger.getEffectiveLevel() <= logging.DEBUG:
            console.print(f"cache: ")
            console.print(Pretty(dict(cache), max_length=20))
        return cache

    def rebuild_metadata_cache(self, path):
        uuid = self.get_git_annex_uuid(path)
        if not uuid:
            return METADATA_CACHE[uuid]
        METADATA_CACHE[uuid] = self.make_metadata_cache(path=path)

    @classmethod
    def subprocess(cls, fun, cmd, *args, **kwargs):
        logger.info(f"🚀 Running {cmd}")
        return fun(
            cmd, *args, **{**dict(encoding="utf-8", errors="ignore"), **kwargs}
        )

    @classmethod
    def run_cmd(
        cls,
        cmdparts,
        cwd=None,
        terminal=True,
        keep_open_on_success=False,
        keep_open_on_failure=True,
        dry_run=False,
    ):
        if not shutil.which("xfce4-terminal"):
            logger.warning(
                f"xfce4-terminal not found. Currently, "
                f"this is the only terminal our git-annex integration supports. "
                f"Continuing without showing commands in terminal."
            )
            terminal = False
        if terminal:

            def close_cmd(text, timeout=None):
                return ";".join(
                    map(
                        shlex.join,
                        [["echo"], ["echo", text]]
                        + (
                            [
                                ["echo", "This window will auto-close soon."],
                                ["sleep", str(int(timeout))],
                                ["exit"],
                            ]
                            if isinstance(timeout, int)
                            else [
                                ["echo", "You can close this window now."],
                                ["sleep", "infinity"],
                            ]
                        ),
                    )
                )

            cmdparts = [
                "sh",
                "-c",
                f"(set -x;{shlex.join(cmdparts)}) "
                f"&& ({close_cmd('✅ Success!',timeout=None if keep_open_on_success else 10)}) "
                f"|| ({close_cmd('💥 Failure!',timeout=None if keep_open_on_failure else 10)})",
            ]
            logger.debug(f"What the terminal will be given: {cmdparts = }")
            if logger.getEffectiveLevel() <= logging.DEBUG:
                console.print(f"📋 Copy-pastable:\n\n{shlex.join(cmdparts)}\n")
            cmdparts = [
                "xfce4-terminal",  # TODO: Hard-coded terminal emulator is bad
                "--icon",
                "git-annex",
                "--hide-menubar",
                "--hide-toolbar",
                "--command",
                shlex.join(cmdparts),
            ]
        logger.info(f"🚀 Running {cmdparts = }")
        if logger.getEffectiveLevel() <= logging.DEBUG:
            console.print(f"📋 Copy-pastable:\n\n{shlex.join(cmdparts)}\n")
        if dry_run:
            return cmdparts
        else:
            return cls.subprocess(subprocess.run, cmdparts, cwd=cwd)

    @classmethod
    def run_git_annex(
        cls,
        subcmd,
        paths=None,
        add_before=False,
        commit_before=False,
        reset_before=True,
        args=None,
        cwd=None,
        **kwargs,
    ):
        args = args or []
        paths = paths or []
        cmdparts = ["git", "annex", subcmd] + args + paths
        logger.debug(f"Bare {cmdparts = }")
        if logger.getEffectiveLevel() <= logging.DEBUG:
            console.print(f"📋 Copy-pastable:\n\n{shlex.join(cmdparts)}\n")
        if reset_before:
            cmdparts = [
                "sh",
                "-xc",
                ";".join(
                    shlex.join(p) for p in (["git", "reset"] + paths, cmdparts)
                ),
            ]
            logger.debug(f"With git resetting: {cmdparts = }")
            if logger.getEffectiveLevel() <= logging.DEBUG:
                console.print(f"📋 Copy-pastable:\n\n{shlex.join(cmdparts)}\n")
        repo_description = cls.get_git_annex_description(cwd or ".")
        if commit_before:
            cmdparts = [
                "sh",
                "-xc",
                ";".join(
                    shlex.join(p)
                    for p in (
                        [
                            "git",
                            "commit",
                            "-m",
                            f"thunar-plugins v{__version__}"
                            + (
                                " in {}".format(repo_description)
                                if repo_description
                                else ""
                            ),
                        ],
                        cmdparts,
                    )
                ),
            ]
            logger.debug(f"With git add: {cmdparts = }")
            if logger.getEffectiveLevel() <= logging.DEBUG:
                console.print(f"📋 Copy-pastable:\n\n{shlex.join(cmdparts)}\n")
        if add_before:
            cmdparts = [
                "sh",
                "-xc",
                ";".join(
                    shlex.join(p)
                    for p in (
                        ["git", "add"]
                        + (["-A"] if add_before == "all" else paths),
                        cmdparts,
                    )
                ),
            ]
            logger.debug(f"With git add: {cmdparts = }")
            if logger.getEffectiveLevel() <= logging.DEBUG:
                console.print(f"📋 Copy-pastable:\n\n{shlex.join(cmdparts)}\n")
        return cls.run_cmd(cmdparts=cmdparts, cwd=cwd, **kwargs)

    @classmethod
    def get_git_annex_uuid(cls, folder):
        try:
            return cls.subprocess(
                subprocess.check_output,
                ["git", "-C", folder, "config", "annex.uuid"],
            ).strip()
        except subprocess.CalledProcessError as e:
            logger.info(f"{folder!r} is apparently no git repository: {e}")

    @classmethod
    def get_git_annex_description(cls, folder):
        try:
            infojson = json.loads(
                cls.subprocess(
                    subprocess.check_output,
                    [
                        "git",
                        "-C",
                        str(folder),
                        "annex",
                        "info",
                        "here",
                        "--json",
                    ],
                )
            )
        except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
            logger.info(
                f"Couldn't determine git annex repo description for {folder!r}: {type(e).__name__} {e}"
            )
            return None
        return (
            re.sub(r"\s*\[here\]\s*$", "", infojson.get("description", ""))
            or None
        )

    @classmethod
    def get_git_branch(cls, folder="."):
        return cls.subprocess(
            subprocess.check_output,
            [
                "git",
                "-C",
                str(folder),
                "rev-parse",
                "--abbrev-ref",
                "HEAD",
            ],
        ).rstrip("\r\n")

    @classmethod
    def get_git_branches(cls, folder=".", all=False, sensible=True):
        git_branch_output = (
            cls.subprocess(
                subprocess.check_output,
                [
                    "git",
                    "-C",
                    str(folder),
                    "branch",
                ]
                + (["-a"] if all else []),
            )
            .rstrip("\r\n")
            .splitlines()
        )
        branches = [re.sub(r"^\W+", r"", L) for L in git_branch_output]
        if sensible:
            branches = [
                b
                for b in branches
                if not (
                    re.search(r"(^|/)views/", b)
                    or re.search(r"(^|/)synced/", b)
                    or re.search(r"(^|/)git-annex$", b)
                )
            ]
        return branches

    @classmethod
    def get_git_repo(cls, folder):
        return cls.subprocess(
            subprocess.check_output,
            [
                "git",
                "-C",
                str(folder),
                "rev-parse",
                "--show-toplevel",
            ],
        ).rstrip("\r\n")

    def get_file_menu_items(self, window, items):
        folders = set(
            (
                f.get_location().get_path()
                if f.is_directory()
                else os.path.dirname(f.get_location().get_path())
            )
            for f in items
        )
        folder_uuids = {d: self.get_git_annex_uuid(d) for d in folders}
        uuids = set(folder_uuids.values())
        if not (len(uuids) == 1 and all(uuids)):
            logger.info(
                f"Not exactly ONE unique git-annex repo selected: "
                f"{folder_uuids = }"
            )
            return []
        uuid = next(iter(uuids), None)
        cwd = next(iter(folder_uuids))
        logger.debug(f"Will operate in {cwd = }")
        repo = self.get_git_repo(cwd)
        branch = self.get_git_branch(repo)
        branches = self.get_git_branches(folder=repo, all=False, sensible=True)
        in_view = re.search(r"^views/.+", branch, flags=re.IGNORECASE)
        logger.debug(f"{repo = }, {branch = }, {branches = }, {in_view = }")

        # Note: Using a relative path to the repo is necessary as git-annex/git
        # doesn't see paths behind symlinks in the repo as tracked. So we need
        # to give it the actual absolute path in the repo
        # (see https://git-annex.branchable.com/bugs/Paths_behind_relative_symlinks_in_repo_don__39__t_work/)
        def path_for_git(path, repo=repo):
            repo = pathlib.Path(repo)
            objects_dir = (repo / ".git" / "annex" / "objects").resolve()
            p = pathlib.Path(path)
            # find the last link in the chain pointing to the actual annex
            while p.is_symlink():
                logger.debug(
                    f"{str(p)!r} is a symlink to {str(p.readlink())!r}"
                )
                if objects_dir in p.resolve().parents:
                    logger.debug(
                        f"{str(p)!r} is a git annex symlink "
                        f"pointing within {str(objects_dir)!r}"
                    )
                    # something dir in the path can still be a link, so we resolve the parent
                    return str(p.parent.resolve() / p.name)
                logger.debug(
                    f"following {str(p)!r} symlink to {str(p.readlink())!r}"
                )
                p = p.readlink()
            logger.debug(
                f"{str(p)!r} is no symlink, resolved path for git is {str(p.resolve())!r}"
            )
            return str(p.resolve())

        paths = [str(path_for_git(f.get_location().get_path())) for f in items]

        notify_flags = ["--notify-start", "--notify-finish"]
        if any(i.is_directory() for i in items) or len(items) > 10:
            logger.debug(
                f"Directory or too many files selected, "
                f"won't show desktop notifications"
            )
            notify_flags = []

        def on_click(menuitem, func=self.run_git_annex, **kwargs):
            kwargs = {**dict(cwd=cwd), **kwargs}
            menuitem.connect(
                "activate",
                lambda item, *a, **kw: func(**kwargs),
            )

        # top-level Git Annex context menu entry
        git_annex_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnex",
            label=_("Git Annex")
            + (" {}".format(_("(in view)")) if in_view else ""),
            tooltip=_("Git Annex File Synchronization"),
            icon="git-annex",
        )

        git_annex_sync_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexSync",
            label=_("Sync"),
            tooltip=_("Synchronize Git Annex state with other repos")
            + " (git annex sync{})".format(
                " {}".format("--only-annex") if in_view else ""
            ),
            icon="emblem-synchronizing",
        )
        on_click(
            git_annex_sync_menuitem,
            subcmd="sync",
            reset_before=False,
            add_before="all" if in_view else False,
            commit_before=in_view,
            args=["--only-annex"] if in_view else [],
        )

        git_switch_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitSwitch",
            label=_("Switch to Branch"),
            tooltip=_("Switch to different git branch"),
            icon="emblem-shared",
        )
        git_switch_submenu = Thunarx.Menu()
        git_switch_menuitem.set_menu(git_switch_submenu)
        for b in branches:
            if b == branch:
                continue
            menuitem = Thunarx.MenuItem(
                name="ContextMenu::GitSwitch",
                label=b,
                tooltip=_("Switch to git branch {!r}").format(b),
            )
            on_click(
                menuitem,
                func=self.run_cmd,
                cmdparts=["git", "switch", b],
                terminal=False,
            )
            git_switch_submenu.append_item(menuitem)

        git_annex_add_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexAdd",
            label=_("Add"),
            tooltip=_("Add untracked files to Git Annex") + " (git annex add)",
            icon="list-add",
        )
        on_click(
            git_annex_add_menuitem,
            subcmd="add",
            paths=paths,
            reset_before=False,
            args=notify_flags,
        )

        git_annex_get_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexGet",
            label=_("Get"),
            tooltip=_("Retreve files with Git Annex") + " (git annex get)",
            icon="edit-download",
        )
        on_click(
            git_annex_get_menuitem,
            subcmd="get",
            paths=paths,
            reset_before=True,
            args=notify_flags,
        )

        git_annex_drop_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexDrop",
            label=_("Drop"),
            tooltip=_("Drop files safely with Git Annex")
            + " (git annex drop)",
            icon="edit-delete",
        )
        on_click(
            git_annex_drop_menuitem,
            subcmd="drop",
            paths=paths,
            reset_before=True,
            args=notify_flags,
        )

        git_annex_lock_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexLock",
            label=_("Lock"),
            tooltip=_(
                "Lock files with Git Annex. "
                "This saves disk space and is faster but makes them read-only."
            )
            + " (git annex lock)",
            icon="object-locked",
        )
        on_click(
            git_annex_lock_menuitem,
            subcmd="lock",
            paths=paths,
            reset_before=True,
        )

        git_annex_unlock_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexUnlock",
            label=_("Unlock"),
            tooltip=_(
                "Unlock files with Git Annex to make them editable. "
                "Increases disk usage and is slower."
            )
            + " (git annex unlock)",
            icon="object-unlocked",
        )
        on_click(
            git_annex_unlock_menuitem,
            subcmd="unlock",
            paths=paths,
            reset_before=True,
        )

        # Metadata submenu
        git_annex_metadata_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexMetadata",
            label=_("Metadata"),
            tooltip=_("Manipulate Git Annex Metadata"),
            icon="dialog-information",
        )
        git_annex_metadata_submenu = Thunarx.Menu()
        git_annex_metadata_menuitem.set_menu(git_annex_metadata_submenu)

        # cache rebuilding
        git_annex_metadata_rebuild_cache_menuitem = Thunarx.MenuItem(
            name="ContextMenu::GitAnnexMetadata::CacheRebuild",
            label=_("Rebuild Cache"),
            tooltip=_("Rebuild cache of Git Annex metadata"),
            icon="database-index",
        )
        git_annex_metadata_submenu.append_item(
            git_annex_metadata_rebuild_cache_menuitem
        )
        git_annex_metadata_rebuild_cache_menuitem.connect(
            "activate",
            lambda item, *a, **kw: self.rebuild_metadata_cache(path=cwd, **kw),
        )

        if len(METADATA_CACHE[uuid]["/"]) > 0 and not in_view:
            git_annex_metadata_view_menuitem = Thunarx.MenuItem(
                name="ContextMenu::GitAnnexMetadata::View",
                label=_("View"),
                tooltip=_("Switch to a metadata-driven view"),
                icon="view-hidden",
            )
            git_annex_metadata_submenu.append_item(
                git_annex_metadata_view_menuitem
            )
            git_annex_metadata_view_submenu = Thunarx.Menu()
            git_annex_metadata_view_menuitem.set_menu(
                git_annex_metadata_view_submenu
            )
            for i, field in enumerate(METADATA_CACHE[uuid]["/"], start=1):
                logger.debug(f"{i = }, {field = }")
                menuitem = Thunarx.MenuItem(
                    name=f"ContextMenu::GitAnnexMetadata::View::{i}",
                    label=field,
                    tooltip=_(
                        "Switch to a metadata-driven view over field {field!r}"
                    ).format(field=field),
                    icon="view-hidden",
                )
                git_annex_metadata_view_submenu.append_item(menuitem)
                on_click(menuitem, subcmd="view", args=[f"{field}=*"])

        logger.debug(f"Assembling menus...")
        git_annex_submenu = Thunarx.Menu()
        git_annex_submenu.append_item(git_annex_sync_menuitem)
        if git_switch_submenu.get_items():
            git_annex_submenu.append_item(git_switch_menuitem)
        git_annex_submenu.append_item(git_annex_add_menuitem)
        git_annex_submenu.append_item(git_annex_get_menuitem)
        git_annex_submenu.append_item(git_annex_drop_menuitem)
        git_annex_submenu.append_item(git_annex_lock_menuitem)
        git_annex_submenu.append_item(git_annex_unlock_menuitem)
        git_annex_submenu.append_item(git_annex_metadata_menuitem)
        git_annex_menuitem.set_menu(git_annex_submenu)

        return (git_annex_menuitem,)

    def get_folder_menu_items(self, window, folder):
        return self.get_file_menu_items(window, [folder])
