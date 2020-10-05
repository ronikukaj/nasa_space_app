import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = ['2020-01-04', '2020-01-14', '2020-01-24', '2020-02-04', '2020-02-14', '2020-02-24', '2020-03-04', '2020-03-14',
 '2020-03-24', '2020-04-04', '2020-04-14', '2020-04-24', '2020-05-04', '2020-05-14', '2020-05-24', '2020-06-04', '2020-06-14',
  '2020-06-24', '2020-07-04', '2020-07-14', '2020-07-24', '2020-08-04', '2020-08-14', '2020-08-24', '2020-09-04', '2020-09-14',
   '2020-09-24']

dataset = pd.read_csv('../data/world_covid.csv', sep=',')
dataset = dataset[['location', 'date', 'total_deaths_per_million', 'total_cases_per_million']]
data_melbourne = dataset.loc[dataset['location'] == 'Australia']
data_melbourne = data_melbourne[data_melbourne['date'].isin(dates)]
deaths_melbourne = np.array(data_melbourne['total_deaths_per_million'])
cases_melbourne = np.array(data_melbourne['total_cases_per_million'])

data_melbourne = pd.read_csv('../data/Melbourne.csv', sep=',')
data_melbourne = data_melbourne[['Date', 'City', 'Baseline_Mean']]
data_melbourne_final = data_melbourne[data_melbourne['Date'].isin(dates)]
melbourne_values = np.array(data_melbourne_final['Baseline_Mean'])


for i in range(len(dates)):
    dates[i] = '-'.join(dates[i].split('-')[1:])

for i in range(len(melbourne_values)):
    melbourne_values[i] *= 1000

plt.title('AUSTRALIA PLOT')
plt.plot(dates, cases_melbourne)
plt.plot(dates, deaths_melbourne)
plt.plot(dates, melbourne_values)

plt.grid(color='b', linestyle='-', linewidth=0.2)

plt.legend(['Australia cases pm', 'Australia deaths pm', 'x * 1e12 NO2 in Melbourne'])
plt.xlabel('Dates')

plt.show()
