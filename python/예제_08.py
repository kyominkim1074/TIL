#before
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)

#after
#1
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)

#2
word = "HappyHacking"

count = 0

for char in word:
    if char == "a":
        count += 1
    elif char == "e":
        count += 1
    elif char == "i":
        count += 1
    elif char == "o":
        count += 1
    elif char == "u":
        count += 1
        
print(count)