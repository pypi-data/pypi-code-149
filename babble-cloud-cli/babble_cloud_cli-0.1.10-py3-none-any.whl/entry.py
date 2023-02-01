import argparse
import pathlib
import subprocess
import shutil
import os

from simple_term_menu import TerminalMenu

path = f"{pathlib.Path(__file__).parent.absolute()}"

if not os.path.exists(f"{path}/projects"):
    os.mkdir(f"{path}/projects")
subprocess.run(f"docker build -t babble {path}", shell=True, capture_output=True)

def prompt(options, header, footer):
    terminal_menu = TerminalMenu(options,
        title = f"\n{header}\n",
        status_bar = f"\n{footer}\n",
        status_bar_style = ("fg_black",),
        menu_cursor_style = ("fg_black",),
        preview_command = f"cat {path}/projects/{{}}/config.yaml",
        preview_size = 1.0
    )
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        exit()
    else:
        return options[menu_entry_index]

parser = argparse.ArgumentParser()
action = parser.add_subparsers(dest = "action")

create = action.add_parser("create")
delete = action.add_parser("delete")
activate = action.add_parser("activate")
deactivate = action.add_parser("deactivate")
view = action.add_parser("view")
push = action.add_parser("push")
push.add_argument("file")
pull = action.add_parser("pull")
pull.add_argument("file")

projects = os.listdir(f"{path}/projects")

args = parser.parse_args()
volume = f"{path}/projects"

def main():
    if args.action == "create":
        os.system(f"docker run --rm -v {volume}:/projects -it babble create")
    elif args.action == "delete":
        os.system(f"docker run --rm -v {volume}:/projects -it babble delete")
    elif args.action == "activate":
        os.system(f"docker run --rm -v {volume}:/projects -it babble activate")
    elif args.action == "deactivate":
        os.system(f"docker run --rm -v {volume}:/projects -it babble deactivate")
    elif args.action == "view":
        os.system(f"docker run --rm -v {volume}:/projects -it babble view")
    elif args.action == "push":
        project = prompt(projects, "select a project", "ctrl-c to cancel")
        shutil.copy(args.file, f"{path}/projects/{project}/config.yaml")
    elif args.action == "pull":
        project = prompt(projects, "select a project", "ctrl-c to cancel")
        shutil.copy(f"{path}/projects/{project}/config.yaml", args.file)