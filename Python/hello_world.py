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