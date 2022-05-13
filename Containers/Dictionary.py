d1 = {"Roll no" : 16,
      "Name" : "XYZ",
      "Branch" : "CS"}

print("Dictionary :", d1)
print("Printing Individual modules :", d1["Branch"])

d1["Phone No"] = 123456
d1["Country"] = "India"
print("Dictionary after adding :", d1)

keys = d1.keys()
values = d1.values()
items = d1.items()

print("Keys : ", keys)
print("Values : ", values)
print("Items : ", items)

d1.update({"Phone No" : 98765})
print("After update : ", d1)

x = d1.pop("Branch")
print("Poped item :", x)

y = d1.popitem()
print("Last Item poped : ", y)

#del d1["Roll No"]
#d1.clear() clear the whole dictonary

for i in d1:
    print(i, d1[i], ",", end = " ")
print()
for x,y in d1.items():
    print(x, y, ",", end = " ")

