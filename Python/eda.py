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

sample = data.query('id == "3c1e4c52"')
print(sample['date_time'].count())




df = pd.DataFrame(
    {
        'From': [
            'Moscow',
            'Moscow',
            'St. Petersburg',
            'St. Petersburg',
            'St. Petersburg',
        ],
        'To': ['Rome', 'Rome', 'Rome', 'Barcelona', 'Barcelona'],
        'Is_Direct': [False, True, False, False, True],
        'Has_luggage': [True, False, False, True, False],
        'Price': [21032, 19250, 19301, 20168, 31425],
        'Date_From': [
            '01.07.19',
            '01.07.19',
            '04.07.2019',
            '03.07.2019',
            '05.07.2019',
        ],
        'Date_To': [
            '07.07.19',
            '07.07.19',
            '10.07.2019',
            '09.07.2019',
            '11.07.2019',
        ],
        'Airline': ['Belavia', 'S7', 'Finnair', 'Swiss', 'Rossiya'],
        'Travel_time_from': [995, 230, 605, 365, 255],
        'Travel_time_to': [350, 225, 720, 355, 250],
    }
)
print(df.query('(Has_luggage == False) and (Airline not in["S7", "Rossiya"])'))
max_time = 300
print(df.query('(Airline in ["Belavia", "S7", "Rossiya"]) and (Travel_time_from < @max_time)'))