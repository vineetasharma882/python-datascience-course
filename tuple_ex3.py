#tuple-et-lit(interchange)
x=[1,2,3,4,5,5,6,6,7]
xt=tuple(x)#list to tuple
xl=list(xt)#tuple to list
xs=set(x)#list to set
xl=list(xs)#set to list
xs=set(xt)#tuple to list
xt=tuple(xs)#set to tuple


#Wap to creae a tuple , by taking inputs from user

z=[]
for i in range(10):
    n=input("enter the tuple eements")
    z.append(n)

xz=tuple(z)
print(xz)