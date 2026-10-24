a=input()
b=input()
def is_anagram(a,b):
    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()
    return sorted(a)==sorted(b)
print(is_anagram(a,b))