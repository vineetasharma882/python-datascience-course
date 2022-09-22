from pprint import pp


movies={}
movies['Top Gun: Maverick']=8.3
movies['Everything Everywhere All at Once']=8.1
movies['Spider-Man: No Way Home']:8.2
pp(movies)

for i in movies:
    print(i)

print("Only values")
for i in movies:
    print(movies[i])

print("both values and key")
for key in movies:
    print(key,movies[key])

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)

#user input of dict
for i in range(3):
    name=input("Movies Name: ")
    rating=float(input('Movie Rating: '))
    movies[name]=rating

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)