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