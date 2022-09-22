A={1,2,3,4,5}
B={4,5,6,7,8}
#union Operator we use (|) symbol
print(A|B)
#or
print(A.union(B)) 
#or
print(B.union(A))

#Intersection operator we use (&) symbol
print(A&B)
#or
print(A.intersection(B))

#set difference we use (-) symbol
print(A-B)
print(B-A)
print(A.difference(B))

#set Symaric Difference we use (^) symbol
print(A^B)
print(A.symmetric_difference(B))
