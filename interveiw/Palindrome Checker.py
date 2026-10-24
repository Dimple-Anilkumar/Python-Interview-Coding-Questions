a=input()
def is_palindrome(a):
    if a == a[::-1]:
        return "yes"
    else:
        return "no"
print(is_palindrome(a))