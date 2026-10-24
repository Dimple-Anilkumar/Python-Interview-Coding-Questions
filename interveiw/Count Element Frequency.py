a=[1,2,3,4,3,4,5,2,4,5,3,2]
n=int(input())
def frec_of(a):
    frequency=0
    for i in a:
        if i==n:
            frequency+=1
    return frequency
print(frec_of(a))