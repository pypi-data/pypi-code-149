# cli.py
import click, os, sys, shutil

dirname = os.path.dirname(__file__)
sys.path.append(dirname)
import modules.ipyCreate as ipyCreate

cwd = os.getcwd()


@click.command()
# @click.argument("command")
@click.option("--add", "-a", is_flag=True, help="Creates a new project")
@click.option(
    "--update", "-u", is_flag=True, help="Update current project (must be in directory)"
)
@click.option(
    "--name",
    "-n",
    default="myProj",
    show_default=True,
    help="Name of your fabric project",
)
@click.option(
    "--local", "-l", is_flag=True, help="Whether project will need local scripts or not"
)
def create_project(add, update, name, local):
    """
    This tool will help you create new fabric project templates, including
    directory structure.
    """
    if add:
        confirmation = input(
            f"Do you want to add a new project in the current directory? (yes/no) "
        )
        if confirmation == "yes":
            rootdir = os.path.join(cwd, name)
            os.makedirs(rootdir)
            os.makedirs(os.path.join(rootdir, "upload"))
            os.makedirs(os.path.join(rootdir, "download"))
            os.makedirs(os.path.join(rootdir, "include/img"))
            os.makedirs(os.path.join(rootdir, "logs"))
            if local:
                os.makedirs(os.path.join(rootdir, "local"))

            shutil.copy(
                os.path.join(dirname, "modules/img/fabric_logo.png"),
                os.path.join(rootdir, "include/img/fabric_logo.png"),
            )
            ipyCreate.create_fab_notebook(name, rootdir)

    # USE SPARINGLY
    elif update:
        rootdir = os.getcwd()
        ipyCreate.update_fab_notebook(rootdir)


if __name__ == "__main__":
    create_project()
