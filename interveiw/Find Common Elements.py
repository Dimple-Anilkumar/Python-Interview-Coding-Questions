a=[1,2,3,4,5,6]
b=[2,3,4,5,6,7]
new=[]
for i in a:
    if i in b:
        new.append(i)
print(new)