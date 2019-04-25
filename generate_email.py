from pandas import read_csv
from pandas import datetime
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import datetime

# Voltage on MCP3008 measured @ 4.59V
def volts_from_reading(row):
    return row['Reading'] * 4.59 / 1024

currentDT = datetime.datetime.now()
print('Graph generated')
print(str(currentDT))
print

series = read_csv('/home/pi/srp/piday/output.csv', header=None, parse_dates=[0], index_col=0, names=['Date/Time','Reading'] )

series['Volts'] = series.apply (volts_from_reading, axis=1)

print(series.describe())
print

solar_minutes = series.resample('1Min')
solar_minutes_mean = solar_minutes.mean()
print(solar_minutes_mean.head())
solar_minutes_mean.plot()
pyplot.savefig('/home/pi/srp/piday/output.png')
