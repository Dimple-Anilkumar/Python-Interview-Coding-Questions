a=input()
count=0
for ch in a.lower():
    if ch in "aeiou":
        count+=1
print(count)

