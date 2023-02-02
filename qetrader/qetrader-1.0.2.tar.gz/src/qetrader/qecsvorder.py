# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:49:53 2022

@author: ScottStation
"""
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:49:53 2022

@author: ScottStation
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:49:53 2022

@author: ScottStation
"""
import os
import fnmatch
import time
import pandas as pd
import numpy as np
from datetime import datetime , timedelta
from qesdk import get_dominant_instID
#from qedata import get_valid_instID, get_future_details
from .qelogger import logger
from .qeglobal import instSetts, getInstAccID, getExemode
from .qeinterface import qeStratBase, make_order, cancel_order
import traceback
import random


ordercsv_filename = 'qeorders.csv'
prods_sfe = ['ag','cu','al','pb','ni','hc','rb','ru','au','zn','bu','fu','sp','sn','ss','wr']
prods_ine = ['sc','lu','nr','bc']
prods_zce = ['PM', 'WH', 'SR', 'CF', 'TA', 'OI', 'RI', 'MA', 'FG', 'RS', 'RM', 'ZC', 'JR', 'LR', 'SF', 'SM', 'CY', 'AP', 'CJ', 'UR', 'SA', 'PF', 'PK', 'ME','RO','TC','WS','ER']
prods_ccf = ['IF','IH','IC','T','TF','TS',"IO",'MO','IM']
prods_dce = ['a', 'b', 'c', 'm', 'y', 'p', 'l', 'v', 'j', 'jm', 'i', 'jd', 'fb', 'bb', 'pp', 'cs', 'eg', 'rr', 'eb', 'pg', 'lh']

def getValidInstID(instid):
    inst = instid
    prod = inst[:2]
    if prod[1].isdigit():
        prod = inst[:1]
    if instid.find('9999') >= 0:
        inst = get_dominant_instID(prod)
        
    elif inst.find('.') < 0:
        exid =''
        if prod.lower() in prods_sfe:
            exid ='SFE'
        elif prod.lower() in prods_dce:
            exid ='DCE'
        elif prod.lower() in prods_ine:
            exid ='INE'
        elif prod.upper() in prods_ccf:
            exid ='CCF'
        elif prod.upper() in prods_zce:
            exid ='ZCE'
            if len(inst)== 5:
                inst = inst[:2]+'2'+inst[2:]
        elif inst[:3]=='100' or inst[:3]=='510':
            exid ="SSE"
        elif inst.find('T+D') >= 0:
            exid = "SGE"
        #print(prod,exid)
        inst = inst+'.'+ exid
    elif inst == 'AU99.99':
        inst = inst+'.SGE'
    else:    
        name = inst.split('.')
        if name[-1] == "SHFE":
            inst = name[0]+".SFE"
        elif name[-1] == "CZCE":
            inst = name[0]+".ZCE"
        elif name[-1] == "CFFEX":
            inst = instid[:-6]+'.CCF'
    return inst.upper()

