import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('../data/air_pollution_deaths.csv', sep=',')
years = np.array(dataset['year'])
deaths = np.array(dataset['deaths'])

plt.title('AIR POLLUTION DEATHS')

plt.plot(years, deaths)

plt.xlabel('Years')
plt.ylabel('Deaths')
plt.grid(color='b', linestyle='dashed', linewidth=0.2)
plt.show()
