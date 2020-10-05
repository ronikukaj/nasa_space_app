import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = ['2020-01-04', '2020-01-14', '2020-01-24', '2020-02-04', '2020-02-14', '2020-02-24', '2020-03-04', '2020-03-14',
 '2020-03-24', '2020-04-04', '2020-04-14', '2020-04-24', '2020-05-04', '2020-05-14', '2020-05-24', '2020-06-04', '2020-06-14',
  '2020-06-24', '2020-07-04', '2020-07-14', '2020-07-24', '2020-08-04', '2020-08-14', '2020-08-24', '2020-09-04', '2020-09-14',
   '2020-09-24']

dataset = pd.read_csv('../data/world_covid.csv', sep=',')
dataset = dataset[['location', 'date', 'total_deaths_per_million', 'total_cases_per_million']]
data_india = dataset.loc[dataset['location'] == 'India']
data_india = data_india[data_india['date'].isin(dates)]
deaths_india = np.array(data_india['total_deaths_per_million'])
cases_india = np.array(data_india['total_cases_per_million'])

data_new_delhi = pd.read_csv('../data/New_Delhi.csv', sep=',')
data_new_delhi = data_new_delhi[['Date', 'City', 'Baseline_Mean']]
data_new_delhi_final = data_new_delhi[data_new_delhi['Date'].isin(dates)]
new_delhi_values = np.array(data_new_delhi_final['Baseline_Mean'])


for i in range(len(dates)):
    dates[i] = '-'.join(dates[i].split('-')[1:])

for i in range(len(new_delhi_values)):
    new_delhi_values[i] *= 1000

plt.title('INDIA PLOT')
plt.plot(dates, cases_india)
plt.plot(dates, deaths_india)
plt.plot(dates, new_delhi_values)

plt.grid(color='b', linestyle='-', linewidth=0.2)

plt.legend(['India cases pm', 'India deaths pm', 'x * 1e12 NO2 in New Delhi'])
plt.xlabel('Dates')

plt.show()
