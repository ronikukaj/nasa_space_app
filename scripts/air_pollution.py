import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_barcelona = pd.read_csv('../data/Barcelona.csv', sep=',')
data_melbourne = pd.read_csv('../data/Melbourne.csv', sep=',')
data_munich = pd.read_csv('../data/Munich.csv', sep=',')
data_new_delhi = pd.read_csv('../data/New_Delhi.csv', sep=',')
data_stockholm = pd.read_csv('../data/Stockholm.csv', sep=',')

data_barcelona = data_barcelona[['Date', 'City', 'Baseline_Mean']]
data_melbourne = data_melbourne[['Date', 'City', 'Baseline_Mean']]
data_munich = data_munich[['Date', 'City', 'Baseline_Mean']]
data_new_delhi = data_new_delhi[['Date', 'City', 'Baseline_Mean']]
data_stockholm = data_stockholm[['Date', 'City', 'Baseline_Mean']]


dates = ['2020-01-04', '2020-01-14', '2020-01-24', '2020-02-04', '2020-02-14', '2020-02-24', '2020-03-04', '2020-03-14',
 '2020-03-24', '2020-04-04', '2020-04-14', '2020-04-24', '2020-05-04', '2020-05-14', '2020-05-24', '2020-06-04', '2020-06-14',
  '2020-06-24', '2020-07-04', '2020-07-14', '2020-07-24', '2020-08-04', '2020-08-14', '2020-08-24', '2020-09-04', '2020-09-14',
   '2020-09-24']

data_barcelona_final = data_barcelona[data_barcelona['Date'].isin(dates)]
data_melbourne_final = data_melbourne[data_melbourne['Date'].isin(dates)]
data_munich_final = data_munich[data_munich['Date'].isin(dates)]
data_new_delhi_final = data_new_delhi[data_new_delhi['Date'].isin(dates)]
data_stockholm_final = data_stockholm[data_stockholm['Date'].isin(dates)]

barcelona_values = np.array(data_barcelona_final['Baseline_Mean'])
melbourne_values = np.array(data_melbourne_final['Baseline_Mean'])
munich_values = np.array(data_munich_final['Baseline_Mean'])
new_delhi_values = np.array(data_new_delhi_final['Baseline_Mean'])
stockholm_values = np.array(data_stockholm_final['Baseline_Mean'])

for i in range(len(dates)):
    dates[i] = '-'.join(dates[i].split('-')[1:])

plt.title('NO2 AIR POLLUTION')

plt.plot(dates, barcelona_values)
plt.plot(dates, melbourne_values)
plt.plot(dates, munich_values)
plt.plot(dates, new_delhi_values)
plt.plot(dates, stockholm_values)

plt.grid(color='b', linestyle='-', linewidth=0.2)
plt.xlabel('Dates')
plt.ylabel(' x * 1e15 NO2 molecules/cm2')
plt.legend(['Barcelona', 'Melbourne', 'Munich', 'New Delhi', 'Stockholm'])

plt.show()
