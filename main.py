from src import EkosSelenium
from src import renamefile
from src import GoogleAPI

# Initialize Classes
ekos = EkosSelenium.EkosSelenium()
rename = renamefile.RenameFile()
gAPI = GoogleAPI.GoogleAPI()

# Define Variables
eUsername = 'EKOS USERNAME'
ePass = 'EKOS PASSWORD'
report = 'Taproom Inventory - Transfers Last Month'
PATH = '/PATH/TO/FILES/'

# Download Report
ekos.login(eUsername, ePass)
ekos.download_report(report)
# Rename Report
rename.rename_file('trTransfers.csv', PATH)
# Update sheet via Google API
gAPI.import_data(PATH)
# Terminate webdriver
ekos.quit()
