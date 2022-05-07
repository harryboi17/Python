li = []
rg = int(input("Enter the range "))
for i in range(rg):
    val  = int(input())
    li.append(val)

print(li)
li[0],li[rg-1] = li[rg-1],li[0]
print(li)