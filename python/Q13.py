# for loop
word="apple"
re=''
for i in word:
    re=i+re
print(re)

# slice를 이용한 경우
word="apple"
re=word[::-1]
print(re)

# reserved를 이용한 경우
word="apple"
re=''.join(reversed(word))
print(re)