import pandas as pd
import yaml

class msw:
    def __init__(self, data=None, api_yml=None):
        # Retrieve api key
        if api_yml == None:
            self.api_yml = './api_key.yml'
        # Load Personal api key
        self.api_key = yaml.load(open(self.api_yml))['api_key']
        
        # Api url stub
        self.url = 'http://magicseaweed.com/api/'
        # Fields to include in api request
        fields = ['timestamp','fadedRating','solidRating','wind.direction',
                  'wind.speed','swell.maxBreakingHeight',
                  'swell.components.combined.period']
        # Fields in url form in accordance with msw api
        self.fields = '&fields=' + ','.join(fields)
        
        # Define data
        if data == None:
            self.data = '../data/surfspots.csv'
        # Load surf spots
        self.df_spots = pd.read_csv(self.data,
                                    sep=',', 
                                    usecols=['spot','spot_id'])
        # Column giving taret api url for each surf spot
        self.df_spots['target'] = (self.url + str(self.api_key) + '/forecast/?spot_id=' + 
                                   self.df_spots['spot_id'].astype(str) + self.fields)
        
        
        
#%%
"""
TO DO
- rename this .py >> msw
- rename msw.py to utils.py
- re-configure utils so it can scrape spots can be used in spotCheck
"""