from helper import read

data = read('pride_n_prejudice.txt')

print(len(data))

newData = data[3:53]
print(newData)

# ...
#  formatting functions
# -lower
# -uppar
# -swapcase
# -capitalize
# -title
# -casefold


# -ljust
# -rjust
# -center
# ...

print(newData.lower())
print(newData.upper())
print(newData.swapcase())
print(newData.capitalize())
print(newData.title())
print(newData.casefold())

word='Hello'
spacing=20
ljust=word.ljust(spacing,'*')
print(ljust)
rjust=word.rjust(spacing,'-')
print(rjust)
cen=word.center(spacing,'😒')
print(cen)

#validation functions - either true or false
print(newData.isupper())
print(newData.islower())
print(newData.isalpha())
print(newData.isnumeric())
print(newData.isalnum())

#utility functions
idx=newData.find("pride")
if idx==-1:
    print('not found')   
else:
    print(f'Pride is found at index{idx}')

idx2=data.index("in")
print(f'in is found at index {idx2}')

start_idx=(0)
for i in range(5):
    idx3=data.find('in',start_idx)
    print(f'in is found at {idx3}')
    start_idx=idx3+1
num_of_in=data.count('in')
print(f'in occurse {num_of_in} times') 
