import msw

print('Surf Forecast Check 3000\n')

# Create string to add to url to specify which fields to parse
fields_url = msw.fieldsToUrl(fields=msw.fields)

# Scrape surf spot data
df = msw.scrapeSurfSpots(surf_spots=msw.surf_spots, fields=fields_url)
    
# Print Results
if df.empty:
    print('\nNo Suitable days for surf :(')
else:
    print('\nThere is surf! :)\n', df)