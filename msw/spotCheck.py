import utils
from msw import Msw
import geoVisual as gv
from autogit import autoGit

print('MSW Visualisation')

# Intialise msw
msw = Msw()

# Scrape surf spot data
df = utils.scrapeSurfSpots(spots=msw.df_spots)

# Print Results
if df.empty:
    print('\nNo Suitable days for surf :(')
else:
    # Draw and open geographic visualisation
    gv.drawSurfMap(df)

# Commit and push index.html to remote directory
#autoGit(local_directory='../',
#        file_to_add='index.html',
#        comment='updating index.html',
#        author='HowardRiddiough')
