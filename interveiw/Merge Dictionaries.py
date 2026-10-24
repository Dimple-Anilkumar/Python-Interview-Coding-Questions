a = {"x": 10, "y": 20}
b = {"y": 30, "z": 40}
result={}
for keys , values in a.items():
    result[keys]=values
for keys , values in b.items():
    if keys in result:
        result[keys]=result[keys]+values
    else:
        result[keys]=values
print(result)