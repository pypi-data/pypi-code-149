# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:42:35 2022

@author: ScottStation
"""
import json
import mysql.connector
#import traceback
from .qelogger import logger
import pandas as pd
import numpy  as np
from datetime import datetime,timedelta
from .qeglobal import dbconfig
dbip = '192.168.123.13' if dbconfig['ip'] != '103.36.172.183' else dbconfig['ip']
dbport = 58003
carduser="amber"
cardpass='amber@cjfco'

from functools import wraps
def convert_stratname(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        nargs = list(args)
        nargs[0] = convert_strat_name(nargs[0])
        nargs= tuple(nargs)
        return func(*nargs, **kwargs)
    return _wrapper
def convert_strat_name(name):
    return name.upper().replace('-','_').replace('.','_')
    
def getPosVal(position, instid, dirstr, field):
    if instid in position:
        if dirstr in position[instid]:
            if field in position[instid][dirstr]:
                return position[instid][dirstr][field]
    return 0

@convert_stratname    
def writeStratPosition(strat_name, date, position, instClosePnl):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_position',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {strat_name} (date char(10), prod char(10), instid char(32),\
                            longpos int default 0, shortpos int default 0, longypos int default 0, \
                            shortypos int default 0, longcost float default 0, shortcost float default 0,\
                            closepnl float default 0,updatetime timestamp not NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP, primary key (date, prod, instid))')
        sql = f'replace into {strat_name} (date, prod, instid, longpos, shortpos, longypos, shortypos,longcost, shortcost, closepnl) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        vallist = []
        for inst in position:
            prod = inst[:1] if inst[1].isdigit() else inst[:2]
            closepnl = instClosePnl[inst] if inst in instClosePnl else 0
            val = (date, prod, inst, getPosVal(position,inst,'long','volume'), getPosVal(position,inst,'short','volume'),\
                   getPosVal(position,inst,'long','yesvol'), getPosVal(position,inst,'short','yesvol'), \
                   getPosVal(position,inst,'long','poscost'), getPosVal(position,inst, 'short','poscost'), closepnl)
            vallist.append(val)
        for inst in instClosePnl:
            if not inst in position:
                prod = inst[:1] if inst[1].isdigit() else inst[:2]
                closepnl = instClosePnl[inst]
                val = (date, prod, inst, 0,0,0,0,0,0, closepnl)
                vallist.append(val)
                
        cursor.executemany(sql,vallist)
        
        
        
        mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
    finally:    
        mydb.close()

@convert_stratname     
def readStratPosition(strat_name, date, prod=None):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_position',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        if prod and isinstance(prod, str):
            cursor.execute(f'select * from {strat_name} where date ="{date}" and prod ="{prod}"')
        else:    
            cursor.execute(f'select * from {strat_name} where date ="{date}"')
        res = cursor.fetchall()
        #print(res)
        position = {}
        instClosePnl = {}
        for r in res:
            inst = r[2] 
            
            position[inst]={'long':{'volume':r[3],'yesvol':r[5], 'poscost':r[7]},'short':{'volume':r[4],'yesvol':r[6], 'poscost':r[8]}}
            instClosePnl[inst] = r[9]
        #print(position)
        #print(instClosePnl)
        mydb.close()
        return position, instClosePnl
    except Exception as e:
        mydb.close()
        #traceback.print_exc()
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
        return {}, {}

@convert_stratname
def clearStratTrades(strat_name, fromdate=None):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_trades',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        if fromdate is None:
            cursor.execute(f'delete from `{strat_name}`')
        else:
            cursor.execute(f"delete from `{strat_name}` where date > '{fromdate.strftime('%Y%m%d')}' ")
        mydb.commit()
        mydb.close()
        #print(strat_name)
    except Exception as e:
        if mydb:
            mydb.close()
        #logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}")

@convert_stratname
def clearStratStat(strat_name, fromdate=None):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_stat',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        if fromdate is None:
            cursor.execute(f'delete from `{strat_name}`')
        else:
            cursor.execute(f"delete from `{strat_name}` where date > '{fromdate.strftime('%Y%m%d')}' ")
        mydb.commit()
        mydb.close()
        #print(strat_name)
    except Exception as e:
        if mydb:
            mydb.close()
        
def clearStratPosition(strat_name, fromdate=None):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_position',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        if fromdate is None:
            cursor.execute(f'delete from `{strat_name}`')
        else:
            cursor.execute(f"delete from `{strat_name}` where date > '{fromdate.strftime('%Y%m%d')}' ")
        mydb.commit()
        mydb.close()
        #print(strat_name)
    except Exception as e:
        if mydb:
            mydb.close()        #traceback.print_exc()

#======trades
@convert_stratname
def save_trades(stratName,trade, date):
    transdate = lambda date : date[:4]+'-'+date[4:6] +'-'+date[6:] if not '-' in date else date
    try:
        mydb = mysql.connector.connect(            
            port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_trades',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        vallist = []
        #print(len(statistic))
        for i in range(len(trade)):
            #print(i)
            #date = str(trade['date'].iloc[i])
            prod = str(trade['prod'].iloc[i])
            tradeid = str(trade['tradeid'].iloc[i])
            timestr = str(trade['time'].iloc[i])
            instid = str(trade['instid'].iloc[i])
            direction= str(trade['dir'].iloc[i])#long/short
            action = str(trade['action'].iloc[i])#open/close
            price = float(trade['price'].iloc[i])
            volume = int(trade['vol'].iloc[i])
            curdate = str(trade['date'].iloc[i])
            context =(transdate(curdate),prod,tradeid,timestr,instid,direction,action,price,volume)
            vallist.append(context)
        cursor.execute(f'create table if not exists {stratName} (date char(10), prod char(10),tradeid char(15),\
        timestr char(20),instid char(32),direction char(10),action char(10),price float default 0, volume int default 0,primary key(date,prod,tradeid))')
        sql_invert = f'replace into {stratName} (date,prod,tradeid,timestr,instid,direction,\
        action,price,volume)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.executemany(sql_invert, vallist)
        mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)

        # print('读取错误，原因是', e.__class__.__name__, e)  # continue#jia
    finally:
        mydb.close()
#save_trades(a,'10日移动平均')
        
    
#=======stat    
@convert_stratname
def save_stratStatistic(stratName,statistic):
    try:
        mydb = mysql.connector.connect(            
            port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_stat',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        vallist = []
        #print(len(statistic))
        for i in range(len(statistic)):
            #print(i)
            date = str(statistic['time'].iloc[i])
            prod = str(statistic['prod'].iloc[i])
            pnl = float(statistic['pnl'].iloc[i])
            maxmarg = float(statistic['maxmarg'].iloc[i])
            turnover = float(statistic['turnover'].iloc[i])
            context =(date,prod,pnl,maxmarg,turnover)
            vallist.append(context)
        cursor.execute(f'create table if not exists {stratName} (date char(20), prod char(15),pnl float default 0, maxmarg float default 0, turnover float default 0,primary key(date,prod))')
        sql_invert = f'replace into {stratName} (date,prod,pnl,maxmarg,turnover)values(%s,%s,%s,%s,%s)'
        cursor.executemany(sql_invert, vallist)
        mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)

        # print('读取错误，原因是', e.__class__.__name__, e)  # continue#jia
    finally:
        mydb.close()

@convert_stratname 
def writeStratStat(strat_name,date, posMaxMarg, posTurnover):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_stat',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        cursor.execute(f'create table if not exists {strat_name} (date char(20), prod char(15),pnl float default 0, maxmarg float default 0, turnover float default 0,primary key(date,prod))')
        sql = f'replace into {strat_name} (date, prod, maxmarg, turnover) values (%s,%s,%s,%s)'
        vallist = []
        for prod in posMaxMarg:
            turnover = posTurnover[prod] if prod in posTurnover else 0
            val = (date, prod, posMaxMarg[prod], turnover)
            vallist.append(val)
                
        cursor.executemany(sql,vallist)
        mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)

    finally:    
        mydb.close()

@convert_stratname 
def readStratStat(strat_name,date):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_stat',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        cursor.execute(f'select * from {strat_name} where date ="{date}"')
        res = cursor.fetchall()
        prodMaxMarg = {}
        prodTurnover = {}
        for r in res:
            prodMaxMarg[r[1]] = r[2]
            prodTurnover[r[1]] = r[3]
        mydb.close()    
        return prodMaxMarg, prodTurnover        
        
        
    except Exception as e:
        mydb.close()    
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
        #traceback.print_exc()
        return {},{}

@convert_stratname 
def readFullStratStat(strat_name, start_date=None, end_date=None):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_stat',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        #print(strat_name)
        if start_date:
            assert isinstance(start_date,str) and len(start_date) == 8, 'start_date must be like "20221010" format.'
        if end_date:
            assert isinstance(end_date,str) and len(end_date) == 8, 'end_date must be like "20221010" format.'
        if start_date and end_date:
            sql = f"select * from `{strat_name}` where date >= '{start_date}' and date <= '{end_date}'"
        elif start_date:
            sql = f"select * from `{strat_name}` where date >= '{start_date}'"
        elif end_date:
            sql = f"select * from `{strat_name}` where date <= '{end_date}'"
        else:
            sql = f"select * from `{strat_name}`"
        cursor.execute(sql)
        res = cursor.fetchall()
        mydb.close()
        if len(res)>0:
            df = pd.DataFrame(res)
            df.columns=['date','prod','pnl','maxmarg','turnover']
            return df
        else:
            return pd.DataFrame()
    except Exception as e:
        if mydb:
            mydb.close()    
        logger.error(f'Error on qestratmarket: {e.__traceback__.tb_lineno} {e}')


def getStratNetValues(strat_name, start_date, end_date):
    try:
        assert isinstance(start_date,str) and len(start_date) == 10, 'start_date must be like "2022-10-10" format.'
        assert isinstance(end_date,str) and len(end_date) == 10, 'end_date must be like "2022-10-10" format.'
        strat = readStratCard(strat_name,fields=['name','initcap'],portfolio=False)
        initcap = strat.loc[0,'initcap']
        df = readFullStratStat(strat_name, start_date.replace('-',''), end_date.replace('-',''))
        df = df.groupby('date').sum()
        df['netval'] = df['pnl'].cumsum()
        df['netval'] = [ 1+nv/initcap for nv in df['netval']]
        getFullDate = lambda x : x[:4]+'-'+x[4:6]+'-'+x[6:8]
        datelist = [getFullDate(d) for d in df.index]
        resdf = pd.DataFrame(index=datelist)
        resdf['netval'] = list(df['netval'])
        return resdf

    except Exception as e:
        logger.error(f'Error on qestratmarket: {e.__traceback__.tb_lineno} {e}')

@convert_stratname 
def writeStratPnl(strat_name,date,prod, pnl):
    #print('stratname',strat_name)
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_stat',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        cursor.execute(f'create table if not exists {strat_name} (date char(20), prod char(15),pnl float default 0, maxmarg float default 0, turnover float default 0,primary key(date,prod))')
        sql = f'update {strat_name}  set pnl ="{str(pnl)}"where date="{date}" and prod="{prod}"'
        cursor.execute(sql)
        mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
    finally:    
        mydb.close()        
        
@convert_stratname 
def writeStratTrade(strat_name, date, trade):
    transdate = lambda date : date[:4]+'-'+date[4:6] +'-'+date[6:] if not '-' in date else date
    def transtime(timestr):
        return timestr[:4]+'-'+timestr[4:6] +'-'+timestr[6:8] + ' ' + timestr[8:10] + ':' + timestr[10:12] +':'+ timestr[12:14]
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user='ls',
            password='Liusuang@2022',
            database='strat_trades',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        cursor.execute(f'create table if not exists {strat_name} (date char(10), prod char(10),tradeid char(15),\
        timestr char(20),instid char(32),direction char(10),action char(10),price float default 0, volume int default 0,primary key(date,prod,tradeid))')
        sql = f'replace into {strat_name} (date,prod,tradeid,timestr,instid,direction,\
        action,price,volume)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        #vallist = []
        tradeid = str(trade['tradeid'])
        timestr = transtime(str(trade['timedigit']))
        instid = str(trade['instid'])
        prod =  instid[:1] if instid[1].isdigit() else instid[:2]
        direction = 'long' if int(trade['dir']) > 0 else 'short'#long/short
        action = str(trade['action'])#open/close
        price = float(trade['tradeprice'])
        volume = int(trade['tradevol'])
        context =(transdate(date),prod,tradeid,timestr,instid,direction,action,price,volume)
        cursor.execute(sql,context)
        mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
    finally:    
        mydb.close()
   

def readStratCard(strat_name=None, fields = None, portfolio = True):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user=carduser,
            password=cardpass,
            database='strat_cards',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        if fields:
            assert isinstance(fields,list),'fields必须是list'
        spec_field = ','.join(fields) if fields else '*' 
        if strat_name:
            sql = f'select {spec_field} from strats where name ="{strat_name}"'if portfolio else f'select {spec_field} from strats where name ="{strat_name}" and type="origin"'
        else:
            sql = f'select {spec_field} from strats' if portfolio else f'select {spec_field} from strats where type="origin"'
        
        #print(sql)
        cursor.execute(sql)
        
        res = cursor.fetchall()
        mydb.close()
        if res and len(res) > 0:
            res = pd.DataFrame(res)
            if fields:
                res.columns = fields
            else:
                res.columns=['name', 'type', 'price', 'investorName', 'AnnualReturn','MaxDrawdown', 'NetValue', \
                             'RecentReturns', 'Introduction', 'RiskLevel', 'maxMarg', 'portfolioProfile',\
                                 'cloneProfile', 'prods', 'template','AnnualVol','MaxLoss','curpirce','preprice','initcap']
            return res
        else:
            return None
    except Exception as e:
        logger.error(f'Error on readStratCard: {e.__traceback__.tb_lineno} {e}')
        if mydb:
            mydb.close()

def batchReadStratCards(strat_names, fields):
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user=carduser,
            password=cardpass,
            database='strat_cards',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        assert isinstance(fields, list) and isinstance(strat_names, list),'strat_names/fields 必须是list'
        spec_field = ','.join(fields) 
        
        if len(strat_names) > 1:
             strat_names = tuple(strat_names)
             sql = f'select {spec_field} from strats where name in {strat_names}'
        else:
            sql = f"select {spec_field} from strats where name ='{strat_names[0]}'"
        #print(sql)
        cursor.execute(sql)
        
        res = cursor.fetchall()
        mydb.close()
        if len(res) > 0:
            res = pd.DataFrame(res)
            res.columns = fields
            return res
    except Exception as e:
        logger.error(f'Error on smStrats: {e.__traceback__.tb_lineno} {e}')
        if mydb:
            mydb.close()

#@convert_stratname        
def update_stratCard(stratName, indicators, prodMaxmarg):
    try:
        mydb = mysql.connector.connect(            
            port=dbport,
            host=dbip,
            user=carduser,
            password=cardpass,
            database='strat_cards',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        stratname = stratName
        #print(indicators)
        annualreturn = indicators['annualret']
        maxdrawdown = indicators['maxdrawdown']
        recentreturn = indicators['retayear']
        netvalue = indicators['netval']
        maxmarg = prodMaxmarg#indicators['maxmarg']
        annualvol = indicators['annualvol']
        maxloss = indicators['maxloss']
        initcap = sum(prodMaxmarg.values()) + maxloss
        sql_update = f"update strats set AnnualReturn = '{str(annualreturn)}',MaxDrawdown ='{str(maxdrawdown)}',\
        RecentReturns = '{str(recentreturn)}',NetValue = '{str(netvalue)}',maxMarg ='{json.dumps(maxmarg)}', \
        AnnualVol = '{str(annualvol)}', MaxLoss = '{str(maxloss)}' , initcap = '{str(initcap)}' where name ='{str(stratname)}'"
        cursor.execute(sql_update)
        mydb.commit()
        print('update stratgy card data sucessfully')
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
        # print('读取错误，原因是', e.__class__.__name__, e)  # continue#jia
    finally:
        mydb.close()

def getIndicators(df, maxloss):
    try:
        ## before groupby , calculate margins
        #prods = set(df['prod'])
        df = df.groupby(['date']).sum()
        #print(df)
        #df.index = df['date']
        initbal = max(df['maxmarg']) + maxloss 
        df['balance'] = df['pnl'].cumsum() + initbal
        df['logret'] = np.log(df['balance'].astype('float')) - np.log(df['balance'].shift(1).fillna(initbal).astype('float'))
        df['netval'] = df['balance']/initbal
        df['highwater'] = df['balance'].cummax()
        df['drawdown'] = 1 - df['balance'] / df['highwater']
        annual_days = 250
        indicators = {}
        indicators['annualret'] = round(sum(df['logret']) *annual_days / len(df), 4)
        indicators['retayear'] = round(sum(df.loc[df.index[-annual_days:], 'logret']),4)
        indicators['annualvol'] = round(df['logret'].std() * np.sqrt(annual_days),4)
        indicators['maxdrawdown'] = round(max(max(df['drawdown']),0),4)
        indicators['netval'] = round(df.loc[df.index[-1],'netval'],2)
        indicators['maxloss'] = maxloss
        return indicators   
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
        
        
        
def update_stratCard_append(stratName, initloss):
    card = readStratCard(stratName, ['name','MaxLoss'])
    maxloss = card.loc[card.index[0],'MaxLoss']
    maxloss = max(maxloss, abs(initloss))
    df = readFullStratStat(stratName)
    if df is None or len(df) == 0:
        return None
    indicators = getIndicators(df,maxloss)
    mm = df.groupby(['prod']).max()
    prodMaxMarg = {p : mm.loc[p,'maxmarg'] for p in mm.index}
    update_stratCard(stratName, indicators, prodMaxMarg)
        
    


## By Amber
def writeContract_messages(strat_name, date, trade):
    try:
        mydb = mysql.connector.connect(port=dbport,
                                       host=dbip,
                                       user="amber",
                                       passwd='amber@cjfco',
                                       db='market_select',
                                       charset='utf8',
                                       use_unicode=True)
        cursor = mydb.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS ContractName_messages(\
                                  time timestamp not NULL default CURRENT_TIMESTAMP,\
                                  instid char(32),\
                                  strategyname char(32) ,\
                                  openorclose char(10),\
                                  longorshort char(10),\
                                  volume int,\
                                  price float,\
                                  id int auto_increment,\
                                  PRIMARY KEY (id))')
        #timestr = str(trade['timedigit'])
        instid = str(trade['instid'])
        direction = str(trade['dir'])#long/short
        action = str(trade['action'])#open/close
        price = float(trade['tradeprice'])
        volume = int(trade['tradevol'])

        sql = f'insert into ContractName_messages(instid, strategyname, openorclose,longorshort,volume,price) values (%s,%s,%s,%s,%s,%s)'
        val = (instid, strat_name, action, direction, volume, price)
        cursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
    finally:
        mydb.close()

def writeStratCard( strat_name, investor_name, introduction, clone_price, 
                  risk_level, prods, template="null", strat_type='origin',  portfolio_sett={}, clone_sett={}):
    '''
    '''
    #if template != 'null':
    #    if not addTemplateInstance(template, prods, strat_name ):
    #        return False
    try:
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user=carduser,
            password=cardpass,
            database='strat_cards',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS strats (name char(32) PRIMARY KEY, type char(15),\
                         price text, InvestorName char(20), AnnualReturn float default 0,MaxDrawdown float(16) default 0,\
                         NetValue float(16) default 0, RecentReturns float default 0,Introduction VARCHAR(256), \
                         RiskLevel int(10),maxMarg JSON, portfolioProfile JSON, cloneProfile JSON,prods text, \
                         template char(32),AnnualVol float default 0,MaxLoss float default 0, \
                         curpirce int default 100, preprice int default 150, initcap float default 0)')
        sql = f'replace into strats (name, price, type, curprice, preprice, Introduction, investorName, RiskLevel, portfolioProfile, cloneProfile, maxMarg,prods, template) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        pricedict = clone_price #json.dumps(clone_price)
        curprice = pricedict['monthly']
        preprice = pricedict['monthly before']
        
        val = (strat_name, json.dumps(clone_price), strat_type,curprice, preprice, introduction,investor_name, int(risk_level), json.dumps(portfolio_sett),json.dumps(clone_sett),'{}',json.dumps(prods), template)
        cursor.execute(sql,val)
        mydb.commit()
        mydb.close()
        return True
        
    except Exception as e:
        logger.error(f'Error on writeStratCard: {e.__traceback__.tb_lineno} {e}')
        if mydb :    
            mydb.close()
        return False    
   

def writeContractTable(stratname, date, position):
    try:
        mydb = mysql.connector.connect(port=dbport,
                                       host=dbip,
                                       user="amber",
                                       passwd='amber@cjfco',
                                       db='market_select',
                                       charset='utf8',
                                       use_unicode=True)

        cursor = mydb.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS ContractTables ( \
                                  datetime timestamp not NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,\
                                  instid char(32),\
                                  longstrats JSON,\
                                  shortstrats JSON,\
                                  netposition int,\
                                  PRIMARY KEY (instid))')
        #cursor.execute(f'CREATE TABLE IF NOT EXISTS ContractTables (date char (18),\
        #                          instid char(32),\
        #                          stratname char(32) ,\
        #                          netposition int,\
        #                          PRIMARY KEY (instid, stratname))')
        
        instlist = list(position.keys())
        if len(instlist) > 0:
            #inststr = ",".join(instlist)
            if len(instlist) == 1:
                sql = f"select instid, longstrats, shortstrats, netposition from ContractTables where instid ='{instlist[0]}'"
            else:
                sql = f"select instid, longstrats, shortstrats, netposition from ContractTables where instid in {tuple(instlist)}"
            cursor.execute(sql)
            res = cursor.fetchall()
            instdict = {}
            if res and len(res) > 0:
                for r in res:
                    #print('ContractTables',r)
                    try:
                        longs = set(json.loads(r[1])) 
                        shorts = set(json.loads(r[2])) 
                    except:
                        longs = set()
                        shorts = set()
                    instdict[r[0]] = {'longs':longs, 'shorts':shorts, 'netpos':int(r[3])}
            sql = f'replace into ContractTables (instid, longstrats, shortstrats, netposition) values (%s,%s,%s,%s)'
            vallist = []
            for inst in position:
                if not inst in instdict:
                    instdict[inst] = {'longs':set(), 'shorts':set(),'netpos':0}
                netposition =  getPosVal(position, inst, 'long', 'volume') - getPosVal(position, inst, 'short', 'volume') 
                if netposition > 0:
                    instdict[inst]['longs'].add(stratname)
                elif netposition < 0:
                    instdict[inst]['shorts'].add(stratname)
                else:
                    instdict[inst]['shorts'].discard(stratname)
                    instdict[inst]['longs'].discard(stratname)
                instdict[inst]['netpos'] = len(instdict[inst]['longs']) - len(instdict[inst]['shorts'])
                val = (inst, json.dumps(list(instdict[inst]['longs']),ensure_ascii=False), json.dumps(list(instdict[inst]['shorts']),ensure_ascii=False),instdict[inst]['netpos'])
                vallist.append(val)
            cursor.executemany(sql, vallist)
            mydb.commit()
    except Exception as e:
        logger.error(f"qestratmarket {e.__traceback__.tb_lineno},{e}",exc_info=True)
    finally:
        mydb.close()


def listStratCards(sfilter = 'AnnualReturn', begin=0, maxnum=16):
    try:
        assert sfilter in ['AnnualReturn', 'SharpeRatio', 'CalmarRatio'], '不合法的filter'
        mydb = mysql.connector.connect(port=dbport,
            host=dbip,
            user=carduser,
            password=cardpass,
            database='strat_cards',
            use_unicode=True,
            charset='utf8')
        cursor = mydb.cursor()
        sel_columns= ['name', 'NetValue','AnnualReturn', 'MaxDrawdown','AnnualVol','initcap']
        spec_field = ','.join(sel_columns)
        condition= "where type='origin'"  
        if sfilter == 'SharpeRatio':
            sql = f"select {spec_field}, (AnnualReturn/AnnualVol) as sharpeRatio from strats {condition} order by sharpeRatio desc limit {begin},{maxnum}"      
            sel_columns.append('SharpeRatio')
        elif sfilter == 'CalmarRatio':
            sql = f"select {spec_field}, (AnnualReturn/MaxDrawdown) as calmarRatio from strats {condition} order by calmarRatio desc limit {begin},{maxnum}"            
            sel_columns.append('CalmarRatio')
        else:
            sql = f"select {spec_field} as calmarRatio from strats {condition} order by AnnualReturn desc limit {begin},{maxnum}"            
        
        cursor.execute(sql)
        res = cursor.fetchall()
        df = pd.DataFrame()
        if res and len(res) > 0:
            df = pd.DataFrame(res)
            df.columns = sel_columns
            
        mydb.close()
        return df
    except Exception as e:
        logger.error(f'Error on smStrats: {e.__traceback__.tb_lineno} {e}')
        if mydb:
            mydb.close()

