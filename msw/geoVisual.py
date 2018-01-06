#!/usr/bin/env python3
#%%
import folium
import pandas as pd
import os
import webbrowser

#%%
# Read surf spot location data
df_geo = pd.read_csv('../data/surfspots.csv',sep=',')

#%%
def mergeGeoData(forecast_df : pd.DataFrame):
    # Merge surf forecast with geo data
    df = forecast_df.merge(df_geo, on='spot', how='inner')
    # Sort Data by SolidRating
    df = df.sort_values('solidRating', ascending=False)
    # Drop duplicates
    df = df.drop_duplicates(subset=['spot'])
    
    return df
    
def drawSurfMap(df : pd.DataFrame):
    # Intialise folium
    m = folium.Map([50, 0], zoom_start=4)
    
    # Add a cirlce marker for each spot
    for i, row in df.iterrows():
        popup = row['spot'] + ': ' + str(row['solidRating']) + ' stars'
        folium.CircleMarker(location=[row['longitude'], row['latitude']],
                            radius=row['solidRating']*4, 
                            fill=True, 
                            popup=popup, 
                            weight=1,
                            fill_color='Blue',
                            color=None,
                            fill_opacity=0.5
                            ).add_to(m)
    # Save map as html
    m.save('./surf_spots.html')
    # Open html file in web browser
    webbrowser.open('file://' + os.path.realpath('./surf_spots.html'))


