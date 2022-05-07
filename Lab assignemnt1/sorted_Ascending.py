my_list = [1,2,3,4]
flag = True
lent = len(my_list)
for i in range(lent-1):
    if(my_list[i] > my_list[i+1]):
        flag = False

if(flag):
    print("Yes")
else:
    print("No")