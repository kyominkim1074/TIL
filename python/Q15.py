##15
#1
word = 'banana'
a = 0
for i in word:
    if i == 'a':
        break
    a+=1
else:
    a=-1
print(a)
#2
word = 'apple'
a = 0
for i in word:
    if i == 'a':
        break
    a+=1
else:
    a=-1
print(a)
#3
word = 'kiwi'
a = 0
for i in word:
    if i == 'a':
        break
    a+=1
else:
    a=-1
print(a)

##15-1
#1
word = 'HappyHacking'

for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')

#2
word = 'banana'
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')

#3
word = 'kiwi'
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')