for i in range(100):
    print(i,end=" ")

#from a num to a num
for i in range(10,21):  
    print(i,end=" X ")

#gap
for i in range(1,11,2):
    print(i,end=' ^ ')
#reverse loop
for i in range(10,0,-1):
    print(i,end=' ')

# print("")
# data=[1,2,3,4,5,6,7,8,9]
# for i,d in enumerate(data):
#     print(i,d)

data=[1,2,3,4,5,6,7,8,9]
for i in enumerate(data):
    print(i)

names=['apple','banana','mango']
price=['10','20','30']
for n,p in zip(names,price):
    print(f'{n}=>${p}')
