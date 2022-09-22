x=[]
for i in range(4):
    n=(input('enter names'))
    x.append(n)

for i in x:
    print(i[::-1])

#Wap to print a fibonacci series using the concept of list(0,1,1,2,3,4,5,8,11....)

fibo=[0,1]
for i in range(10):
    fibo.append(fibo[-1]+fibo[-2])
print(fibo)

#Wap o generate a new list that contains squares if each number from existing list
#eg x=[2,3,4,5]=[4,8,16,25]
x=[2,3,4,5]
for i in x:
    print(i*i)

#or
x=[2,3,4,5]
x2=[]
for i in x:
    x2.append(i**2)

# 4
x=[1,2,3,4,5,6,7]
xodd=[]
for i in x:
    if i%2!=0:
        xodd.append(i)

print(xodd)

#add 2 list elementwise
x = [1,2,3,4,5,6]
y = [6,4,3,2,1,2]
z = []

for i,j in zip(x,y):
    z.append(i + j)
print(x)   
print(y) 
print(z)
