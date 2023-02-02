import nbformat as nbf, os
from datetime import date
from getpass import getuser


nb = nbf.v4.new_notebook()


def create_fab_notebook(name, path):
    text = [
        f"""\
<img src="./include/img/fabric_logo.png" width="500"/>

# {name}
```
Created: {date.today()}
Last Modified: 
{getuser()}
Clemson University
<username>@clemson.edu
```

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>"""
    ]

    code = [
        """\
from fabrictestbed_extensions.fablib.fablib import FablibManager as fablib_manager

try:
    fablib = fablib_manager()
                     
    fablib.show_config()
except Exception as e:
    print(f"Exception: {e}")""",
        """\
# Clean up log directory to avoid large files
import os
for item in os.scandir(os.path.join(os.getcwd(), 'logs')):
    if '.' != item.name[0]:
        os.remove(item.path)""",
    ]

    nb["cells"] = [
        nbf.v4.new_markdown_cell(text[0]),
        nbf.v4.new_code_cell(code[0]),
        nbf.v4.new_code_cell(code[1]),
    ]

    nbf.write(nb, path + f"/{name.lower()}.ipynb")


def update_fab_notebook(path):
    for item in os.scandir(path):
        if ".ipynb" in item.path and ".ipynb_checkpoints" not in item.path:
            itemPath = item.path
    code = """\
# Clean up log directory to avoid large files
import os
for item in os.scandir(os.path.join(os.getcwd(), 'logs')):
    if '.' != item.name[0]:
        os.remove(item.path)"""
    nb = nbf.read(itemPath, as_version=4)
    nb["cells"].insert(2, nbf.v4.new_code_cell(code))

    nbf.write(nb, itemPath)
