rg = int(input("Enter the range of list : "))
li = []
for i in range(rg) :
    val = int(input())
    li.insert(i,val)

for i in range(rg) :
    if(li[i]%2== 0):
        print(li[i], " is even")
    else:
        print(li[i], " is odd") 