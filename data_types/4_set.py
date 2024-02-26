#############################################
################ Lists ######################
#############################################

# Not Ordered And Not Indexed
set1 = {1,2,3,4,5}
print(set1)

# print(set1[0])    # Indexing Cant Be Done
# print(set1[0])    # Slicing Cant Be Done

# set1 = {1,2,3, {4,5,6}}
#set1 = {1,2,3, [4,5,6]}  #error: set contains Inimuutable data (data than i can't change it's conntent )
# remember i can't change Tubles connent : #Tuple[0] = 3 (error) , so set can't contain list or dict or set

set1 = {1,2,3, (4,5,6)}
print(set1)

print("====== Items are unique =======")
set1 = {1,2,3,3,"Ali"}
print(set1)

#########################
######## Methods ########
#########################

print("====== clear ========")
t1 = {1,2,3,4,5}
t1.clear()
print(t1)

print("====== remove ========")
t2 = {1,2,3,4,"Ali" ,4}
t2.remove(4)
print(t2)
# t2.remove(7)    #error : 7 doesn't exist

print("====== discard ========")
t2 = {1,2,3,4,"Ali" ,4}
t2.discard(4)
print(t2)
t2.discard(7)       # No error
print(t2)

print("====== add ========")
t2 = {1,2,3,4,"Ali" }
t2.add(158)
print(t2)

print("====== copy ========")
t2 = {1,2,3,4,"Ali" }
t3 = t2.copy()
print(t2)
print(t3)
t2.add(99)
print(t2)
print(t3)

print("====== union ========")
t2 = {1,2,3,4,"Ali" }
t3 = {17,18,15}
print(t2 | t3)
print(t2.union(t3))
print(t2)
t2.union(t3)
print(t2)
t2 = t2.union(t3)
print(t2)
t4 = {"a","b","c"}
print(t2.union(t3,t4))

print("====== update ========")
t2 = {1,2,3,4,"Ali" }
t3 = {17,18,15}
t2.update(t3)                   # unlike union 
print(t2)
# print(t2.update(t3))  #error
t4 = {"a","b","c"}
t2.update(t3,t4)                   # unlike union 
print(t2)

print("====== pop ========")
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())                      #pop random element (in list pop(index))

print("=============================")

print("======== difference =============")
a = {1,2,3,4,5}
b= {4,5}
print(a.difference(b))
print(a-b)
print(a)

a.difference(b)
print(a)
a= a.difference(b)
print(a)

print("======== difference_update =============")
a = {1,2,3,4,5}
b= {4,5}
a.difference_update(b)
print(a)

print("======== symmetric_difference =============")
a = {1,2,3,4,5}
b= {4,5}
print(a.symmetric_difference(b))
print(a)

print("======== symmetric_difference_update =============")
a = {1,2,3,4,5}
b= {4,5}
a.symmetric_difference_update(b)
print(a)

print("======== intersection =============")
a = {1,2,3,4,5}
b= {4,5}
print(a.intersection(b))
print(a)
print(a&b)
print(a)

print("======== intersection_update =============")
a = {1,2,3,4,5}
b= {4,5}
a.intersection_update(b)
print(a)

print("=============================")

print("======== issuperset =============")
a= {1,2,3,4,5}
b= {4,5}
print(a.issuperset(b)) #True

print("======== issubset =============")
a= {1,2,3,4,5}
b= {4,5}
print(b.issubset(a)) #True

print("======== isdisjoint =============")
a= {1,2,3,4,5}
b= {4,7}
print(b.isdisjoint(a)) #False
b= {8,7}
print(b.isdisjoint(a)) #True