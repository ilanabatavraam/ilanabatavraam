import pandas as pd

music = [
    ['Bob Dylan', 'Like A Rolling Stone'],
    ['John Lennon', 'Imagine'],
    ['The Beatles', 'Hey Jude'],
    ['Nirvana', 'Smells Like Teen Spirit'],
]

entries = ['artist', 'track']

playlist = pd.DataFrame(data=music, columns=entries)
print(playlist)

#read_csv() to open csv     board_df = pd.read_csv('game_board.csv')

# to print 5 rows, print(data_df.head()) use .head() or fill how much you want. ex.: .head(10)

# tail() print the last

# dtypes types
# columns 
# shape size

#### PANDAS
# object (string)
# int64 (int) 3
# float64 (float) 3.14
# bool


# print(df.shape) => (123, 456) 123 - rows, 456 - columns TUPLE


# df.info() full info 


columns = ['movie_name', 'country', 'year', 'genre', 'duration', 'rating'] 

movies_df = pd.DataFrame(data=movies_table, columns=columns)

print(movies_df[movies_df['duration'] > 180]) 


### LOC()
df = pd.read_csv('music_log.csv')
result = df.loc[4, 'genre'] # 4 - row, 'genre' - column
print(result)

# 1 cell 	.loc[7, 'genre']  
# 1 column	.loc[:, 'genre']  / df['genre']
# ~ columns	.loc[:, ['genre', 'Artist']]   / df[['genre', 'Artist']]
# columns from to	.loc[:, 'total play': 'genre']
# 1 row	.loc[1]
# rows from	.loc[1:]   / df[1:]   
# rows to	.loc[:3]  / df[:3] (3 not includes)
# rows from to	.loc[2:5]  / df[2:5] (5 not includes)


df = pd.read_csv('music_log.csv')

genre_fight = df[['genre', 'Artist']]

print(genre_fight)


#### COUNT ROWS IN COLUMN WITHOUT IF
df = pd.read_csv('music_log.csv')
genre_fight = df[['genre', 'Artist']]
# only pop
genre_pop = df.loc[df.loc[:, 'genre'] == 'pop']['genre'].count()
print(genre_pop)




df = pd.read_csv('music_log.csv')

rock = df[df['genre'] == 'rock']
rock_time = rock['total play']
rock_haters = rock_time[rock_time <= 5].count() ## !!!
print(rock_haters)

pop = df[df['genre'] == 'pop']
pop_time = pop['total play']
pop_haters = pop_time[pop_time <= 5].count() ## !!!
print( pop_haters)


df.columns ## all columns
df = df.rename(columns={'  user_id': 'user_id', 'total play': 'total_play', 'Artist': 'artist'})

# isna() is finding NaN
print(cholera.isna().sum()) 
# isnull() is working, but it's better to use # isna()

# fillna() is filling smth instead of Nan
cholera['imported_cases'] = cholera['imported_cases'].fillna(0)

# dropna() is checking choosed columns to remove rows with Nan
cholera = cholera.dropna(subset=['total_cases', 'deaths', 'case_fatality_rate'])

# or removing columns, not rows
cholera = cholera.dropna(axis='columns')

#duplicated()
print(df.duplicated().sum()) 

# printing only duplicates
duplicated_df = df[df.duplicated()].head()

# removing duplicates
#drop_duplicates()
df = df.drop_duplicates()

# to correct index after cleaning
df = df.drop_duplicates().reset_index()
# and remove old index
df = df.drop_duplicates().reset_index(drop=True)

# unique()  to check manually
print(tennis['name'].unique())

# replace() to rename not unique
tennis['name'] = tennis['name'].replace('Roger Federer', 'RF')
tennis['name'] = tennis['name'].replace('Roger Fderer', 'RF')
tennis['name'] = tennis['name'].replace('Roger Fdrer', 'RF')
#  or smarter
duplicates = ['Roger Fderer', 'Roger Fdrer', 'Roger Federer'] 
name = 'RF' 
tennis['name'] = tennis['name'].replace(duplicates, name) 

# groupby()
track_grouping = df.groupby('user_id')['genre_name'].count()
track_counting = track_grouping[track_grouping > 50] #!!!

# sort_values()
print(exoplanet.sort_values(by='radius').head(30))
print(exoplanet[exoplanet['radius'] < 1])
print(exoplanet[exoplanet['discovered'] == 2014])
exo_small_14 = exo_small_14[exo_small_14['discovered'] == 2014]
print(exo_small_14) 
print(exo_small_14.sort_values(by='radius', ascending=False))

# .median() and .mean()


df = pd.read_csv('music_log_upd.csv')

pop_music = df[df['genre_name'] == 'pop']
pop_music = pop_music[pop_music['total_play_seconds'] != 0]

pop_music_max_total_play = pop_music['total_play_seconds'].max()

pop_music_max_info = pop_music[pop_music['total_play_seconds'] == pop_music_max_total_play]['total_play_seconds'] 
print(pop_music_max_info)


