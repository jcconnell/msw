# -*- coding: utf-8 -*-

import pandas as pd
import datetime as dt

def dictToSeries(df : pd.DataFrame, column : str):
    """
    """
    # Convert those columns with dictionaries in each row to pd.Series
    df = pd.concat([df, df[column].apply(pd.Series)], axis=1)
    df = df.drop(column, axis=1)
    
    return df

def parsePeriod(df : pd.DataFrame, column : str):
    """
    """
    # Extract Period swell from column
    df[column] = df[column].apply(pd.Series)
    df[column] = df[column].apply(pd.Series)
    # Rename colum to period
    df= df.rename(columns={column:'period'})
    
    return df

def processJson(target_url : str, spot_name : str, longitude : int,
                latitude : int):
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
    # Column with spot name
    df['spot'] = spot_name
    # Longitude and latitude columns
    df['longitude'] = longitude
    df['latitude'] = latitude
    # Row with value equal to datetime now
    df['now'] = dt.datetime.now()
    # Calculate timedelta between now and forecasted date
    df['delta'] = (df['timestamp'] - df['now'])
    # Only positive deltas
    df = df[df['delta'] >= pd.Timedelta(0)]
    # Sort values by delta, nearest to furthest away
    df = df.sort_values('delta')
    # Drop duplicates keeping only the very next forecast only
    df = df.drop_duplicates(subset='spot')
    # Convert wind and swell cols from dictionaries to pd.Series
    df = dictToSeries(df=df, column='wind')
    df = dictToSeries(df=df, column='swell')
    # Parse Period info
    df = parsePeriod(df=df, column='components')
    # Select only days with a "good" swell
#    df = df[(df.solidRating >= 3)]
            
    # Reset index
    df = df.reset_index(drop=True)
    
    return df

def scrapeSurfSpots(spots : pd.DataFrame):
    """
    loops through surf_spots and scrapes each json table from its respective 
    api using processJson() and returns a DataFrame with all json tables concatenated.
    Parameters
    --------
    spots : 
    
    Returns
    --------
    df : DataFrame containing all relevant surf forecasts for each spot in
         surf_spots, pd.DataFrame
    """
    # Create empty DataFrame
    df = pd.DataFrame([])
    # Retrieve data for each surf spot from msw api
    for idx, row in spots.iterrows():
        print('\nGetting forecast info for', row['spot'])
        # Access MSW API
        df = pd.concat([df, processJson(target_url=row.target,
                                        spot_name=row.spot,
                                        longitude=row.longitude,
                                        latitude=row.latitude)])
        # Reset Index 
        df = df.reset_index(drop=True)
        
    return df
