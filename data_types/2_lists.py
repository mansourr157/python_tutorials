#############################################
################ Lists ######################
#############################################

list1 = [1,2,3,"four","five" ,6.0,True]
print(list1)
print(list1[0])
print(list1[3])
print(type(list1[0]))
print(type(list1[3]))
print(list1[-1])
print(list1[-3])
print(list1[:])
print(list1[1:])
print(list1[:-1])
print(list1[::2])

print("=========")
list1[0] = 10
print(list1)
list1[0:2] = ["one" , "two"]
print(list1)
list1[0:3] = [1, 2]
print(list1)

print("\n======================\n")

#####################################################
################ Lists Methods ######################
#####################################################

print("\n========= append =========\n")
list1 = ["one" , 'two' , 3,4,5]
print(list1)
list1.append(6)
print(list1)

list2 = [7,8,9]
list1.append(list2)
print(list1)
print(list1[5])
print(list1[6])
print(list1[6][1])

print("\n========= extend =========\n")
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
list1.extend(list2)
print(list1)

print("\n========= insert =========\n")
list1 = [4,6,8,1,5,3,2,7]
list1.insert(0,"a")
print(list1)

print("\n========= clear =========\n")
list1 = [1,2,3,4,5]
list1.clear()
print(list1)

print("\n========= remove =========\n")
list1 = [1,2,3,"Mansour",4,5,"Mansour","Mansour"]
list1.remove("Mansour")
print(list1)

print("\n========= sort =========\n")
list1 = [4,6,8,1,5,3,2,7]
list1.sort()
list1.sort(reverse = False)
print(list1)
list1.sort(reverse = True)
print(list1)

print("\n========= reverse =========\n")
list1 = [4,6,8,1,5,3,2,7]
list1.reverse()
print(list1)

print("\n========= copy (shallow) =========\n")
list1 = [4,6,8,1,5,3,2,7]
list2 = list1.copy()
list1.append(157)
print(list1)
print(list2)

#################################################### inside print
print("\n========= pop =========\n")
list1 = [1,2,3,"Mansour",4,5,"Mansour","Mansour"]
print(list1.pop(-1))  #Mansour

print("\n========= count =========\n")
list1 = [4,6,8,1,5,3,2,7,6,6]
print(list1.count(6))

print("\n========= index =========\n")
list1 = [4,6,8,1,5,3,2,7,6,6]
print(list1.index(6))
