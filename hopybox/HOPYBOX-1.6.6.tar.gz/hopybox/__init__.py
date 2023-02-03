'''
            Copyright (c) 2022 HOStudio123(ChenJinlin) ,
                      All Rights Reserved.
'''
from .hopter import Error_ptc
import os
try:
  from .__main__ import *
except Exception as e:
  Error_ptc('Sorry,The program has an error and cannot continue to run',str(e))
  print('\033[93mWARNING:The program is about to restart')
  os.system('python3 -m hopybox')