# default parameter mus come after required parameter
def total(a,b=3,c=0):
    return a+b+c



#named parameter must come after positonal parameter
print(total(5))
print(total(a=5))

print(total(100,50))
print(total(a=100,b=50))
print(total(b=50,a=100))# Swapped and working

print(total(10,10,10))
print(total(a=10,b=10,c=10))
print(total(a=10,c=10,b=10))
print(total(10,c=10,b=10))
