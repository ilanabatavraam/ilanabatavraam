import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('/datasets/visits.csv', sep='\t')
stat = data.pivot_table(index='name', values='time_spent')
total_visits = data['date_time'].count()
total_stations = len(data['id'].unique())
data['date_time_days'] = pd.to_datetime(
    data['date_time'], format='%Y%m%dT%H%M%S'
    )
total_days = data['date_time_days'].max().day - data['date_time_days'].min().day
station_visits_per_day = total_visits / total_stations / total_days

data['time_spent'].hist(bins=100, range=(0, 1500))
                        
plt.ylim(-100, 1000)
data.boxplot()
print(data.describe())
data.hist('age', range=(18, 30))