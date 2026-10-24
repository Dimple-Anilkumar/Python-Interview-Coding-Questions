a=input()
for ch in a.lower():
    if ch not in "aeiou":
        print(ch, end="")