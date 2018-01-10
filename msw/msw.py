# -*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import yaml

# Load surf spot data
df_spots = pd.read_csv('../data/surfspots.csv',
                       sep=',', 
                       usecols=['spot','spot_id'])
# Load Personal api key
api_key = yaml.load(open('./api_key.yml'))['api_key']

# Other necessary variables
# api url stub
url = 'http://magicseaweed.com/api/'
# fields to parse
fields = ['timestamp','fadedRating','solidRating','wind.direction',
          'wind.speed','swell.maxBreakingHeight',
          'swell.components.combined.period']

# Define functions
def fieldsToUrl(fields : list):
    """
    Returns a string that can be used to query specific fields in MSW api.
    
    Parameters
    --------
    fields : list of fields, list
    
    Returns
    --------
    , str
    """
    return '&fields=' + ','.join(fields)

fields = fieldsToUrl(fields)

def targetUrl(spot_id : str, fields=None):
    """
    Returns a target url consisting of msw url, personal api key, spot id and if
    specified some specified fields
    
    Parameters
    --------
    surf_spot : Name of surf spot, str
    fields : url string of fields to be parsed when scraping the msw api, str
    
    Returns
    --------
    target : url of api, str
    """
    target = url + str(api_key) + '/forecast/?spot_id=' + str(spot_id) + fields
                
    return target

def dictToSeries(df : pd.DataFrame, column : str):
    # Convert those columns with dictionaries in each row to pd.Series
    df = pd.concat([df, df[column].apply(pd.Series)], axis=1)
    df = df.drop(column, axis=1)
    
    return df

def parsePeriod(df : pd.DataFrame, column : str):
    # Extract Period swell from column
    df[column] = df[column].apply(pd.Series)
    df[column] = df[column].apply(pd.Series)
    # Rename colum to period
    df= df.rename(columns={column:'period'})
    
    return df

def processJson(target_url : str, spot_name : str):
    """
    Returns pandas DataFrame as read of json in MSW api with 2 new columns 
    (spot & weekday). DataFrame limited to "good" surf only and days defined 
    in msw_config.
    
    Parameters
    --------
    target_url : the api target, str
    spot_name : name of surf spot
    
    Returns
    --------
    df : DataFrame with fields specified in targetUrl, pd.DataFrame
    """
    # pd DataFrame from json
    df = pd.read_json(target_url)
    # Report dates in DataFrame
    print('dates:',df.timestamp.dt.date.min(),'to',df.timestamp.dt.date.max())
    # Convert wind and swell cols from dictionaries to pd.Series
    df = dictToSeries(df=df, column='wind')
    df = dictToSeries(df=df, column='swell')
    # Parse Period info
    df = parsePeriod(df=df, column='components')
    # Column with spot name
    df['spot'] = spot_name
    # Day name from timestamp
    df['weekday'] = df.timestamp.dt.weekday_name
    # Select only days with a "good" swell
    #df = df[(df.solidRating >= 3)]
    # Row with value equal to datetime now
    df['now'] = dt.datetime.now()
    # Calculate timedelta between now and forecasted date
    df['delta'] = (df['timestamp'] - df['now'])
    # Only positive deltas
    df = df[df['delta'] >= pd.Timedelta(0)]
    # Drop duplicates keeping only the very next forecast only
    df = df.drop_duplicates(subset='spot')
            
    # Reset index
    df = df.reset_index(drop=True)
    
    return df

def scrapeSurfSpots(fields=fields):
    """
    loops through surf_spots and scrapes each json table from its respective 
    api using processJson() and returns a DataFrame with all json tables concatenated.
    Parameters
    --------
    surf_spots : dictionary of surf spots. Key being the spot name and value being 
                 the unique spot identifier.
    fields : see targetUrl()
    
    Returns
    --------
    df : DataFrame containing all relevant surf forecasts for each spot in
         surf_spots, pd.DataFrame
    """
    # Create empty DataFrame
    df = pd.DataFrame([])
    # Retrieve data for each surf spot from msw api
    for idx, row in df_spots.iterrows():
        # Create target api url
        target = targetUrl(spot_id=row['spot_id'], fields=fields)
        print('\nGetting forecast info for', row['spot'])
        # Access MSW API
        df = pd.concat([df, processJson(target_url=target, spot_name=row['spot'])])
        # Reset Index 
        df = df.reset_index(drop=True)
        
    return df

#%%
