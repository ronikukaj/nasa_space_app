import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = ['2020-01-04', '2020-01-14', '2020-01-24', '2020-02-04', '2020-02-14', '2020-02-24', '2020-03-04', '2020-03-14',
 '2020-03-24', '2020-04-04', '2020-04-14', '2020-04-24', '2020-05-04', '2020-05-14', '2020-05-24', '2020-06-04', '2020-06-14',
  '2020-06-24', '2020-07-04', '2020-07-14', '2020-07-24', '2020-08-04', '2020-08-14', '2020-08-24', '2020-09-04', '2020-09-14',
   '2020-09-24']

dataset = pd.read_csv('../data/world_covid.csv', sep=',')
dataset = dataset[['location', 'date', 'total_deaths_per_million', 'total_cases_per_million']]
data_spain = dataset.loc[dataset['location'] == 'Spain']
data_spain = data_spain[data_spain['date'].isin(dates)]
deaths_spain = np.array(data_spain['total_deaths_per_million'])
cases_spain = np.array(data_spain['total_cases_per_million'])

data_barcelona = pd.read_csv('../data/Barcelona.csv', sep=',')
data_barcelona = data_barcelona[['Date', 'City', 'Baseline_Mean']]
data_barcelona_final = data_barcelona[data_barcelona['Date'].isin(dates)]
barcelona_values = np.array(data_barcelona_final['Baseline_Mean'])


for i in range(len(dates)):
    dates[i] = '-'.join(dates[i].split('-')[1:])

for i in range(len(barcelona_values)):
    barcelona_values[i] *= 1000

plt.title('SPAIN PLOT')
plt.plot(dates, cases_spain)
plt.plot(dates, deaths_spain)
plt.plot(dates, barcelona_values)

plt.grid(color='b', linestyle='-', linewidth=0.2)

plt.legend(['Spain cases pm', 'Spain deaths pm', 'x * 1e12 NO2 in Barcelona'])
plt.xlabel('Dates')

plt.show()
