import numpy as np
import datetime as dt
import pandas as pd

a = np.arange(10)
print(a)

now = dt.datetime.now()
print('Halo teman. Waktu sekarang adalah {}'.format(now))

data = pd.read_csv('data.csv')
