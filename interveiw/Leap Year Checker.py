def leap_year(n):
    if n % 400 ==0:
        return"Leap year"
    elif n % 4==0:
        return"Leap year"
    elif n % 100!=0:
        return"not leap year"
    else:
        return ("not leap year")
print(leap_year(2024))
