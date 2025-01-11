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

#read_csv() to open csv

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