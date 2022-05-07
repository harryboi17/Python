li1=[]
li2=[]

l1 = int(input("Enter length of list one : "))
l2 = int(input("Enter length of list two : "))

for i in range(l1) :
    val = int(input())
    li1.append(val)
for i in range(l2) :
    val = int(input())
    li2.append(val)

li1 = li1+li2
print(li1)
