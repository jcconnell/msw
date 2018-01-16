import matplotlib as mpl
import folium
import pandas as pd
import numpy as np
import os
import webbrowser

def calcColors(values : pd.Series):
    """
    For a given series this function calculates an RGB color for each value
    in the series. Larger numbers will be allocated a darker color.
    
    Parameters
    --------
    values : a series conatining interger or float values
    
    Returns
    --------
    colors : a list of RGB colors, list
    """
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
    For each value in a given series the float or integer provided is converted 
    into a number that can be used to determine the size of a point in a plot.
    Parameters
    --------
    values : a series conatining interger or float values
    
    Returns
    --------
    sizes : a list of point sizes, list
    
    """
    # Calculate size of bubble
    sizes = np.where(values < 16, ((values**3)**0.5)*1.3, ((17**3)**0.5)*1.3)
                              
    return sizes.tolist()
    
def drawSurfMap(df : pd.DataFrame):
    """
    Using folium a html map is created with a circle marker for each surf spot.
    The circle's size is determined by the max breaking wave height and the 
    color intensity by the number of MSW solid stars of the swell. A popup marker
    is included providing further information: spot name, swell height, period 
    and number of MSW solid stars.
    
    Parameters
    --------
    df : DataFrame with the following columns: spot, solidRating, maxBreakingHeight,
    longitude and latitude, pd.DataFrame
    
    Returns
    --------
    m : folium html map, folium.map
    """
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


