dict = {1: "one", 2: "two"}
lst = [] 
for i in dict:
    lst.append({i:dict[i]})
print(lst)