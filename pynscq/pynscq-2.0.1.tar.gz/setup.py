#
# Copyright 2020-2023 NVIDIA Corporation.  All rights reserved.
#
# NOTICE TO USER:
#
# This source code is subject to NVIDIA ownership rights under U.S. and
# international Copyright laws.  Users and possessors of this source code
# are hereby granted a nonexclusive, royalty-free license to use this code
# in individual and commercial software.
#
# NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOURCE
# CODE FOR ANY PURPOSE.  IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR
# IMPLIED WARRANTY OF ANY KIND.  NVIDIA DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOURCE CODE, INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
# IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL,
# OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS,  WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
# OR OTHER TORTIOUS ACTION,  ARISING OUT OF OR IN CONNECTION WITH THE USE
# OR PERFORMANCE OF THIS SOURCE CODE.
#
# U.S. Government End Users.   This source code is a "commercial item" as
# that term is defined at  48 C.F.R. 2.101 (OCT 1995), consisting  of
# "commercial computer  software"  and "commercial computer software
# documentation" as such terms are  used in 48 C.F.R. 12.212 (SEPT 1995)
# and is provided to the U.S. Government only as a commercial end item.
# Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through
# 227.7202-4 (JUNE 1995), all U.S. Government End Users acquire the
# source code with only those rights set forth herein.
#
# Any use of this source code in individual and commercial software must
# include, in the user documentation and internal comments to the code,
# the above Disclaimer and U.S. Government End Users Notice.
#

from setuptools import find_packages, setup

# read the contents of your README file
long_description = open("README.md").read()

setup(name='pynscq',
      version='2.0.1',
      packages=find_packages(),
      python_requires='>=3',
      install_requires=[],
      package_data={},
      scripts=['bin/lsnvswitch.py', 'bin/list_switch_errors.py', 'bin/list_switch_info.py'],
      author="NVIDIA Corporation",
      author_email="CUDAIssues@nvidia.com",
      description="Python bindings for the NVSwitch Configuration and Query (NSCQ) library",
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords="nvidia nvswitch nscq management nvlink")
