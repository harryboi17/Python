rg = int(input("Enter the range of list : "))
li = []
for i in range(rg) :
    val = int(input())
    li.insert(i,val)

flag = True
for i in range(rg-1):
    if(li[i] > li[i+1]):
        flag = False

if(flag):
    print("Yes")
else:
    print("No")

