import pandas as pd
import matplotlib.pyplot as plt
import os
plt.style.use('seaborn')

FREEMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv',url=FREEMONT_URL,
		force_download=False):
    """
	dOWNLOAD data
    """
    if force_download or not os.path.exists(filename):
        from urllib.request import urlretrieve
        urlretrieve(URL,'Fremont.csv')
    data = pd.read_csv('Fremont.csv',index_col='Date',parse_dates=True)
    data.drop('Fremont Bridge Total',axis=1,inplace=True)
    data.columns = ['East','West']
    return data
