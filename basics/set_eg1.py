my_Set={1,3,4,2,6,78,5}
print(my_Set)

my_set=set([1,2,3,4])
print(my_set)
#my_Set={1,2,[3,4]}#error because in set we can not enter a list because is is immutable 
#print(my_Set)

my_Set={1,3}
print(my_Set)
my_Set.add(2)#we use add to enter single value at a time
print(my_Set)
my_Set.update([2,3,4])#we use update to enter multiple values in a set
print(my_Set)
my_Set.update([4,5],{1,2,3})
print(my_Set)

#remove
my_Set={1,2,4,5,6}
print(my_Set)
my_Set.remove(6)
#discard
print(my_Set)
my_Set.discard(4)#same as remove
#pop
print(my_Set)
my_Set.pop()
print(my_Set)
#Clear
my_Set.clear()
print(my_Set)