genre_rock = df[df['genre_name'] == 'rock']
genre_rock = genre_rock[genre_rock['total_play_seconds'] > 0]
genre_rock_max = genre_rock['total_play_seconds'].max()
genre_rock_min = genre_rock['total_play_seconds'].min()

data = [['pop', 8663, 34.6, 1158.03, 0.000794],
       ['rock', 6828, 33.3, 1699.14882, 0.014183]]
columns = ['genre_name','total_track','skip_track','max_total_time','min_total_time']


research_genres_result = pd.DataFrame(data=data, columns=columns)


email_visits = 1000 
context_visits = 2500
email_purchases = 50 
context_purchases = 100 

email_conversion = (email_purchases / email_visits) * 100
context_conversion = (100 / context_visits) * 100

print('Email Conversion: {:.0f}%'.format(email_conversion))
print('Context Conversion: {:.0f}%'.format(context_conversion))


purchases = pd.read_csv('/datasets/returned.csv')
purchases['total'] = purchases['first'] + purchases['repeated']
purchases['repeated_share'] = purchases['repeated'] / purchases['total']
print(purchases.sort_values(by='repeated_share', ascending=False))


logs = pd.read_csv('/datasets/logs.csv')
print(f"Уникальных email: {len(logs['email'].unique())}")
print(f"Уникальных User ID: {len(logs['user_id'].unique())}")


hogwarts_points = pd.read_csv('/datasets/hogwarts_points.csv')
hogwarts_points['faculty_name'] = hogwarts_points['faculty_name'].fillna(value='Gryffindor')
print('Total student points:', hogwarts_points['points'].sum())
print('Total faculty points:', hogwarts_points.groupby('faculty_name')['points'].sum().sum())

print('The Cup goes to:', hogwarts_points.groupby('faculty_name')['points'].sum().idxmax())


logs = pd.read_csv('/datasets/logs.csv')
visits = logs.groupby('source')['purchase'].count()
purchase = visits = logs.groupby('source')['purchase'].sum()
conversion = purchase / visits
print(conversion)

## catching only string from cell
data = pd.read_csv('/datasets/projects.csv')
print(data.loc[data['Name'] == 'A', 'Col'].values[0])
#OR
print(data.loc[data['Name'] == 'A', 'Col'].to_string(index=False))
data.loc[:, 'New'] = data.loc[:, 'New'].fillna('+')
rows = [True, False, True, False, False, False, True, False]
print(data.loc[rows])
rows = data['New'] == '+'
print(rows)
# 0     True
# 1     True
# 2    False
# 3     True
# 4    False
# 5    False
# 6     True
# 7    False

print(data.loc[(data['New'] == '+') & (data['Role'] == 'coder')]) 


term = (data['Role'] == 'coder') & (data['New'] == '+')
data.loc[term, 'New'] = '-'

game_survey.loc[game_survey['gender'] == 'None', 'gender'] = 'f'

## agg()
logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})
# purchase       
# source     count   sum        
# None        1674   108
# context    52032  3029
# email      12279   913
# other     133834  8041
# undef        181    12 


logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'unknown' 
print(logs['source'].value_counts())
# other      133834
# context     52032
# email       12279
# unknown      1674
# undef         181
# Name: source, dtype: int64

logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})
logs_grouped['conversion'] = (
    logs_grouped['purchase']['sum'] / logs_grouped['purchase']['count']
)
print(logs_grouped)
#         purchase       conversion
#            count   sum
# source
# context    52032  3029   0.058214
# email      13953  1021   0.073174
# other     133834  8041   0.060082
# undef        181    12   0.066298



# .read_excel()
df = pd.read_excel(
    '/datasets/eee.xlsx', sheet_name='1st'
) 
subcategory_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='subcategory_ids')

# to_numeric()
transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')

# astype()
df['col'] = df['col'].astype('int') # or not int. wherewer you want


data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
# total rows
print(f'Number of row: {data.shape[0]}')
# broken rows (2)
print(data.loc[data['subcategory_id'] == 'total'])

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
data = data[(data['subcategory_id'] != 'total')]
data['visits'] = data['visits'].astype('int')


# .to_datetime()
arrivals['date_datetime'] = pd.to_datetime(
    arrivals['date'], format='%d.%m.%YZ%H:%M:%S'
)
    # •	%d — day of the month (from 01 to 31)
	# •	%m — month number (from 01 to 12)
	# •	%Y — four-digit year (e.g., 2019)
	# •	Z — standard date and time separator
	# •	%H — hour number in 24-hour format
	# •	%I — hour number in 12-hour format
	# •	%M — minutes (from 00 to 59)
	# •	%S — seconds (from 00 to 59)

arrivals['month'] = pd.DatetimeIndex(arrivals['date_datetime']).month
# => num of the month

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(
    position['timestamp'], format='%Y-%m-%dT%H:%M:%S'
)
position['month'] = pd.DatetimeIndex(position['timestamp']).month
print(position.groupby('month')['level'].mean())
# month
# 2    1.750000
# 3    5.769231
# 4    6.214286
# Name: level, dtype: float64