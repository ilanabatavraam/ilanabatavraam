	# 1.	Import the pandas library.
	# 2.	Read the CSV file 'music_log.csv' into a variable named df.
	# 3.	Rename the column names in df.
	# 4.	Declare a list columns_to_replace containing the column names: track, artist, genre.
	# 5.	Fill the missing values in the columns from the columns_to_replace list with the value 'unknown' using a loop.
	# 6.	Remove duplicate rows from the DataFrame df.
	# 7.	Print the first 20 rows of the updated dataset df.

import pandas as pd

df = pd.read_csv('music_log.csv')
df = df.rename(columns={'  user_id': 'user_id',
                       'total play': 'total_play',
                       'Artist': 'artist'})
columns_to_replace = ['track', 'artist', 'genre']
for col in columns_to_replace:
    df[col] = df[col].fillna('unknown')
df = df.drop_duplicates().reset_index(drop=True)
print(df.head(20))