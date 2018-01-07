#!/usr/bin/env python3
#%%
import matplotlib as mpl
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
    # Reset index
    df = df.reset_index(drop=True)
    
    return df

def calcColors(values : pd.Series):
    # Convert series to list
    values = values.tolist()
    # Create color for each value in values
    colors = ["#%02x%02x%02x" % (int(r), int(g), int(b))
                        for r, g, b, _ in 
                        255*mpl.cm.OrRd(mpl.colors.Normalize()(values))
             ]
    
    return colors
    
def drawSurfMap(df : pd.DataFrame):
    # Calculate color values for color map
    colors = calcColors(df['solidRating'])
    
    # Intialise folium
    m = folium.Map([50, 0], zoom_start=4, tiles='cartodbpositron')
    
    # Add a cirlce marker for each spot
    for i, row in df.iterrows():
        # Define popup text
        popup = (row['spot'] + 
                 '<br>msw stars: ' + str(row['solidRating']) + 
                 '<br>wave height: ' + str(row['maxBreakingHeight']) + 'ft' +
                 ' @ ' + str(row['period']) + 's')
        # Add CircleMarker to map for each spot
        folium.CircleMarker(location=[row['longitude'], row['latitude']],
                            radius=((row['maxBreakingHeight']**3)**0.5)*1.5, 
                            fill=True, 
                            popup=popup, 
                            weight=1,
                            fill_color=colors[i],
                            color=None,
                            fill_opacity=0.6
                            ).add_to(m)
    # Save map as html
    m.save('./surf_spots.html')
    # Open html file in web browser
    webbrowser.open('file://' + os.path.realpath('./surf_spots.html'))


