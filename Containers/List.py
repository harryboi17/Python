li = [3,1,6,7,3,5]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

li.remove(3)
print("After remove :", li)
a = li.pop()
print("After pop :", a)

if 6 in li:
    print("Yes", 6, "is in list")

print("Lenght of list is :", len(li))
for i in range(len(li)):
    print(li[i], end = " ")
