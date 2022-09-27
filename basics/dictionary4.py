import helper as h
from string import punctuation

data=h.read('basics/pride_n_prejudice.txt')
print(len(data))

#remove punctuatin
for p in punctuation:
    data=data.replace(p,'')

#split into words
words=[word.strip() for word in data.lower().split()]

print("TOTAl WORDS FOUND: ",len(words))
print("UNIQUE WORDSFOUND: ",len(set(words)))

#create a dictionary
wc={}
#for word in set(words):
#    wc[word]=words.count(word)

#or
for word in set(words):
    if word in wc:
        wc[word]+=1
    else:
        wc[word]=1


#sorting the dict
wc=sorted(wc.items(),key=lambda x:x[1],reverse=True)
#first 10 words
for i in range(10):
    print(wc[i])