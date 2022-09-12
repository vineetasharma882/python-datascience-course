from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase, ascii_uppercase

for letter in ascii_lowercase:
    counter =data.count(letter)
    print(f'{letter} found {counter} times')

for letter in ascii_uppercase:
    counter =data.count(letter)
    print(f'{letter} found {counter} times')

# wap to find the most accuring alphabet and its frequency