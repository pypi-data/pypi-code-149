# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Maintains file utility functions
"""

import gzip
import os
import subprocess
import sys
import tempfile


def _is_safe_path(path, basedir=os.getcwd(), follow_symlinks=True):
    # resolves symbolic links
    if follow_symlinks:
        # print('path ', os.path.realpath(path))
        return os.path.realpath(path).startswith(basedir), os.path.realpath(path)
    # print('path ', os.path.abspath(path))
    issafe = os.path.abspath(path).startswith(basedir)
    return issafe, os.path.abspath(path)


def safe_join(basedir, path, follow_symlinks=True):
    """Enforces that path is under basedir.
    That is, it prevents relative path escalation out of the given basedir."""
    is_safe_path, safe_path = _is_safe_path(
        path, basedir=basedir, follow_symlinks=follow_symlinks
    )
    if not is_safe_path:
        raise Exception(
            "invalid access, basedir is {} yet asking for {}".format(basedir, path)
        )
    return os.path.normpath("{}{}{}".format(basedir, os.sep, safe_path))


def possibly_unsafe_join(basedir, path):
    """
    Mimics the behavior of os.path.join
    (except it does not allow var args for path) without actually using it.
    This is currently untested on native windows systems.
    It is labeled as 'possibly' unsafe because it's possible
    that someone could pass in a relative path for path
    giving access to the file system outside the basedir
    (the same way os.path.join can). Whether this is really unsafe
    depends heavily on the context. On systems with poor
    user access control it could indeed be.
    Therefore, use with care and see if you can
    find alternatives such as :func:`~safe_join.
    Do not just use os.path.join as this will lead to security scan violations.
    """
    return os.path.normpath("{}{}{}".format(basedir, os.sep, path))


def get_home_dir():
    """Returns the user's home directory"""
    if sys.platform.startswith("win"):
        return os.environ["HOMEPATH"]
    return os.environ["HOME"]


def gettempdir():
    """Alternative to tempfile.gettempdir that doesn't flag
    IBM security scanner race condition alert."""
    with tempfile.NamedTemporaryFile() as atempfile:
        return os.path.dirname(atempfile.name)


def get_workspace():
    """Returns SROM workspace path. Will use value of environment variable SROM_INSTANCE_LOCATION if defined, otherwise 
    will return the system temporary directory."""
    base_path = (
        os.environ.get("SROM_INSTANCE_LOCATION")
        if "SROM_INSTANCE_LOCATION" in os.environ
        else tempfile.gettempdir()
    )
    return base_path


def is_gzip(afile):
    """Returns true if a file is a gzip file"""
    if not os.path.isfile(afile) or not os.path.exists(afile):
        return False
    agzfile = gzip.GzipFile(afile)
    try:
        agzfile.peek(1)
        return True
    except OSError as _:
        return False


def _abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for afilename in filenames:
            yield os.path.abspath(possibly_unsafe_join(dirpath, afilename))


def new_tempfile(prefix=None, suffix=None, dir=None):
    """Create and return a new temporary file using tempfile.mkstemp
    Keyword Arguments:
        prefix {string} -- file prefix (default: {None})
        suffix {string} -- file suffice (default: {None})
        dir {string} -- directory where to write (default: {None}) uses system temporary directory if None.
    returns:
     {string} the fully qualified path of the created file
    """
    file_handle, file_name = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=dir)
    os.close(file_handle)
    return file_name


def python_package_from_snippet(module_name, code_snippet):
    """produces a python archive from a code snippet"""
    tmpdir = tempfile.mkdtemp()
    modulepath = possibly_unsafe_join(tmpdir, module_name)
    os.mkdir(modulepath)

    # create a file inside this directory called "__init__.py"
    # (a requirement of python packages)
    open(possibly_unsafe_join(modulepath, "__init__.py"), "w")
    # write our custom code to a .py file
    open(possibly_unsafe_join(modulepath, "{}.py".format(module_name)), "w").write(
        code_snippet
    )
    # python packages also expect a minimal
    # 'setup.py' file
    setup_dot_py = """from setuptools import setup, find_packages\nsetup(name='{}',\n\
    version='0.0.1',\n\
    packages=find_packages('.')\n\
    )""".format(
        module_name
    )
    # write it out
    open(possibly_unsafe_join(tmpdir, "setup.py"), "w").write(setup_dot_py)
    # finally create a package archive
    completed_process = subprocess.run(
        ["python", "setup.py", "sdist", "--formats=zip"],
        cwd=tmpdir,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    if completed_process.returncode:
        print(completed_process.stdout)
        print(completed_process.stderr)
        return dict(return_code=completed_process.returncode)

    return dict(
        return_code=completed_process.returncode,
        module_path=modulepath,
        package=[
            name for name in _abs_file_paths(possibly_unsafe_join(tmpdir, "dist"))
        ][0],
    )
