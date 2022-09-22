x=[1,2,3,1,2,3,4,1,2,3,2,1,3,4,1,2,3]
x_one=x.count(1)
x_two=x.count(2)
x_four=x.count(4)
x_three=x.count(1)
print('1 occurred',x_one,'times')
print('2 occurred',x_two,'times')
print('3 occurred',x_three,'times')
print('4 occurred',x_four,'times')

# extend
y=[12,13,41,65]
z=[66,77,432]
print('x addng y')
x.extend(y)
print(x)
print('x addng z')
x.extend(z)
print(x)

# pop
xyz=x+y+z
print(xyz)
a=['appe','mango','banana','elaich']
v=a.pop(3)
print(a)
print(v)
lv=a.pop()
print(a)
print(lv)