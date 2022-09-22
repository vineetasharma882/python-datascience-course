#Add 10 items n a list using user input

x=[]
y=0
for i in range(10):
    n=float(input('enter item in the list'))
    x.append(n)

print('the value entered is')
print(x) 

for i in range(10):
    y=y+x[i]

mean=y/10
print("mean is- ",mean)

if len(x)/2==0:
    median=(y+1)/2
    print("Median is- ",median)

else:
    median=((y/2)+((y/2)+1))/2
    print("Median is- ",median)

