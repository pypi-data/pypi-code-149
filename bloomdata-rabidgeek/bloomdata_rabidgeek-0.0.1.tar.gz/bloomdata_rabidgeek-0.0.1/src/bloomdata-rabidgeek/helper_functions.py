import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split

# Part 2 Functions ==============================================================
'''
Part Two:
The exercise of writing these functions in part 2 is helpful practice in learning how to generate
random values. The data structures of having tuples inside of a list is one that we'll see multiple
times through Unit 3 so it's helpful to get familiar with it and also be able to stimulate our
own versions of lists of tuples with fake data in them. 
'''

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrases():
    adj = random.choice(adjectives)
    noun = random.sample(nouns, 1)[0]

    return adj + ' ' + noun

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def random_bowling_score():
    return random.randint(0, 300)

def silly_tuple():
    return (random_phrases(), random_float(1, 5), random_bowling_score())

def silly_tuple_list(num_tuples):
    tuple_list = []
    for item in range(num_tuples):
        tuple_list.append(silly_tuple())

    return tuple_list

# Part 3 Functions ==============================================================
'''
Part Three
Part 3 is practice in writing functions that might be truly useful withina published 
python package. we're writing fucntions that we could theoretically import into other
projects to help us do our work. 

Remmy - it's only required that you implement 1 of the functions from part 3. 
It's better to do 'em all. 
PRACTICE, my goodman!
'''

test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
null_df = pd.DataFrame(np.array([[None,2,3],[4,None,6],[None,8,None]]))

# Check a dataframe for nulls and return the number of missing values.
def null_count(df):
  return df.isna().sum().sum()

# Create a Train/Test split function for a dataframe and returns both the 
# Training and Testing sets. Frac referes to the precent of data you would 
# like to set aside for training.
def train_test_split(df, frac=.8):
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test

#Develop a randomization function that randomizes all of a dataframes cells 
# then returns that randomized dataframe. This function should also take a 
# random seed for reproducible randomization.
def randomize(df, seed):
    randomized_df = df.sample(frac=1.0, random_state=seed)
    return randomized_df

# Split addresses into three columns (df['city'], df['state'], and df['zip']) - 
# you can use regex to detect the format and pull out important pieces.
address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
                                       '8394 Kim Meadow\nDarrenville, AK 27389',
                                       '379 Cain Plaza\nJosephburgh, WY 06332',
                                       '5303 Tina Hill\nAudreychester, VA 97036']})

def addy_split(addy_series):
    df = pd.DataFrame()
    city_list = []
    state_list = []
    zip_list = []

    for addy in addy_series:
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[-2]
        zip = second_half.split()[-1]
        
        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip)

    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list

    return df

# Return a new column with the full name from a State abbreviation column. An input 
# of FL would return Florida. This function should also take a boolean (abbr_2_state) 
# and when False takes full state names and return state abbreviations. An input of 
# Florida would return Fl.
def abbr_2_st(state_series, abbr_2_st=True):
    state_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    def abbrev_replace(abbrev):
        return state_dict[abbrev]
    
    def state_replace(state_name):
        reverse_state_dict = dict((v,k) for k,v in state_dict.items())
        return reverse_state_dict[state_name]

    if abbr_2_st:
        return state_series.apply(abbrev_replace)
    else:
        return state_series.apply(state_replace)
    
addy_states = addy_split(address_df['address'])['state']

full_state_name_column = abbr_2_st(addy_states)

# Single function to take a list and dataframe then turn the list into a series 
# and add it to the inputted dataframe as a new column.
def list_2_series(list_2_series, df):
    new_column = pd.Series(list_2_series)
    return pd.concat([df, new_column], axis=1)

outliers = pd.DataFrame(
    {'a': [1,2,3,4,5,6],
     'b': [4,5,6,7,8,9],
     'c': [7,1000,9,10,11,12]}
)

# A 1.5*Interquartile range outlier detection/removal function that gets rid of 
# outlying rows and returns that outlier cleaned dataframe.
def rm_outliers(df):
    cleaned_df = pd.DataFrame()
    
    for (columnName, columnData) in df.iteritems():
        Q1 = columnData.quantile(.25)
        Q3 = columnData.quantile(.75)
        IRQ = Q3 - Q1
        lower_bound = Q1 - 1.5*IRQ
        upper_bound = Q3 + 1.5*IRQ 
        mask = columnData.between(lower_bound, upper_bound, inclusive='both')
        cleaned = columnData.loc[mask]

        cleaned_df[columnName] = cleaned
        
    return cleaned_df 

# Function to split dates of format "MM/DD/YYYY" into multiple columns (df['month'], df['day'], 
# df['year']) and then return the same dataframe with those additional columns.
def split_dates(date_series):
    df = pd.DataFrame()
    month_list = []
    day_list = []
    year_list = []

    for date in date_series:
        month_list.append(date.split('/')[0])
        day_list.append(date.split('/')[1])
        year_list.append(date.split('/')[2])
    
    df['month'] = month_list
    df['day'] = day_list
    df['year'] = year_list

    return df