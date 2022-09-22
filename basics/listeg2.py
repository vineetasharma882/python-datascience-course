books=['Stealheart','You can win','osmosis','calamity']
books.append('The Final empire')
books.append('Atomic Habit')
books.append('you can win')
books.append('three mstakes of my life')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books[6]="he well of Ascension" #update
books[-1] ='the hero of ages'
books[2]='Legion'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3,'Legion: skn deep')
books.insert(5,'Elantris')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

#books.remove('you can win')
#books.remove('Legion')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

#extend()
fruit=['apple','mango','banana','Cherry','Guava']
dry_fruits=['Almands','cashew','walnut']
fruit.extend(dry_fruits)
print(fruit)