from importlib.resources import path
from turtle import up


msg="we will be seeing the horizin"
words=msg.split()
print(words)

words=msg.split('e')
print(words)

#replace()
updated_msg=msg.replace('seeing','viewing')
print(updated_msg)

updated_msg=msg.replace('e','')
print(updated_msg)

#join()
path=['user','mypc','documents','data','files.txt']
content="/".join(path)
print(content)

#strip()
name="   hello steve     "
cleaned_name=name.strip()
print(cleaned_name)
print(len(name),len(cleaned_name))

#strip()
name=''' 

we are venom

'''
cleaned_name=name.strip()
print(cleaned_name)
print(len(name),len(cleaned_name))

from helper import read
data=read('pride_n_prejudice.xt')

#wap to find fequency of all the vowels in the 'data'

for vowel in 'aeiou':
    print(f"{vowel}=> {data.lower().count(vowel)} times")

#wap to remove all the punctuations frm he string
#Str= 'he@#ll%o!@ &*(!@wo!@r,l!d)'

str= 'he@#ll%o!@ &*(!@wo!@r,l!d)'
from string import punctuation
for p in punctuation:
    str=str.replace(p,'')
print(str)