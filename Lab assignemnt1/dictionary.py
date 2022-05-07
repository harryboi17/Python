dict = {"Roll no" : 1,
        "Name" : "Harshit Bansal",
        "Branch" : "Computer Science"}

# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())

dict["marks"] = 10
print(dict)

dict.update({"marks": 20})
print(dict)

x = dict.pop("marks")
print(x)

y = dict.popitem()
print(y)

del dict["Name"]
print(dict)

for x,y in dict.items():
  print(x,":",y)