#!/usr/bin/env python
import os, sys, glob, yaml, subprocess
from yui import tsklib

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) != 1 :
        print("""
        pick single task to current day
        Usage:
            """+tsklib.cmd+""" pick %taskId%
            """+tsklib.cmd+""" pick id%taskId%
            """+tsklib.cmd+""" pick heap%taskNum%  - taskNum is order number from `"""+tsklib.cmd+""" list heap` command
        Example:
            """+tsklib.cmd+""" pick 3
            """+tsklib.cmd+""" pick id3
            """+tsklib.cmd+""" pick heap1
            """)
        exit(1);
        pass;
    id = argv[0]
    filename = tsklib.getTaskFilenameByIdOrNum(id, "heap")
    task = tsklib.loadYaml(filename)
    targetPath = tsklib.tskpath() + "/cur/" + task["status"]
    os.makedirs(targetPath, exist_ok=True)
    os.rename( filename, targetPath + "/" + task["filename"]);
    tsklib.gitAddCommitTask("pick "+id);
    pass

if __name__=="__main__":
    main()
    pass

