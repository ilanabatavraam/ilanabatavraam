# In this file Im gonna record very first knowelege about this language. In my experience, I used to work with JavaScript, so here is just small notes from the couse. Just to remember :)

print(1,2,3, str='***')

try:
    print(1/0)
except:
    print('dividing on zero!')

# to recognise the type
print(type(your_var)) 

# int() — 3.0 => 3;
# float() — 3 => 3.0;
# str() — to string
cz_total_speakers = 10.6
cz_total_speakers = int(cz_total_speakers)
print(cz_total_speakers)

fra_total_speakers = '284.9'
fra_total_speakers = float(fra_total_speakers)
print(fra_total_speakers)

# +=, -=, *=, /=
var = 1
var = var + 1
var += 1

# \n new line
phrase = 'I don\'t want to stop'

# lenght of the string
print(len('No pain no gain!'))

multiline_string = """one
two
three!"""
print(multiline_string)

# index
word = 'chargoggagoggmanchauggagoggchaubunagungamaugg'
letter = word[8]
print(letter)

password = 'qwerty'
print(password[0:3])

# it works in python lol
print('lol' * 5)
print(3 * 'ha')
print('lol\n' * 5)

# replace() — replaces part of the string.;
# find() — searches for a substring in a string;
# upper() — replaces all letters in the string with uppercase letters.;
# lower() — replaces all letters with lowercase letters.
some_string = 'leaving'
some_string = some_string.replace('leav', 'stay') 
print(some_string)

# shows only the first index
word = 'hey, hello, hello, hello, how low?'
ind = word.find('hello')
print(ind)
# we can ask where to find
ind = word.find('hello', 15, 25)

# if find nothing it comes with -1

word = 'AbRacaDABRA'
lower_word = word.lower()
upper_word = word.upper()
print(lower_word, upper_word)

# F string
name = 'John'
age = 30
height = 173.5
introduction = f'Hello, this is {name}, he is {age}, his height is {height}'
print(introduction)
print(type(introduction))

# OR OLD
introduction = 'Hello, this is {0}, he is {1}, his height is {2}'.format(name, age, height)
print(introduction)

# lists
list = []
var_list = list.append(1)
var_list = list.extend([1, 2, 3])
var_list = list.insert(2, 3333) # to add to index 2
var_list = list.insert(len(list), 123) # to add to the end

list.pop() # to remove the last element

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1979, 1985]
years.sort()
print(years) 
[1962, 1966, 1972, 1979, 1985, 1993, 1994, 1994, 1999, 2003, 2008] 
years.sort(reverse=True) 

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]
movies_duration_sorted = sorted(movies_duration, reverse=True)

# .split() str => list
# .join() list => str
stations = ['a', 'b', 'c', 'd']
info = '>'.join(stations) 
print(info)
'a>b>c>d'

years = [1994, 1972, 2008, 1993]
for year in years:
    print(year) 
    print('*' * 20)

prices = [1500, 2999, 7499, 3220]
for i in range(len(prices)):
    prices[i] -= 1000
print(prices)

# counter
movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]
total_duration = 0
for duration in movies_duration:
    total_duration += duration

print(total_duration)


movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]
total_duration = sum(movies_duration)
print(total_duration)

# import math
# sum() +
# prod() *
# max()
# min()
# factorial()

# factorial
number = 8
fact = 1 
for i in range(1, number + 1):
    fact *= i
print(fact)

# how to print a table
for row in movies_table: 
    for elem in row: 
        print(elem, end='   ')
    print() 

lambda row: row[5]
movies_table_sorted = sorted(movies_table, key=lambda row: row[5], reverse=True)

# islower() true/false
# isdigit()
# isalpha()

for i in items:
while total_weight < capacity:

# functions
def omelet(eggs_number = 1):
    result = str(eggs_number) + ' omelets'
    return result 


def get_hours_and_minutes(time_string):
    return int(time_string.split(':')[0]), int(time_string.split(':')[1])

time_str = '12:35'
hours, minutes = get_hours_and_minutes(time_str)
print(hours, minutes)




def get_minutes_and_seconds(time_string):
    time_list = time_string.split(':')
    m = int(time_list[0])
    s = int(time_list[1])
    return m, s

def check_song_duration(time_string):
    return (get_minutes_and_seconds(time_string)[0] * 60) + get_minutes_and_seconds(time_string)[1] <= 210

print(check_song_duration('4:35'))
print(check_song_duration('2:10'))


financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Microsoft': 213.67,
    'Walmart': 130.68 
} 
coca_cola_price = financial_info['Coca-Cola'] 
print(coca_cola_price)

try:
    pepsi_price = financial_info['Pepsi']
    print(pepsi_price)
except:
    print('Ключ Pepsi отсутствует!')

nike_price = financial_info.get('Nike')
print(nike_price)


game_scores = {
    'A': [23, 35, 70, 45],
    'B': [38, 72, 65, 80],
    'C': [30, 35, 90, 73],
    'D': [45, 20, 95, 80]
}

for person, points in game_scores.items(): 
    total_points = sum(points)
    print(f'{person} - {total_points}') 


# to print dict + loops as a table
from json import dumps
# indent for gaps
# ensure_ascii for ru
print(dumps(filtered_order, indent=4, ensure_ascii=False))


nba_players = {
    'a': [2191, 2818, 2335],
    'b': [2251, 1505, 1698],
    'c': [1962, 2067, 2009],
}
for p in nba_players:
    summ = 0
    for i in nba_players[p]:
        summ += i
    avg = summ / len(nba_players[p])
    print(f'{p} {int(avg)}')

# OR

for player, score in nba_players.items():
    avg = int(sum(score) / len(nba_players[player]))
    print(f'{player} {avg}')


tracklist = [
    {
        'title': 'Stronger', # название трека
        'artist': 'Saimoo', # исполнитель
        'duration': 145, # продолжительность (в секундах)
        'genre': 'Deep House', # жанр
    },
    {
        'title': 'Alors On Danse',
        'artist': 'Stromae',
        'duration': 205,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Don\'t Be So Shy',
        'artist': 'Imany (Filatov & Karas Remix)',
        'duration': 190,
        'genre': 'Deep House',
    },
    {
        'title': 'Off My Mind',
        'artist': 'Matvey Emerson',
        'duration': 130,
        'genre': 'Deep House',
    },
    {
        'title': 'Now You\'re Gone',
        'artist': 'Basshunter',
        'duration': 154,
        'genre': 'Eurodance',
    },
    {
        'title': 'It Was A Good Day',
        'artist': 'Ice Cube',
        'duration': 260,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Diva',
        'artist': 'Beyonce',
        'duration': 200,
        'genre': 'Hip-Hop',
    }
]

hip_hop_duration = 0

for track in tracklist:
    if track['genre'] == 'Hip-Hop':
        hip_hop_duration += track['duration']

print(hip_hop_duration)

deep_house_tracklist = []

for i in tracklist:
    if i['genre'] == 'Deep House':
        deep_house_tracklist.append(i)

for track in deep_house_tracklist:
    print(dumps(track, indent=4))