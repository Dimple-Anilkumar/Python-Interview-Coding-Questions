a=[1,2,3,4,5,6,7,8]
new=[]
def even_num(a):
    for i in a:
      if i %2 ==0:
            new.append(i)
    return new
print(even_num(a))
    
