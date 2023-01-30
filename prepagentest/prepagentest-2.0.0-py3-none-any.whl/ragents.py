#!/usr/bin/env python3
import time
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm
from helperagent import Helper
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import multiprocessing

# More ML Models
import xgboost as xgb
import xgboost
import sklearn
import statsmodels
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from interpret.glassbox.ebm.ebm import ExplainableBoostingClassifier
import shap as shap

###################################################################################################
# preparation agent ###############################################################################
###################################################################################################
class Preparation_Agent:
#installing dependencies
    import pandas as pd
    #uploading data and simple data wrangling
    def __init__(self, dbfile, shiftable_devices):
        from helperagent import Helper
        helper = Helper()
        self.input = helper.export_sql(dbfile)
        self.shiftable_devices = shiftable_devices

    def unpacking_attributes(self, df):
        import pandas as pd
        output = df.copy()
        output['shared_attributes']=output['shared_attributes'].apply(lambda x: x.replace('true','True'))
        output['shared_attributes']=output['shared_attributes'].apply(lambda x: x.replace('false','False'))
        output['shared_attributes']=output['shared_attributes'].apply(lambda x: x.replace('null','None'))

        output['shared_attributes']=output['shared_attributes'].apply(lambda dat: dict(eval(dat)))
        df2 = pd.json_normalize(output['shared_attributes'])
        result = pd.DataFrame( pd.concat([output,df2], axis = 1).drop('shared_attributes', axis = 1))
        result = result.dropna(axis = 1, thresh=int(0.95*(len(result.columns))))
        return result

    def access_shiftable_devices(self, df, attrs= 'all'):
        import pandas as pd
        trial = df.copy()
        trial.attributes_id = trial.attributes_id.dropna()
        trial.state= pd.to_numeric(trial['state'], errors='coerce').dropna()
        if attrs == 'all':
            w_data = trial[trial.unit_of_measurement.isin(['W'])]
            w_data = trial[trial.entity_id.isin(self.shiftable_devices)]
            w_data_long = w_data[['entity_id','last_updated','state']]
            w_data_wide = pd.pivot(w_data_long,  index = ['last_updated'], columns = 'entity_id', values = 'state')
        if attrs != 'all':
            w_data = trial[trial.unit_of_measurement.isin(['W']) & trial.attributes_id.isin([attrs])]
            w_data = trial[trial.entity_id.isin(self.shiftable_devices)]
            w_data_long = w_data[['entity_id','last_updated','state']]
            w_data_wide = pd.pivot(w_data_long,  index = ['last_updated'], columns = 'entity_id', values = 'state')
        result = w_data_wide.fillna(0).reset_index()
        return(result)
    
    #basic preprocessing
    # -------------------------------------------------------------------------------------------
    def outlier_truncation(self, series, factor=1.5, verbose=0):
        from tqdm import tqdm
        
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3-q1
        
        lower_bound = q1 - factor*iqr
        upper_bound = q3 + factor*iqr
        
        output = []
        counter = 0
        for item in (tqdm(series, desc=f'[outlier truncation: {series.name}]') if verbose != 0 else series):
            if item > upper_bound:
                output.append(int(upper_bound))
                counter += 1
            elif item < lower_bound:
                output.append(int(lower_bound))
                counter += 1
            else:
                output.append(item)
        print(f'[outlier truncation: {series.name}]: {counter} outliers were truncated.') if verbose != 0 else None 
        return output
    
    def scale(self, df, features='all', kind='MinMax', verbose=0):
        output = df.copy()
        features = output.select_dtypes(include=['int', 'float']).columns if features == 'all' else features

        if kind == 'MinMax':
            from sklearn.preprocessing import MinMaxScaler
            
            scaler = MinMaxScaler()
            output[features] = scaler.fit_transform(output[features])
            print('[MinMaxScaler] Finished scaling the data.') if verbose != 0 else None
        else:
            raise InputError('Chosen scaling method is not available.')
        return output 

    def get_timespan(self, df, start, timedelta_params):
        df.last_updated = pd.to_datetime(df.last_updated)
        df = df.set_index('last_updated')
        start = pd.to_datetime(start) if type(start) != type(pd.to_datetime('1970-01-01')) else start 
        end = start + pd.Timedelta(**timedelta_params)
        return df[start:end].reset_index()
    
    def truncate(self, df, features='all', factor=1.5, verbose=0):
        import time
        output = df.copy()
        features = df.select_dtypes(include=['int', 'float']).columns if features == 'all' else features

        for feature in features:
            time.sleep(0.2) if verbose != 0 else None
            row_nn = df[feature] != 0                                                                  # truncate only the values for which the device uses energy
            output.loc[row_nn, feature] = self.outlier_truncation(df.loc[row_nn, feature], factor=factor, verbose=verbose) # Truncatation factor = 1.5 * IQR
            print('\n') if verbose != 0 else None
        return output
    
    def last_reported(self, df):
        return str(df.index.max())[:10]
    
    def days_between(self, d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)

    
    def add_dummy_data_tomorrow(self, df):

        today = str(datetime.now())[:10]
        last_updated = self.last_reported(df)
        tomorrow = (pd.to_datetime(today) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
        diff_days = self.days_between(last_updated, today)
        # determine how many hours we need to fill up (missing hours till new day + 23 for tomorrow, day of prediction)
        hours_to_fill = 24 - int(str(df.index.max())[11:13]) + 23 + (24 * diff_days)

        # add rows and fill up with dummy 0
        for i in range(0,hours_to_fill):
            idx = df.tail(1).index[0] + pd.Timedelta(hours=1)
            df.loc[idx] = 0
        return df
    
    def plot_consumption(self, df, features='all', figsize='default', threshold=None, title='Consumption'):
        df = df.copy()
        features = [column for column in df.columns if column not in ['Unix', 'Issues']] if features == 'all' else features
        fig, ax = plt.subplots(figsize=figsize) if figsize != 'default' else plt.subplots()
        if threshold != None:
            df['threshold'] = [threshold]*df.shape[0]
            ax.plot(df['threshold'], color = 'tab:red')
        for feature in features:
            ax.plot(df[feature])
        ax.legend(['threshold'] + features) if threshold != None else ax.legend(features)
        ax.set_title(title);
    # feature creation
    # -------------------------------------------------------------------------------------------
    def get_device_usage(self, df, device, threshold):
        return (df.loc[:, device] > threshold).astype('int')

    def get_activity(self, df, active_appliances, threshold):
        import pandas as pd
        active = pd.DataFrame({appliance: df[appliance] > threshold for appliance in active_appliances})
        return active.apply(any, axis = 1).astype('int')

    def get_last_usage(self, series):
        import pandas as pd
        last_usage = []
        for idx in range(len(series)):
            shift = 1
            if pd.isna(series.shift(periods = 1)[idx]):
                shift = None
            else:
                while series.shift(periods = shift)[idx] == 0:
                    shift += 1
            last_usage.append(shift)
        return last_usage

    def get_last_usages(self, df, features):
        import pandas as pd

        output = pd.DataFrame()
        for feature in features:
            output['periods_since_last_'+str(feature)] = self.get_last_usage(df[feature])
        output.set_index(df.index, inplace=True)
        return output


    def get_time_feature(self, df, features='all'):
        import pandas as pd
        functions = {
            'hour': lambda df: df.index.hour, 
            'day_of_week': lambda df: df.index.dayofweek,
            'day_name': lambda df: df.index.day_name().astype('category'),
            'month': lambda df: df.index.month, 
            'month_name': lambda df: df.index.month_name().astype('category'),
            'weekend': lambda df: [int(x in ['Saturday', 'Sunday']) for x in  list(df.index.day_name())]
        }
        if features == 'all':
            output = pd.DataFrame({function[0]: function[1](df) for function in functions.items()})
        else:
            output = pd.DataFrame({function[0]: function[1](df) for function in functions.items() if function[0] in features})
        output.set_index(df.index, inplace=True)
        return output
    
    def get_time_lags(self, df, features, lags):
        import pandas as pd
        output = pd.DataFrame()
        for feature in features:
            for lag in lags:
                output[f'{feature}_lag_{lag}'] = df[feature].shift(periods=lag)
        return output

    #visualising threshold
    # ------------------------------------------------------------------------------------------- 
    def visualize_threshold(self, df, threshold, appliances, figsize=(18,5)):
        import pandas as pd
        # data prep
        for appliance in appliances:
            df[str(appliance) + '_usage'] = self.get_device_usage(df, appliance, threshold)
        df = df.join(self.get_time_feature(df))
        df['activity'] = self.get_activity(df, appliances, threshold)

        # plotting 
        import matplotlib.pyplot as plt

        usage_cols = [column for column in df.columns if str(column).endswith('_usage')]
        columns = ['activity'] + usage_cols

        fig, axes = plt.subplots(1,3, figsize=figsize)

        # hour
        hour = df.groupby('hour').mean()[columns]
        hour.plot(ax=axes[0])
        axes[0].set_ylim(-.1, 1.1);
        axes[0].set_title(f'[threshold: {round(threshold, 4)}] Activity ratio per hour')

        # week 
        usage_cols = [column for column in df.columns if str(column).endswith('_usage')]
        week = df.groupby('day_name').mean()[columns]
        week = week.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        week.plot(ax=axes[1])
        axes[1].set_ylim(-.1, 1.1);
        #axes[1].set_xticklabels(['']+list(week.index), rotation=90)
        axes[1].set_title(f'[threshold: {round(threshold, 4)}] Activity ratio per day of the week')

        # month
        usage_cols = [column for column in df.columns if str(column).endswith('_usage')]
        month = df.groupby('month').mean()[columns]
        month.plot(ax=axes[2])
        axes[2].set_ylim(-.1, 1.1);
        axes[2].set_title(f'[threshold: {round(threshold, 4)}] Activity ratio per month')
    def validate_thresholds(self, df, thresholds, appliances, figsize=(18,5)):

        for threshold in tqdm(thresholds):
            self.visualize_threshold(df, threshold, appliances, figsize)
        time.sleep(0.2)
        print('\n')
    
    #pipelines
    # -------------------------------------------------------------------------------------------
    #pipeline load
    def pipeline_load(self, df, params):
        from helperagent import Helper
        import pandas as pd
        helper = Helper()
        
        df  = self.unpacking_attributes(self.input)
        df = self.access_shiftable_devices(df)
        
        df = df.copy()
        output = pd.DataFrame()

        # Data cleaning
        # df = self.truncate(df, **params['truncate'],)
        # scaled = self.scale(df, **params['scale'])
        # ignore scaling for now, we would just scale those variables, which does not make sense 
        # Index(['state_id', 'old_state_id', 'attributes_id', 'origin_idx', 'hash'], dtype='object')
        scaled = df.copy()

        df['last_updated'] = pd.to_datetime(df['last_updated'])
        df = df.set_index('last_updated')

        scaled['last_updated'] = pd.to_datetime(scaled['last_updated'])
        scaled = scaled.set_index('last_updated')

        # aggregate
        df = helper.aggregate_load(df, **params['aggregate'])
        scaled = helper.aggregate_load(scaled, **params['aggregate'])
        
        # Add dummy data
        df = self.add_dummy_data_tomorrow(df)
        scaled = self.add_dummy_data_tomorrow(scaled)

        # Get device usage and transform to energy consumption
        for device in params['shiftable_devices']:
            df[str(device) + '_usage'] = self.get_device_usage(df, device, **params['device'])
            output[device] = df.apply(lambda timestamp: timestamp[device] * timestamp[str(device) + '_usage'], axis = 1)

        return output, scaled, df
    #pipeline usage
    def pipeline_usage(self, df, params):
        from helperagent import Helper
        import pandas as pd

        helper = Helper()

        df  = self.unpacking_attributes(self.input)
        df = self.access_shiftable_devices(df)
        
        df = df.copy()
        output = pd.DataFrame()

        # Data cleaning
        # df = self.truncate(df, **params['truncate'],)
        # scaled = self.scale(df, **params['scale'])
        # ignore scaling for now, we would just scale those variables, which does not make sense 
        # Index(['state_id', 'old_state_id', 'attributes_id', 'origin_idx', 'hash'], dtype='object')
        scaled = df.copy()
        
        # df['last_updated'] = pd.to_datetime(df['last_updated'])
        # df = df.set_index('last_updated')
        scaled['last_updated'] = pd.to_datetime(scaled['last_updated'])
        scaled = scaled.set_index('last_updated')
        
        # Aggregate to hour level
        scaled = helper.aggregate_load(scaled, **params['aggregate_hour'])
        
        # Add dummy data
        scaled = self.add_dummy_data_tomorrow(scaled)


        # Activity feature
        output['activity'] = self.get_activity(scaled, **params['activity'])

        # Get device usage and transform to energy consumption
        for device in params['shiftable_devices']:
            output[str(device) + '_usage'] = self.get_device_usage(scaled, device, **params['device'])

        # aggregate and convert from mean to binary
        output = helper.aggregate(output, **params['aggregate_day'])
        output = output.apply(lambda x: (x > 0).astype('int'))

        # Last usage
        output = output.join(self.get_last_usages(output, output.columns))
        
        # Time features
        output = output.join(self.get_time_feature(output, **params['time']))

        # lags
        output = output.join(self.get_time_lags(output, ['activity'] + [str(device)+'_usage' for device in params['shiftable_devices']], [1,2,3]))
        output['active_last_2_days'] = ((output.activity_lag_1 == 1) | (output.activity_lag_2 == 1)).astype('int')

        # dummy coding
        output = pd.get_dummies(output, drop_first=True)
        return output

    #pipeline activity
    def pipeline_activity(self, df, params):
        from helperagent import Helper
        import pandas as pd
        helper = Helper()
        df = df.copy()
        import pandas as pd
        output = pd.DataFrame()

        df  = self.unpacking_attributes(self.input)
        df = self.access_shiftable_devices(df)
        # Data cleaning
        # df = self.truncate(df, **params['truncate'],)
        # df = self.scale(df, **params['scale'])
        # ignore scaling for now, we would just scale those variables, which does not make sense 
        # Index(['state_id', 'old_state_id', 'attributes_id', 'origin_idx', 'hash'], dtype='object')

        df['last_updated'] = pd.to_datetime(df['last_updated'])
        df = df.set_index('last_updated')
        # Aggregate to hour level
        df = helper.aggregate_load(df, **params['aggregate'])
        
        # Add dummy data
        df = self.add_dummy_data_tomorrow(df)

        # Activity feature
        output['activity'] = self.get_activity(df, **params['activity'])
        
        ## Time feature
        output = output.join(self.get_time_feature(df, **params['time']))

        # Activity lags
        output = output.join(self.get_time_lags(output, **params['activity_lag']))

        # Dummy coding
        output = pd.get_dummies(output, drop_first=True)

        return output
