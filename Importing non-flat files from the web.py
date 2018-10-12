# Import package
from urllib.request import urlretrieve
import pandas as pd

# Assign url of file: url
url ='http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xl
xl = pd.read_excel(url,sheetname=None)

# Print the sheet names to the shell
m = xl.keys()
print(m)

# Print the head of the first sheet (using its name, NOT its index)
print(xl["1700"].head())
