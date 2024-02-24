# -----------
# -- Tuple --
# -----------
# [note] Tuple Are Immutable => You Cant Add or Delete

##### Syntax #####
str1 = ("Mansour")
str2 = "Mansour"
print(type(str1))
print(type(str2))

tuple1 = ("Mansour" ,)
tuple2 = "Mansour" ,
print(type(tuple1))
print(type(tuple2))
print(len(tuple1))      # 1

print("="*10)
tuple1 = (1,2,"three",4,5)
print(tuple1[0])
print(tuple1[2])
print("="*10)

tuple1 = (1,2,"three",4,5)
# tuple1[0] = 3                 #error : 'tuple' object does not support item assignment
# print(tuple1)

############ Methods #############
# Tuple Concatenation
a= (1,2,3)
b= (4,5,6)
print('='*20)
print(a + b)

# #Tuple, List , String repeat
# y= "="
# x= (1,2,3)
# z=["a","b"]
# print(x*5)
# print(y*5)
# print(z*5)
# print(y*20)

print("============== count =============")
tuple1 = (1,2,"three",4,5,9,4,4,4)
print(tuple1.count(4))
print(f"Thw count of 4 is: {tuple1.count(4)}")
print(tuple1.index(4))
print(f"Thw index of 4 is: {tuple1.index(4)}")

print("============== Destruct =============")
a,b,c = 1,2,3
print(f"a = {a}") 
print(f"b = {b}") 
print(f"c = {c}") 

print('='*20)

e= (7,8,9)
a,b,c = e
print(f"a = {a}") 
print(f"b = {b}") 
print(f"c = {c}") 

print('='*20)

f= (7,8,125,9)
a,b, _ ,c = f
print(f"a = {a}") 
print(f"b = {b}") 
print(f"c = {c}")
 
print('='*20)