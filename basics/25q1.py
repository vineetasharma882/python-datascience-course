#ques no 1
str= "Hii  am good"
print(str)

#ques no 2
str=input("Enter a string")
print(len(str))

#ques no 3
str="python is great"
st=str[-5:]
print(st)
for i in range((len(str)-1),0,-1):
    if str[i]==" ":
        print(st[::-1])
    else:
        st=st+str[i]

#ques no 4
str='python is everywhere'
print(*str.split(),sep='\n')

#ques no 5
str='Hello World!'
s=" "
for i in str:
    s=i+s
print(s)

#ques no 6
str="How are you?"
print(str.upper())

#ques no 7
str="How Is It Going?"
print(str.lower())

#ques no 8
words = ['Python', 'is', 'easy', 'to', 'learn']
print(" ".join(words))

#ques no 9
print("print multiline String \n using single print")
#or
data=""
while True:
    line=input()
    if not line:
        data+=line+'\n'
print(len(data),'chars')

#ques no 10
print("\\n")
print(r'\n')

#ques no 11
c=15
print("the variable is ",c)

#ques no 12
s1 = 'python '
s2 = 'is '
s3 = 'great.'
s=s1+s2+s3
print(s)

#ques no 13
b='#'
print(b*20)

#ques no14
for i in range(1,10):
    print(i,".")

#ques no 15
sentnce=input("enter the sentance : ")
print(*sentnce.split(),sep='\n')

#ques no 16
if sentnce[len(sentnce)-1]=='?':
    print("The entered strng has '?' in the end of the String")
else:
    print("The entered sentance does not have '?' in it. ")

#ques no 17
print(sentnce.count('e'))

#ques no 18
print(sentnce.isnumeric())

#ques no 19
text="    this is not a good String     "
sen=text.lstrip()
print(sen.rstrip())

#ques no 20
for i in sentnce:
    if i.isupper():
        print("Found")

#ques no 21
names = 'Joe, David, Mark, Tom, Chris, Robert'
l=[]
l=names.split(',')
print(l)

#ques no 22
text = 'this is some text'
a=text.split( )
a.insert(1,'aye')
a.insert(3,'aye')
a.insert(5,'aye')
a.insert(7,'aye')
print(a)

#ques no 23
str=input("enter string to check the 'fyi' in the string")
if "fyi" in str:
    print("yes , entered string have 'fyi' in the string")
else:
    print("No , entered string does not have 'fyi' in the string")

#ques no 24
text = '%p34@y!*-*!t68h#&on404'
from string import punctuation
for p in punctuation:
    text=text.replace(p,'')
print(text)

#ques no 25
str1="this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated"
w=str1.split()
print("number of words in the given string is",len(w))