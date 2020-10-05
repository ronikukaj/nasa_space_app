import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = ['2020-01-04', '2020-01-14', '2020-01-24', '2020-02-04', '2020-02-14', '2020-02-24', '2020-03-04', '2020-03-14',
 '2020-03-24', '2020-04-04', '2020-04-14', '2020-04-24', '2020-05-04', '2020-05-14', '2020-05-24', '2020-06-04', '2020-06-14',
  '2020-06-24', '2020-07-04', '2020-07-14', '2020-07-24', '2020-08-04', '2020-08-14', '2020-08-24', '2020-09-04', '2020-09-14',
   '2020-09-24']

dataset = pd.read_csv('../data/world_covid.csv', sep=',')

dataset = dataset[['location', 'date', 'total_deaths_per_million']]
data_spain = dataset.loc[dataset['location'] == 'Spain']
data_australia = dataset.loc[dataset['location'] == 'Australia']
data_germany = dataset.loc[dataset['location'] == 'Germany']
data_india = dataset.loc[dataset['location'] == 'India']
data_sweden = dataset.loc[dataset['location'] == 'Sweden']

data_spain = data_spain[data_spain['date'].isin(dates)]
data_australia = data_australia[data_australia['date'].isin(dates)]
data_germany = data_germany[data_germany['date'].isin(dates)]
data_india = data_india[data_india['date'].isin(dates)]
data_sweden = data_sweden[data_sweden['date'].isin(dates)]

cases_spain = np.array(data_spain['total_deaths_per_million'])
cases_australia = np.array(data_australia['total_deaths_per_million'])
cases_germany = np.array(data_germany['total_deaths_per_million'])
cases_india = np.array(data_india['total_deaths_per_million'])
cases_sweden = np.array(data_sweden['total_deaths_per_million'])

for i in range(len(dates)):
    dates[i] = '-'.join(dates[i].split('-')[1:])

plt.title('COVID-19 DEATHS')
plt.plot(dates, cases_spain)
plt.plot(dates, cases_australia)
plt.plot(dates, cases_germany)
plt.plot(dates, cases_india)
plt.plot(dates, cases_sweden)

plt.grid(color='b', linestyle='-', linewidth=0.2)

plt.legend(['Spain', 'Australia', 'Germany', 'India', 'Sweden'])
plt.ylabel('Total deaths per million')
plt.xlabel('Dates')

plt.show()
