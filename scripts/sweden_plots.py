import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = ['2020-01-04', '2020-01-14', '2020-01-24', '2020-02-04', '2020-02-14', '2020-02-24', '2020-03-04', '2020-03-14',
 '2020-03-24', '2020-04-04', '2020-04-14', '2020-04-24', '2020-05-04', '2020-05-14', '2020-05-24', '2020-06-04', '2020-06-14',
  '2020-06-24', '2020-07-04', '2020-07-14', '2020-07-24', '2020-08-04', '2020-08-14', '2020-08-24', '2020-09-04', '2020-09-14',
   '2020-09-24']

dataset = pd.read_csv('../data/world_covid.csv', sep=',')
dataset = dataset[['location', 'date', 'total_deaths_per_million', 'total_cases_per_million']]
data_sweden = dataset.loc[dataset['location'] == 'Sweden']
data_sweden = data_sweden[data_sweden['date'].isin(dates)]
deaths_sweden = np.array(data_sweden['total_deaths_per_million'])
cases_sweden = np.array(data_sweden['total_cases_per_million'])

data_stockholm = pd.read_csv('../data/Stockholm.csv', sep=',')
data_stockholm = data_stockholm[['Date', 'City', 'Baseline_Mean']]
data_stockholm_final = data_stockholm[data_stockholm['Date'].isin(dates)]
stockholm_values = np.array(data_stockholm_final['Baseline_Mean'])


for i in range(len(dates)):
    dates[i] = '-'.join(dates[i].split('-')[1:])

for i in range(len(stockholm_values)):
    stockholm_values[i] *= 1000

plt.title('SWEDEN PLOT')
plt.plot(dates, cases_sweden)
plt.plot(dates, deaths_sweden)
plt.plot(dates, stockholm_values)

plt.grid(color='b', linestyle='-', linewidth=0.2)

plt.legend(['Sweden cases pm', 'Sweden deaths pm', 'x * 1e12 NO2 in Stockholm'])
plt.xlabel('Dates')

plt.show()
