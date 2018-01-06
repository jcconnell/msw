
import msw
import geoVisual as gv

print('Check Surf Forecasts')

# Create string to add to url to specify which fields to parse
fields_url = msw.fieldsToUrl(fields=msw.fields)

# Scrape surf spot data
df = msw.scrapeSurfSpots(surf_spots=msw.surf_spots, 
                         fields=fields_url,
                         live=True)
    
# Print Results
if df.empty:
    print('\nNo Suitable days for surf :(')
else:
    # Print reply
    print('\nThere is surf! :)\n', df)
    # Merge forecast data to geographic data
    df = gv.mergeGeoData(forecast_df = df)
    # Draw and open geographic visualisation
    gv.drawSurfMap(df)