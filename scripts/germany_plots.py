import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = ['2020-01-04', '2020-01-14', '2020-01-24', '2020-02-04', '2020-02-14', '2020-02-24', '2020-03-04', '2020-03-14',
 '2020-03-24', '2020-04-04', '2020-04-14', '2020-04-24', '2020-05-04', '2020-05-14', '2020-05-24', '2020-06-04', '2020-06-14',
  '2020-06-24', '2020-07-04', '2020-07-14', '2020-07-24', '2020-08-04', '2020-08-14', '2020-08-24', '2020-09-04', '2020-09-14',
   '2020-09-24']

dataset = pd.read_csv('../data/world_covid.csv', sep=',')
dataset = dataset[['location', 'date', 'total_deaths_per_million', 'total_cases_per_million']]
data_germany = dataset.loc[dataset['location'] == 'Germany']
data_germany = data_germany[data_germany['date'].isin(dates)]
deaths_germany = np.array(data_germany['total_deaths_per_million'])
cases_germany = np.array(data_germany['total_cases_per_million'])

data_munich = pd.read_csv('../data/Munich.csv', sep=',')
data_munich = data_munich[['Date', 'City', 'Baseline_Mean']]
data_munich_final = data_munich[data_munich['Date'].isin(dates)]
munich_values = np.array(data_munich_final['Baseline_Mean'])


for i in range(len(dates)):
    dates[i] = '-'.join(dates[i].split('-')[1:])

for i in range(len(munich_values)):
    munich_values[i] *= 1000

plt.title('GERMANY PLOT')
plt.plot(dates, cases_germany)
plt.plot(dates, deaths_germany)
plt.plot(dates, munich_values)

plt.grid(color='b', linestyle='-', linewidth=0.2)

plt.legend(['Germany cases pm', 'Germany deaths pm', 'x * 1e12 NO2 in Munich'])
plt.xlabel('Dates')

plt.show()
