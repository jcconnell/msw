#!/usr/bin/env python3
#%%
import matplotlib as mpl
import folium
import pandas as pd
import numpy as np
import os
import webbrowser

#%%
def calcColors(values : pd.Series):
    # Convert series to list
    values = values.tolist()
    # Create color for each value in values
    colors = ["#%02x%02x%02x" % (int(r), int(g), int(b))
                        for r, g, b, _ in 
                        255*mpl.cm.OrRd(mpl.colors.Normalize()(values))
             ]
    
    return colors

def calcSize(values : pd.Series):
    """
    """
    # Calculate size of bubble
    sizes = np.where(values < 16, ((values**3)**0.5)*1.3, ((17**3)**0.5)*1.3)
                              
    return sizes.tolist()
    
def drawSurfMap(df : pd.DataFrame):
    # Calculate color values for color map
    colors = calcColors(df['solidRating'])
    # Calculate sizes
    sizes = calcSize(df['maxBreakingHeight'])  
    
    # Intialise folium
    m = folium.Map([50, 0], zoom_start=3.5, tiles='cartodbpositron')
    
    # Add a cirlce marker for each spot
    for i, row in df.iterrows():
        # Define popup text
        popup = (row['spot'] + 
                 '<br>msw stars: ' + str(row['solidRating']) + 
                 '<br>wave height: ' + str(row['maxBreakingHeight']) + 'ft' +
                 ' @ ' + str(row['period']) + 's')
        # Add CircleMarker to map for each spot
        folium.CircleMarker(location=[row['longitude'], row['latitude']],
                            radius=sizes[i], 
                            fill=True, 
                            popup=popup, 
                            #weight=1,
                            fill_color=colors[i],
                            color=None,
                            fill_opacity=0.7
                            ).add_to(m)
    # Save map as html
    m.save('../index.html')
    # Open html file in web browser
    webbrowser.open('file://' + os.path.realpath('../index.html'))


