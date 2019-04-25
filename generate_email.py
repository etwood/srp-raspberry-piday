from pandas import read_csv
from pandas import datetime
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import datetime

currentDT = datetime.datetime.now()
print('Graph generated')
print(str(currentDT))
print

series = read_csv('/home/pi/srp/piday/output.csv', header=None, parse_dates=[0], index_col=0, names=['Date/Time','Reading'] )

# print('Max:' + str(series.max))
# print('Min:' + series.min)
# print('N:' + len(series.index))

print(series.describe())
print

solar_minutes = series.resample('1Min')
solar_minutes_mean = solar_minutes.mean()
print(solar_minutes_mean.head())
solar_minutes_mean.plot()
pyplot.savefig('/home/pi/srp/piday/output.png')
