import os
import util

projects = sorted(os.listdir("/projects"))
project = util.prompt(projects, "select project to view", "ctrl-c to cancel")
print()
if not os.path.exists(f"/projects/{project}/config.yaml"):
    exit()
os.system(f"cat /projects/{project}/config.yaml")
print("\n")