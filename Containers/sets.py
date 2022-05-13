myset = {"CSK", "MI", "RCB", "GT"}
print(myset)
print("The lenght of set is :", len(myset))

print("Checking membership : ")
print("RCB" in myset)
print("RR" in myset)

myset.add("SRH") #rando0m addition at any idx
print("After addition :", myset)

myset2 = {"LSG", "RR", "DC"}
myset.update(myset2)
print("After adding to sets :", myset)

set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}

c = set1.union(set2) #use set1.union_update(set2)
                     #to prevent making new set
print("Union of sets : ", c)

d = set1.intersection(set2) #.intersection_update
print("After intersection :", d)

e = set1.symmetric_difference(set2)#.symmetric_difference_update
print("After Symmetric Diff :", e)

set1.remove(2)
set1.discard(6) #doesn't throw error is element doesnt exists
f = set1.pop()

print("After removal : ", set1)
print("removed element : ", f)
