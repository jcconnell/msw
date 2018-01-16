import pandas as pd
import yaml

class Msw:
    def __init__(self, data=None, api_yml=None):
        """
        Intialises msw with data and an api key.
        
        Parameters
        --------
        data : Must contain spot name, msw spot id and longitude and latitude of
        spot location, str
        api_yml : yaml file with personal msw api key
        
        Returns
        --------
        api_key : personal msw api key, str
        fields : fields in accordance with api url, str
        df_spots : DataFrame with spot information, pd.DataFrame
        """
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
        self.df_spots = pd.read_csv(self.data, sep=',')
        # Column giving taret api url for each surf spot
        self.df_spots['target'] = (self.url + str(self.api_key) + '/forecast/?spot_id=' + 
                                   self.df_spots['spot_id'].astype(str) + self.fields)
        
        