class qeCsvOrders(qeStratBase):
    def __init__(self):
        self.autofiles=[]
        self.ordertime = 0
        self.crontab = {}
        self.destpos = {}
        domiAU = get_dominant_instID('AU')
        domiT = get_dominant_instID('T')
        self.instid =[domiAU, domiT]
        self.name = 'csvorders'
        self.newinst = False
        self.useinsts = []
        
    def handleData(self, context):
        for i in range(len(context.accounts)):
            if not context.accounts[i].loadReady :
                return
        try:
            #for i in range(len(self.instid)):
            #    print('csvorder handle', self.instid[i], context.getCurrent(self.instid[i]))
            self.newinst = False
            self.readCsvFiles(context)
            self.checkCsvExec(context)
            self.useinsts = list(set(self.useinsts))
            #if not self.newinst:
            self.checkOrders(context)
        except:
            traceback.print_exc()
        
    def crossDay(self, context):
        domiAU = get_dominant_instID('AU')
        domiT = get_dominant_instID('T')
        self.instid =[domiAU, domiT]
        self.instid += list(self.destpos.keys())
                
        
    
        
    def updateOrders(self, context, df, fn):
        try:
            i = -1
            errmsg = ''
            #algo = False
            df.columns=['account','instid','longvol','shortvol','ordertype','price','diffticks',\
                            'timecond','trackmode','tracktime','trackticks','trackcount',\
                            'canceltime','cancelticks','algo','algotime','algofactor']
            insts = []
            num = 0
            accounts = context.token.split('_')
            #print(accounts)
            for i in range(len(df)):
                #print(df.account[i])
                if df.account[i] in accounts  or df.account[i]=='*':
                    num += 1 
                    ## if it is my orders
                    accid = accounts.index(df.account[i]) if df.account[i] != '*' else 0
                    instid = getValidInstID(df.instid[i])
                    #if is_future_expired(instid):
                    #   logger.info(f"{instid} in csv orders is expired")
                    #    continue
                    #print('accid',accid, instid)
                    #logger.info(f'accid,{accid}, {instid}')
                    algo = False
                    d = {}
                    d['longvol'] = int(df.longvol[i])
                    d['shortvol'] = int(df.shortvol[i])
                    d['price'] = float(df.price[i])
                    d['diffticks'] = int(df.diffticks[i])
                    d['timecond'] = df.timecond[i].replace(' ','')    
                    if not d['timecond'] in ['FAK',"FOK","GFD"]:
                        errmsg = u'无法识别时间类型'
                        raise KeyError
                    d['algo'] = df.algo[i].replace(' ','')
                    d['algotime'] =max(0,int(df.algotime[i]))
                    d['algofactor'] =int(df.algofactor[i])
                    if not d['algo'] in ['twap','no']:
                        errmsg = u'无法识别算法交易类型'
                        raise KeyError
                    if d['algo'] in ['twap']:
                        algo = True
                        if d['algotime'] == 0:
                            errmsg = u'算法交易执行时间不能为0'
                            raise KeyError
                        if d['timecond'] != 'GFD':
                            errmsg = u'算法交易时间类型只能为GFD'
                            raise KeyError
                        
                    d['trackmode'] = max(0,int(df.trackmode[i]))
                    d['trackticks'] = max(0,int(df.trackticks[i]))
                    d['tracktime'] = max(0,int(df.tracktime[i]))
                    d['trackcount'] = max(0,int(df.trackcount[i]))
                    d['canceltime'] = max(0,int(df.canceltime[i]))
                    d['cancelticks'] = max(0,int(df.cancelticks[i]))
                    d['accid']  = accid
                    if not algo:
                        if d['trackmode'] > 2:
                            errmsg = u'无法识别追单模式，只能是0-2'
                            raise KeyError
                        if (d['trackmode'] == 1 and d['timecond'] != 'FAK' ) :
                            errmsg = u'追单模式1 必须对应时间类型为FAK'
                            raise KeyError
                            
                        if (d['trackmode'] == 2 and d['timecond'] != 'GFD'):  
                            errmsg = u'追单模式2 必须对应时间类型为GFD'
                            raise KeyError
                        if (d['trackmode'] == 2 and d['trackticks'] == 0 and d['tracktime'] == 0):  
                            errmsg = u'追单模式2 追单时间和追单超价必须有一个大于0'
                            raise KeyError
                        if (d['trackmode'] > 0 and d['trackcount'] == 0 ):  
                            errmsg = u'追单模式下最大追单次数必须大于0'
                            raise KeyError
                    #d['lock'] = df.lock[i].replace(' ','') 
                    d['ordertype'] = df.ordertype[i].replace(' ','')
                    #if not d['lock'] in ['y','n','c']:
                    #    errmsg = u'无法识别锁仓模式，只能是 "y","n","c"其中之一'
                    #    raise KeyError
                    if not d['ordertype'] in ['limit','market','opponent','quote','current']:
                        errmsg = u"无法识别价格类型，只能是 'limit','market','opponent','quote','current'其中之一"
                        raise KeyError
                    d['status'] = 'commited'
                    if instid in insts:
                        logger.warning(f'有两条或以上指令为同一个合约{instid}，只有最后一条指令会生效')
                    else:
                        insts.append(instid)
                    self.destpos[instid] = d
                    
                    if not instid in self.instid:
                        self.instid.append(instid)
                        self.newinst = True
                    #print(f'{instid} 目标仓位 {d["longvol"]} {d["shortvol"]}')    
                    longpos = context.getAccountPosition(instid,'long','volume')
                    shortpos = context.getAccountPosition(instid, 'short','volume')
                    if longpos != d ['longvol'] or shortpos != d['shortvol']:
                        logger.info(f'change position of :{instid} from {longpos},{shortpos} to  {d["longvol"]} {d["shortvol"]}')    
                    #self.useinsts.append(instid)
            #context.addNewInsts(adds)
            if len(df) > 0 :
                if num > 0:
                    print(f'加载csv文件成功，生成 {num} 条指令')
                else:
                    print('加载csv文件成功，但没有发现当前账户相关指令，请检查csv文件账户名')
            
            logger.info(f'updateOrders: {insts}, {len(self.destpos)}')
                        
        except Exception as e:
            if errmsg != '':
                logger.warning(f"导入csv文件orders错误，csv文件第{i+2}行 错误说明：{errmsg}")
            else:    
                logger.warning(f"导入csv文件orders错误，csv文件第{i+2}行 错误说明：{e.__traceback__.tb_lineno}行 {e}")
    
    def checkDF(self,context,  df, fname):
        try:
            i = -1
            errmsg = ''
            
            #df.columns=['account','instid','vol','lock','ordertype','price','diffticks',\
            #                'timecond','trackmode','tracktime','trackticks','trackcount',\
            #                'canceltime','cancelticks','algo','algotime','algofactor']
            df.columns=['account','instid','longvol','shortvol','ordertype','price','diffticks',\
                            'timecond','trackmode','tracktime','trackticks','trackcount',\
                            'canceltime','cancelticks','algo','algotime','algofactor']    
            
            accounts = context.token.split('_')
            for i in range(len(df)):
                if df.account[i] in accounts or df.account[i]=='*':
                    #print(df.account[i],i,accounts)
                    ## if it is my orders
                    #instid = getValidInstID(df.instid[i])
                    #if not isInstNameValid(instid):
                    #     raise KeyError
                    algo = False     
                    d={}
                    d['longvol'] = int(df.longvol[i])
                    d['shortvol'] = int(df.shortvol[i])
                    d['price'] = float(df.price[i])
                    d['diffticks'] = int(df.diffticks[i])
                    d['timecond'] = df.timecond[i].replace(' ','')    
                    if not d['timecond'] in ['FAK',"FOK","GFD"]:
                        errmsg = u'无法识别时间类型'
                        raise KeyError
                    d['algo'] = df.algo[i].replace(' ','')
                    d['algotime'] = max(0,int(df.algotime[i]))
                    if d['algo'] in ['twap']: 
                        algo = True
                        if d['algotime'] == 0:
                            errmsg = u'算法交易执行时间不能为0'
                            raise KeyError
                        if d['timecond'] != 'GFD':
                            errmsg = u'算法交易时间类型只能为GFD'
                            raise KeyError
                            
                    d['algofactor'] =int(df.algofactor[i])
                    if not d['algo'] in ['twap','no']:
                        errmsg = u'无法识别算法交易类型'
                        raise KeyError
                    d['trackmode'] = max(0,int(df.trackmode[i]))
                    d['trackticks'] = max(0,int(df.trackticks[i]))
                    d['tracktime'] = max(0,int(df.tracktime[i]))
                    d['trackcount'] = max(0,int(df.trackcount[i]))
                    d['canceltime'] = max(0,int(df.canceltime[i]))
                    d['cancelticks'] = max(0,int(df.cancelticks[i]))
                    if not algo:
                        if d['trackmode'] > 2:
                            errmsg = u'无法识别追单模式，只能是0-2'
                            raise KeyError
                        if (d['trackmode'] == 1 and d['timecond'] != 'FAK' ) :
                            errmsg = u'追单模式1 必须对应时间类型为FAK'
                            raise KeyError
                            
                        if (d['trackmode'] == 2 and d['timecond'] != 'GFD'):  
                            errmsg = u'追单模式2 必须对应时间类型为GFD'
                            raise KeyError
                        if (d['trackmode'] == 2 and d['trackticks'] == 0 and d['tracktime'] == 0):  
                            errmsg = u'追单模式2 追单时间和追单超价必须有一个大于0'
                            raise KeyError
                        if (d['trackmode'] > 0 and d['trackcount'] == 0 ):  
                            errmsg = u'追单模式下最大追单次数必须大于0'
                            raise KeyError
                    #if not df.lock[i].replace(' ','') in ['y','n','c']:
                    #    errmsg = u'无法识别锁仓模式，只能是 "y","n","c"其中之一'
                        
                    #    raise KeyError
                    if not df.ordertype[i].replace(' ','') in ['limit','market','opponent','quote','current']:
                        errmsg = u"无法识别价格类型，只能是 'limit','market','opponent','quote','current'其中之一"
                        raise KeyError
                    #self.useinsts.append(instid)    
            return True            
    
        except Exception as e:
            if errmsg != '':
                logger.warning(f"导入csv文件orders错误，csv文件第{i+2}行 错误说明：{errmsg}")
            else:    
                logger.warning(f"导入csv文件orders错误，csv文件第{i+2}行 错误说明：{e.__traceback__.tb_lineno}行 {e}")
            return False  
           
    
    def readCsvFiles(self,context):
        global ordercsv_filename
        if getExemode():
            #syspath = os.getcwd()
            csvdir = 'csvfiles' if context.runmode=='simu' else 'rcsvfiles'
            syspath = csvdir
            fname = syspath + '\\'+ ordercsv_filename
        else:
            try:
                from .qedockerconfig import log_path
                syspath = '/home/'+context.user
                fname = syspath +'/'+ordercsv_filename
            except:
                fname = './'+ ordercsv_filename
                syspath = './'
        
        if os.path.exists(fname):
            ordertime = os.path.getmtime(fname)
            if ordertime != self.ordertime:
                self.ordertime = ordertime
                df = pd.read_csv(fname,header=None)
                df.columns=df.iloc[0,:]
                df = df.drop(index=0)
                df.index = range(len(df))
                self.updateOrders(context, df,fname)
                
        autofiles = [csv for csv in os.listdir(syspath) if fnmatch.fnmatch(csv, 'qeorders*.csv')]
        for fn in autofiles:
            timestr = fn[8:-4]
            if len(timestr) in [6, 8, 14] and timestr.isdigit():
                try:
                    if len(timestr)== 8:
                        pendtime=datetime.strptime(timestr, '%Y%m%d')
                    elif len(timestr)==6:
                        daystr = datetime.today().strftime('%Y-%m-%d')
                        pendtime= datetime.strptime(daystr+timestr, '%Y-%m-%d%H%M%S')
                    else:
                        pendtime=datetime.strptime(timestr, '%Y%m%d%H%M%S')
                    
                    if pendtime > datetime.now() - timedelta(seconds=2):
                        ordertime = os.path.getmtime(fn)
                        #logger.info(f'loading future file {fn}')
                        #if pendtime in self.crontab:
                        #    logger.info(f'csvorder: {fn} {self.crontab[pendtime][2]} {ordertime}')
                       
                        if not pendtime in self.crontab or (pendtime in self.crontab and ordertime > self.crontab[pendtime][2]): 
                                df =  pd.read_csv(fn, header=None)
                                df.columns=df.iloc[0,:]
                                df = df.drop(index=0)
                                df.index = range(len(df))
                                #print('checkdf', df)
                                ret = self.checkDF(context, df, fn)
                                if ret:
                                    logger.info(f'csvorder: {fn} added {pendtime} {ordertime}')
                                    self.crontab[pendtime] = [df,fn,ordertime,False]
                        #elif pendtime in self.crontab and ordertime == self.crontab[pendtime][2]:
                        #     crontab[pendtime] = self.crontab[pendtime]
                        #     df = crontab[pendtime][0]
                except:
                    print(u'无法识别csvorder文件'+fn)
                    traceback.print_exc()
        #print(self.crontab)
        removes=[]
        for t in self.crontab:
            if t < datetime.now()-timedelta(minutes=1) and self.crontab[t][3]:
                removes.append(t)
        for r in removes:
            del self.crontab[t]
            #print('delete crontab ', t)       
        #crontab = {}
                
        
    def checkCsvExec(self, context):
        #print(self.crontab.keys())
        #print(datetime.now())
        timetags = list(self.crontab.keys())
        timetags.sort()
        #logger.info(f'timetags:{timetags}')
        for t in timetags:
            if datetime.now() >= t:
                [df,fn,ot,status] = self.crontab[t]
                #print(fn, len(df),ot)
                if len(df) > 0 and not status:
                    logger.info(f'execute csv:{fn}')
                    self.crontab[t][3]=True
                    self.updateOrders(context,df,fn)
        
        #self.crontab[t] = [pd.DataFrame(),fn,ot]
    
    def makeOrder(self,context,instid, posinfo, action, dirstr,vol):
        direction = 1 if dirstr=='long' else -1
        if action =='close':
            direction = -direction
    
        autoremake =[posinfo['trackmode'],posinfo['tracktime'],posinfo['trackticks'],posinfo['trackcount']]   
        autocancel = [posinfo['canceltime'],posinfo['cancelticks']]
        price = context.getCurrent(instid)
        pricediff = posinfo['diffticks']
        ordertype = 'limit'
        if posinfo['ordertype'] == 'market':
            ordertype = 'market'
        elif posinfo['ordertype'] == 'limit':
            price = posinfo['price']
        elif posinfo['ordertype'] == 'quote':
            price = context.getDataSlide(instid, 'b1_p') if direction > 0 else context.getDataSlide(instid, 'a1_p')
        elif  posinfo['ordertype'] == 'opponent':
            price = context.getDataSlide(instid, 'b1_p') if direction < 0 else context.getDataSlide(instid, 'a1_p')
            
        if instSetts.get(instid):
            ticksize = instSetts[instid]['ticksize']
            if posinfo['ordertype'] != 'market' and pricediff != 0:
                price += pricediff * ticksize
        
        #context, instid, direction, price, volume, ordertype="limit", action="open", closetype='auto', autoremake=[0,0], autocancel=[0,0]
        if price > 0:
            if posinfo['algo'] =='twap':
                logger.info(f'CSVOrder algo trade: {instid}, {action},{direction},price:{price},vol:{vol},{posinfo["ordertype"]},algosecs:{posinfo["algotime"]}')
                #print(f'{context.curtime} CSVOrder algo trade: {instid}, {action},{direction},price:{price},vol:{vol},{posinfo["ordertype"]},algosecs:{posinfo["algotime"]}')            
                algo_trade(context, instid, direction, price,vol,posinfo['algotime'],posinfo['algofactor'],ordertype,action,posinfo['algo'],timecond=posinfo['timecond'],accid=posinfo['accid'])
            else:    
                logger.info(f'CSVOrder: {instid}, {action},{direction},price:{price},vol:{vol},{posinfo["ordertype"]}')
                #print(f'{context.curtime} CSVOrder: {instid}, {action},{direction},price:{price},vol:{vol},{posinfo["ordertype"]}')            
                make_order(context,instid,direction,price,vol,ordertype,action,timecond=posinfo['timecond'], autoremake=autoremake, autocancel=autocancel,accid=posinfo['accid'])
        else:
            logger.warning(f'csvorders: {instid} 下单价格必须为正数，请检查设置并确保该合约在strat中被包含并在交易时间下单')
    
    
    def cancelOrders(self, context, instid):
        for i in range(len(context.accounts)):
            tmporders = context.accounts[i].orders.copy()
            for oid, order in tmporders.items():
                if order['instid'] == instid and order['leftvol'] > 0:
                    try:
                      print('cancel',oid,order['instid'],order['leftvol'])
                      cancel_order(context, oid)
                    except Exception as e:
                      logger.info(f'cancelOrders: {e}')
    
    '''
    def checkOrdersOld(self,context):
        for inst in self.destpos:
            posinfo = self.destpos[inst]
            price = context.getCurrent(inst)
            if price == 0:
                logger.info(f'{inst} not listed')
                continue
            if posinfo['status'] == 'commited':
            ## deal with makes
                  
                lpos = context.getAccountPosition(inst, 'long', 'volume')
                spos = context.getAccountPosition(inst, 'short', 'volume')
                netpos = lpos - spos
                vol = posinfo['vol']
                #logger.info(f'deal with make/cancel,{inst},{pos},{vol}')        
                self.cancelOrders(context, inst)
                if posinfo['lock'] == 'y':
                    if netpos > vol:
                        self.makeOrder(context,inst, posinfo,'open','short',netpos-vol)
                    elif netpos < vol:
                        self.makeOrder(context,inst, posinfo,'open','long',vol - netpos)
                elif posinfo['lock'] == 'n':
                    if netpos > vol:
                        diff = netpos - vol
                        if lpos >= diff:
                            self.makeOrder(context,inst, posinfo,'close','long',diff)
                            #print('n1',netpos, vol)
                        else:
                            if lpos > 0:
                                self.makeOrder(context, inst, posinfo, 'close', 'long', lpos)
                            self.makeOrder(context, inst, posinfo,'open','short', diff - lpos)
                            #print('n2',netpos, vol)
                    elif netpos < vol:
                        diff = vol  - netpos
                        if spos >= diff:
                            self.makeOrder(context,inst, posinfo,'close','short',diff)
                            #print('n3',netpos, vol)
                        else:
                            if spos > 0:
                                self.makeOrder(context, inst, posinfo, 'close', 'short', spos)
                            self.makeOrder(context, inst, posinfo,'open','long', diff - spos)
                            #print('n4',netpos, vol)
                elif posinfo['lock'] == 'c':
                    if vol == 0:
                        if lpos > 0:
                            self.makeOrder(context,inst, posinfo,'close','long',lpos)
                        if spos > 0:
                            self.makeOrder(context,inst, posinfo,'close','short',spos)
                    elif vol > 0:
                        if spos > 0:
                            self.makeOrder(context, inst,posinfo , 'close', 'short',spos)
                        if lpos > vol:
                            self.makeOrder(context, inst, posinfo,'close', 'long', lpos - vol)
                        elif lpos < vol:
                            self.makeOrder(context, inst, posinfo, 'open','long', vol-lpos)
                    else:
                        if lpos > 0:
                            self.makeOrder(context, inst, posinfo,'close','long',lpos)
                        if -spos > vol:
                            self.makeOrder(context, inst, posinfo, 'open','short', -spos-vol)
                        elif -spos < vol:
                            self.makeOrder(context, inst, posinfo, 'close','short', vol +spos)
                        
                
    
                self.destpos[inst]['status'] = 'executed'  
                  
                #logger.info(f'status:{self.destpos[inst]["status"]}')
            ## deal with cancels
    '''
    
    def checkOrders(self,context):
        for inst in self.destpos:
            posinfo = self.destpos[inst]
            price = context.getCurrent(inst)
            if price == 0:
                #logger.info(f'{inst} not listed')
                continue
            if posinfo['status'] == 'commited':
            ## deal with makes
                  
                lpos = context.getAccountPosition(inst, 'long', 'volume')
                spos = context.getAccountPosition(inst, 'short', 'volume')
                #netpos = lpos - spos
                #vol = posinfo['vol']
                #logger.info(f'deal with make/cancel,{inst},{pos},{vol}')        
                self.cancelOrders(context, inst)
                
                if posinfo['longvol'] > lpos:
                    self.makeOrder(context, inst, posinfo, 'open','long',posinfo['longvol'] - lpos)
                elif posinfo['longvol'] < lpos:
                    self.makeOrder(context, inst, posinfo, 'close','long',lpos - posinfo['longvol'] )    
                
                if posinfo['shortvol'] > spos:
                    self.makeOrder(context, inst, posinfo, 'open','short',posinfo['shortvol'] - spos)
                elif posinfo['shortvol'] < spos:
                    self.makeOrder(context, inst, posinfo, 'close','short',spos - posinfo['shortvol'] )    
                
                
                
                '''
                if vol ==0 and not posinfo['lock']:
                    self.makeOrder(context,inst, posinfo,'close','long',lpos)
                    self.makeOrder(context,inst, posinfo,'close','short',spos)
                
                elif pos == vol:
                    #logger.info(f'no make: ,{inst},{pos},{vol}')    
                    continue
                elif pos > vol:
                    if pos <= 0:
                        #open short
                        self.makeOrder(context,inst, posinfo,'open','short',pos-vol)
                    elif vol >= 0:
                        #close long
                        self.makeOrder(context,inst, posinfo,'close','long',pos-vol)
                    else:
                        #open short, close long
                        self.makeOrder(context,inst, posinfo,'open','short',abs(vol))
                        self.makeOrder(context,inst, posinfo,'close','long',abs(pos))
                else:
                    if pos >= 0:
                        #open long
                        self.makeOrder(context,inst, posinfo,'open','long',vol-pos)
                    elif vol <= 0 :
                        #close short
                        self.makeOrder(context,inst, posinfo,'close','short',vol-pos)
                    else:
                        #open long  close short
                        self.makeOrder(context,inst, posinfo,'open','long',abs(vol))
                        self.makeOrder(context,inst, posinfo,'close','short',abs(pos))
                '''        
                self.destpos[inst]['status'] = 'executed'  
            
