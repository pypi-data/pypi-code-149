import re
import sys

from generalfile import Path
from generallibrary import deco_cache, Ver, Terminal, debug, EnvVar, remove, DecoContext, deco_require, VerInfo, Log, \
    join_with_str


class Venv(DecoContext):
    """ Standalone API, unlike the other APIs this one is not included in Packager. """
    PATH = EnvVar("PATH")
    VIRTUAL_ENV = EnvVar("VIRTUAL_ENV", default=None)
    ver_info = VerInfo()

    def __init__(self, path=None):
        self.path = Path(path)
        self.previous_venv = None

    @classmethod
    def get_active_venv(cls):
        active_venv_path = Path.get_active_venv_path()
        if active_venv_path is not None:
            return Venv(path=active_venv_path)

    def before(self, *args, **kwargs):
        self.activate()

    def after(self, *args, **kwargs):
        if self.previous_venv:
            self.previous_venv.activate()
        else:
            self.deactivate()

    def pyvenv_cfg_path(self):  return self.path / "pyvenv.cfg"
    def scripts_path(self):     return self.path / self.ver_info.venv_script_path
    def python_exe_path(self):  return self.scripts_path() / ("python.exe" if self.ver_info.windows else "python")
    def site_packages_path(self):  return self.path / "Lib/site-packages"
    def python_home_path(self): return Path(self.cfg()["home"])

    def exists(self):
        return self.path.is_venv()

    def active(self):
        return Path.get_active_venv_path() is self.path

    def create_venv(self, python_path=None, ver=None):
        assert self.path.empty()

        if python_path:
            python = python_path
        elif ver:
            python = self.list_python_versions()[ver]
        else:
            python = True

        return Terminal("-m", "venv", self.path, python=python).string_result

    PATH_delimiter = ver_info.env_var_path_delimiter

    @classmethod
    def _remove_path_from_PATH(cls, path_to_remove):
        paths = [Path(path=path_str) for path_str in cls.PATH.value.split(cls.PATH_delimiter)]
        paths.remove(path_to_remove)
        cls.PATH.value = join_with_str(delimiter=cls.PATH_delimiter, obj=paths)

    @classmethod
    def _add_path_to_PATH(cls, path_to_add):
        cls.PATH.value = f"{path_to_add}{cls.PATH_delimiter}{cls.PATH}"

    @classmethod
    def deactivate(cls):
        active_venv = Venv.get_active_venv()
        if active_venv:
            cls._remove_path_from_PATH(path_to_remove=active_venv.scripts_path())
            remove(sys.path, str(active_venv.scripts_path()))
            remove(sys.path, str(active_venv.site_packages_path()))
            cls.VIRTUAL_ENV.remove()
            return active_venv

    @deco_require(exists)
    def activate(self):
        self.previous_venv = self.deactivate()
        self._add_path_to_PATH(path_to_add=self.scripts_path())
        sys.path = [str(self.path), str(self.site_packages_path())] + sys.path
        self.VIRTUAL_ENV.value = self.path

        # Not sure these two do anything, doubt you can change interpreter during runtime
        # https://github.com/ManderaGeneral/generalpackager/issues/60
        sys.prefix = self.path
        sys.executable = self.python_exe_path()

    @deco_require(exists)
    def upgrade(self):
        return Terminal("-m", "ensurepip", "--upgrade", capture_output=False, python=self.python_exe_path()).string_result

    @deco_require(exists)
    @deco_cache()
    def cfg(self):
        r""" Example: https://github.com/ManderaGeneral/generalpackager/issues/57#issuecomment-1399402211 """
        return self.pyvenv_cfg_path().cfg.read()

    def python_version(self):
        return Ver(self.cfg().get("version") or self.cfg().get("version_info"))

    @staticmethod
    def list_venv_paths(path=None):
        """ Search parent folder of active venv path for venvs. """
        active_venv_path = Path.get_active_venv_path()
        if path is None and active_venv_path:
            path = active_venv_path.get_parent()
        else:
            path = Path(path)
        return path.get_children(filt=lambda p: p.is_venv())

    @classmethod
    def list_python_versions(cls):
        """ Examples here: https://github.com/ManderaGeneral/generalpackager/issues/58 """
        if cls.ver_info.windows:
            pythons = cls._list_python_versions_windows()
        else:
            pythons = cls._list_python_versions_linux()

        return {version: path for version, path in pythons.items() if path.is_file() and not path.get_parent_venv()}

    @staticmethod
    def _list_python_versions_windows():
        info_string = Terminal("py", "--list-paths").string_result
        versions = {}
        for line in info_string.splitlines():
            version, *_, path = line.split()  # Example: '-V:3.11 *        C:\Users\ricka\AppData\Local\Programs\Python\Python311\python.exe'
            version = version.split(":")[-1]  # Example: '-V:3.11'
            path = Path(path=path)
            versions[version] = path
        return versions

    @classmethod
    def _list_python_versions_linux(cls):
        versions = {}
        info_string = Terminal("whereis", "python").string_result
        for path_str in info_string.split()[1:]:
            path = Path(path=path_str)
            if not path.is_file():
                continue
            if not re.search("python(\d\.\d+)?$", path_str):
                continue
            terminal = Terminal(path, "--version", error=False)
            if terminal.fail:
                continue
            version = ".".join(terminal.string_result.split(" ")[1].split(".")[:2])  # Example: "Python 3.11.0"
            versions[version] = path
        return versions

    def __str__(self):
        return f"<Venv: {self.path}>"

    @staticmethod
    def debug():
        import os
        import sys

        debug(locals(),
              "os.environ['PATH']",
              "os.environ['VIRTUAL_ENV']",
              "sys.prefix",
              "sys.path",
              "sys.executable",
              )

