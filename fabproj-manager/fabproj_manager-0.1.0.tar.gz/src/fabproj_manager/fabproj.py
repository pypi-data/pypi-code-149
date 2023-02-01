# cli.py
import click, os, sys, shutil
dirname = os.path.dirname(__file__)
sys.path.append(dirname)
import modules.ipyCreate as ipyCreate

cwd = os.getcwd()


@click.command()
@click.argument("command")
@click.option("--name", "-n")


def create_project(command, name):
    if command == "add":
        confirmation = input(
            f"Do you want to add a new project titled {name} in the current working directory? (yes/no) "
        )
        if confirmation == "yes":
            rootdir = os.path.join(cwd, name)
            os.makedirs(rootdir)
            os.makedirs(os.path.join(rootdir, "upload"))
            os.makedirs(os.path.join(rootdir, "download"))
            os.makedirs(os.path.join(rootdir, "include/img"))
            shutil.copy(os.path.join(dirname,'modules/img/fabric_logo.png'), os.path.join(rootdir, 'include/img/fabric_logo.png'))
            ipyCreate.create_fab_notebook(name, rootdir)


if __name__ == "__main__":
    create_project()
