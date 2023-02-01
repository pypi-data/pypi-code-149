import nbformat as nbf
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

    code = """\
from fabrictestbed_extensions.fablib.fablib import FablibManager as fablib_manager

try:
    fablib = fablib_manager()
                     
    fablib.show_config()
except Exception as e:
    print(f"Exception: {e}")"""

    nb["cells"] = [nbf.v4.new_markdown_cell(text[0]), nbf.v4.new_code_cell(code)]

    nbf.write(nb, path + '/test.ipynb')
