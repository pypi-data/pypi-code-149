#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 07:34:57 2022

@author: root
"""

import qedata
from datetime import datetime, timedelta
import qereal
import pandas as pd
import numpy as np
from .qelogger import initTableLogger, logger, getLoggerPath
import os
import copy


def get_qemonitor_log(user,password,mode):
    
    max_line = 5000
#     current_line = 0    
    log_path = getLoggerPath()
    if mode == 'real':  
        filename = f'{log_path}/qelog_real_{user}'           
    elif mode == 'simu':
        filename = f'{log_path}/qelog_{user}'
    pd.set_option('max_colwidth',180)
    if os.path.isfile(filename):
        try:
            df = pd.read_csv(filename,sep='\n',header=None,memory_map=True)    
            #LT = len(df)
        except:
            try:
                df = pd.read_csv(filename,sep='\n',header=None,memory_map=True,encoding='GB18030')
            except:
                return pd.DataFrame()
            
        
        logdata = df[-max_line:]
    else:
        logdata = pd.DataFrame()

    return logdata
            
    
