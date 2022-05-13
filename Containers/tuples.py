tup = ("ABC", "XYZ", "PQR")
print(tup)

li = list(tup)
tup2 = tuple(li)
print("List converted tuple :", li)
print("Tuple converted list :", tup2)

li.append("NEW_ADD")
tup3 = tuple(li)
tup = tup + tup3
print("Merged tuples :", tup)

li.remove("ABC")
s1 = li.pop() #pops last element
s2 = li.pop(1)

print("poped element =", s1)
print("Index poped element =", s2)
print("Remaining List :", li)

if "XYZ" in tup: #check membership
    print("YES XYZ is in Tuple")