def algo_trade(context,instid,direction,price,volume,exec_seconds, random_factor=0, ordertype='market', action='open', algo='twap',timecond='GFD', accid=-1):
    '''
    
    Parameters
    ----------
    context : object
        DESCRIPTION.
    instid : str
        DESCRIPTION.
    direction : int
        DESCRIPTION.
    price : float
        DESCRIPTION.
    volume : int
        DESCRIPTION.
    exec_seconds : int
        DESCRIPTION.
    random_factor : int, optional
        DESCRIPTION. The default is 0.
    ordertype : str, optional
        DESCRIPTION. The default is 'market'.
    action : str, optional
        DESCRIPTION. The default is 'open'.
    algo : str, optional
        DESCRIPTION. The default is 'twap'.

    Returns
    -------
    None.

    '''
    validtypes = ['limit', 'market']
    validaction = ['open', 'close']  # ['auto','open','close']
    try:
        direction = int(direction)
        volume = int(volume)
    except Exception as e:
        logger.warning("volume/direction must be digits." + str(direction) + '/' + str(volume), e)
        return -1
    if not ordertype in validtypes:
        logger.warning("ordettype must be one of " + str(validtypes) + ",your ordertype:" + str(ordertype))
        return -1
    if not action in validaction:
        logger.warning("action must be one of " + str(validaction) + ',your action:' + str(action))
        return -1

    if direction == 0:
        logger.warning("Direction can not be zero. your direction: " + str(direction))
        return -1
    
    if ordertype =='market' and price == 0:
        price = context.getCurrent(instid)
    
    if volume <= 0 or price <= 0:
        logger.warning("price and volume must be positive . current price:" + str(price) + ',volume:' + str(volume))
        return -1
    
    if not isinstance(exec_seconds, int) or exec_seconds <= 0:
        logger.warning("exec_seconds must larger than 1")
        return -1
    
    maxmarg = context.getMargin(price,direction >0, volume,instid)
    accid = getInstAccID(instid)[0] if accid < 0 else accid
    if accid >= len(context.accounts):
        accid = len(context.accounts)-1
    if action =='open' and context.account.avail <= maxmarg:
        logger.warning("算法交易开仓不可执行，因总可用权益不足")
        return -2
    
    if action =='close':
        dirstr = 'long' if direction < 0 else 'short'
        pos = context.getAccountPosition(instid, dirstr,'volume')
        pend = context.account.calcFrozenVol(instid, direction) 
        if volume > pos - pend:
            logger.warning("算法交易平仓不可执行，因持仓不足")
            return -2
    
    if instid in context.algoorders:
        for oid in context.algoorders[instid]['orderids']:
            if context.orders[oid]['leftvol'] > 0:
                cancel_order(context, oid)
    
    freq = int(exec_seconds / volume)
    freq = max(freq, 2)
    basevol = freq * volume / exec_seconds
    if ordertype =='market':
        tradevol = round(basevol * (1 + random.randint(-random_factor, random_factor)/100)) 
        tradevol = max(tradevol, 1)
        limitcount = 0
        limitleft = 0
    else:
        tradevol = round(basevol)
        limitcount = int(volume / tradevol)
        limitleft = volume - limitcount * tradevol
        #limitleft = volume - tradevol * exec_seconds/freq 
    
    starttime = datetime.now()
    endtime =  starttime + timedelta(seconds=exec_seconds)   
    if tradevol > volume:
        tradevol = volume
    ret, oids = make_order(context, instid, direction, price, tradevol,ordertype, action,timecond=timecond, accid=accid)    
    if ret == 0:
        #context.algoid += 1
        context.algoorders[instid] = {'starttime':starttime,
                                              'inittime':starttime,
                                              'endtime':endtime,
                                              'instid':instid,
                                              'direction':direction,
                                              'price':price,
                                              'volume':volume,
                                              'leftvol':volume,
                                              'factor': random_factor,
                                              'ordertype':ordertype,
                                              'action': action,
                                              'freq': freq,
                                              'basevol': round(basevol),
                                              'limitcount': limitcount,
                                              'limitleft': limitleft,
                                              'algo':algo,
                                              'timecond':timecond,
                                              'accid' : accid,
                                              'orderids':oids}
    return 0            
            
        
        
        
    

        
        
