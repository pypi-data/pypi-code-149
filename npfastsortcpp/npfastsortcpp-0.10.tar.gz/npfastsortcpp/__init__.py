import os
import pathlib

pyxcode = """
import cython
cimport cython

ctypedef fused real:
    cython.short
    cython.ushort
    cython.int
    cython.uint
    cython.long
    cython.ulong
    cython.longlong
    cython.ulonglong
    cython.float
    cython.double


cdef extern from "<ppl.h>" namespace "concurrency":
    cdef void parallel_sort[T](T first, T last) nogil

@cython.boundscheck(False)
@cython.wraparound(False) 
def parallelsort(real[:] a):
    parallel_sort(&a[0], &a[a.shape[0]])
"""
wdi = os.path.normpath((os.path.abspath(os.path.dirname(__file__))))
wdina = os.path.normpath((os.path.dirname(__file__)))

pyxf_ = os.path.normpath(os.path.join(wdi, "npparallelsortcpp.pyx"))
pyxf = pathlib.Path(pyxf_).as_posix()
wdi_ = "."
setuptoolscode = rf"""
from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "npparallelsortcpp",
        [{repr(pyxf)}],
        language="c++",

    )
]
setup(
    name='npparallelsortcpp',
    ext_modules=cythonize(ext_modules, compiler_directives={{'language_level': "3"}}),
)"""
import sys
import numpy as np
import warnings

npfastsortconfig = sys.modules[__name__]
npfastsortconfig.enablewarning = True


def parallelsort(a):
    if npfastsortconfig.enablewarning:
        warnings.warn("You are using numpy.sort", RuntimeWarning, stacklevel=2)
    return np.sort(a)


try:
    from .npparallelsortcpp import parallelsort
except ImportError:
    import sys
    import subprocess

    sourcefile = pyxf_

    setupfile = os.path.normpath(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "setuppara.py")
    )

    with open(sourcefile, mode="w", encoding="utf-8") as f:
        f.write(pyxcode)
    with open(setupfile, mode="w", encoding="utf-8") as f:
        f.write(setuptoolscode)
    import Cython, setuptools

    command = [sys.executable, setupfile, "build_ext", "--build-lib", wdi]

    print("______________________________")
    print("Compiling ... ")
    print(
        "If you get an error, "
        "download:\n https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&passive=false&cid=2030"
    )
    print("and install: MSVC ..... C++ x64/x86 build tools")
    print("______________________________")
    subprocess.run(command)

    try:
        from .npparallelsortcpp import parallelsort
    except Exception as fe:
        print(fe)
