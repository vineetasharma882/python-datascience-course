from tkinter.font import names


a={i:i*i for i in range(6)}
print(a)

a={5,6,7,8}
b={7,8,9,10}
#print(len(a+b)) # prints error , TypeError: unsupported operand type(s) for +: 'set' and 'set'

a=[13,56,17]
a.append([87])
a.extend([45,67])
print(a)

d={"john":40,"peter":45}
print(list(d.keys()))

names1=['Amir','Bala','Chales']
if 'amir' in names1:
    print(1)
else:
    print(2)

nums=set([1,1,2,3,3,3,4,4])
print(len(nums))


a={1:"A",2: "B",3: "C"} 
for i,j in a.items():
    print(i,j, end=" ")

print("ab\tcd\tef".expandtabs())

print("Welcome to Python".split())

print("abc. DEF".capitalize())

#galat
print("Hello (0) and (1)".format('foo', 'bin'))

l1=[1,3,2]
print(l1*2)

a=(1,2, (4,5))
b=(1,2, (3,4))
print(a<b)

print('{0:.2}'.format(1/3))

total={}
def insert(items):
    if items in total:
         total [items] += 1
    else:
        total[items] =1
insert('Apple')
insert('Ball')
insert('Apple')
print (len(total))

s='digipodium' 
slice=s[4: len(s)] 
print(slice)

a=(2,3,1,5)
#a.sort() Error ,AttributeError: 'tuple' object has no attribute 'sort'
print(a)

#galat
listex =[3,4,5,20,5,25,1,3]
listex.pop(1)
print(listex)

a=(1,2,3)
b=('A','B','C')
c=tuple(zip(a,b))
print(c)

