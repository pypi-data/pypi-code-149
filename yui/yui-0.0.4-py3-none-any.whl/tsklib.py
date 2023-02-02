#!/usr/bin/env python
import os, glob, yaml
from appdata import AppDataPaths

Title="Yui"
cmd="yui"

def tskpath():
    default=cmd
    home = os.getenv("YUI_HOME", default)
    path = AppDataPaths(home).app_data_path
    os.makedirs(path, exist_ok=True)
    return path
    pass

def getTaskFilenameById(id, location="*"):
    files = findTaskFiles( location, "*."+id+".md")
    if len(files) == 0:
        suffix = ""
        if location !="*":
            suffix = " in "+location
        print("task with id="+id+" not found"+suffix)
        exit(1)
    pass;
    if len(files) != 1:
        print("more than one task with id="+id+" found. That should never happen")
        exit(1)
    pass;
    return files[0]
    pass

def getTaskFilenameByIdOrNum( idOrNum, location="*"):
    if idOrNum.isnumeric():
        return getTaskFilenameById( idOrNum, location )
        pass
    if idOrNum[:2] == "id":
        return getTaskFilenameById( idOrNum[2:], location )
        pass
    if idOrNum[:3] == "cur":
        return getTaskFilenameByNum( idOrNum[3:], "cur")
        pass
    if idOrNum[:4] == "heap":
        return getTaskFilenameByNum( idOrNum[4:], "heap")
        pass
    print("Unknown task id or number format");
    pass

def getTaskByIdOrNum( idOrNum, location="*"):
    if idOrNum.isnumeric():
        return getTaskById( idOrNum, location )
        pass
    if idOrNum[:2] == "id":
        return getTaskById( idOrNum[2:], location )
        pass
    if idOrNum[:3] == "cur":
        return getTaskByNum( idOrNum[3:], "cur")
        pass
    if idOrNum[:4] == "heap":
        return getTaskByNum( idOrNum[4:], "heap")
        pass
    print("Unknown task id or number format");
    pass



def getTaskFilenameByNum( num, location ):
    return getTaskByNum( num, location )["fullfilename"]
    pass

def getTaskById(id, location):
    filename = getTaskFilenameById( id, location )
    task = loadYaml( filename )
    task["fullfilename"] = filename
    return task
    pass

def getTaskByNum( num, location ):
    tasks = listTasks( location )
    for task in tasks:
        if int(task["No."]) == int(num):
            return task
    print("Task "+num+" not found in "+location)
    pass



def findTaskFiles(location, pattern):
    return glob.glob( tskpath() + "/"+location+"/*/"+pattern)
    pass

def listTasks(location):
    scope = getScope();
    files = findTaskFiles( location, "*.md" )
    tasks = []
    for filename in files:
        task = loadYaml(filename)
        task["fullfilename"] = filename
        addItem = True
        for key in scope:
            addItem = addItem and ( scope[key] == "" or scope[key] == task[key] )
            pass
        if not addItem:
            continue
            pass
        tasks.append( task )
        pass
    tasks = sorted(tasks, key = lambda task : task["id"])
    key = 0
    for task in tasks:
        key = key+1
        task["No."] = key
        pass
    return tasks
    pass

def getConfigParam(param):
    return loadYaml( tskpath() + "/config.yaml" )[param]
    pass

def loadYaml(filename):
    with open( filename ) as f:
        return next(yaml.load_all(f, Loader=yaml.loader.UnsafeLoader))
        pass
    pass

def saveYaml(filename, data):
    with open( filename, 'w' ) as f:
        yaml.dump( data, f )
        pass
    pass

def gitInitIfNotPresent():
    workingdir = tskpath()
    if os.path.isdir( workingdir+"/.git"):
        return
        pass
    curpath = os.getcwd();
    os.chdir(workingdir);
    os.system("git init > /dev/null");
    os.chdir(curpath);
    pass

def gitAddCommitTask(message):
    gitInitIfNotPresent()
    curpath = os.getcwd();
    os.chdir(tskpath());
    os.system("git add ./*.md > /dev/null && git commit -m '"+message+"' > /dev/null");
    os.chdir(curpath);
    pass

def getLastId():
    files = findTaskFiles("*", "*.md")
    maxId = -1
    for filename in files :
        # Open the file and load the file
        id = loadYaml( filename )["id"]
        if id > maxId:
            maxId = id
            pass
        pass
    return maxId
    pass

def newScope():
    return {
        "project":"",
        "context":""
        }
    pass

def loadScope():
    scope = newScope()
    try:
        data = loadYaml( tskpath()+"/scope.yaml")
        for key in scope:
            try:
                scope[key] = data[key]
            except:
                pass
            pass
    except:
        pass
    return scope
    pass

def mergeScope( orig, changes ):
    scope = orig
    for key in changes:
        if changes[key] == "":
            continue
        scope[key] = changes[key]
    return scope
    pass

def parseFilter( filterstring ):
    scope = newScope()
    if filterstring == "":
        return scope
        pass
    # split by ,
    pairs = filterstring.split(",")
    for pair in pairs:
        keyvalue = pair.split(":")
        key = keyvalue[0]
        value = keyvalue[1]
        if key == "c":
            key = "context"
            pass
        if key == "p":
            key = "project"
            pass
        scope[key] = value
        pass
    return scope
    pass

def getDefaultContextForProject( projectName ):
    try:
        return loadYaml( tskpath() + "/projects/" + projectName + ".yaml")["defaultContext"]
    except:
        return ""
    pass

def getScope():
    scope = loadScope()
    scope = mergeScope( scope, parseFilter(os.getenv(cmd.upper(),"")) )
    for key in scope:
        scope[key] = os.getenv(cmd.upper() + "_" + key.upper(), scope[key])
        pass
    if scope["context"] == "" and scope["project"] != "":
        scope["context"] = getDefaultContextForProject( scope["project"] )
        pass
    return scope
    pass

def saveScope( scope ):
    saveYaml( tskpath()+"/scope.yaml", scope)
    pass
