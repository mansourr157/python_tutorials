#######################################
########## string formatting ##########
#######################################

###### old method ######
name = input("Enter ur name:").title().strip()
age = int(input("Enter ur age:"))
rank = float(input("Enter ur rank:"))

print("Hello %.3s , ur age is: %i and ur rank is: %.2f" %(name , age , rank)) 

###### new methods ######
print(f"Hello {name} , ur age is: {age} and ur rank is: {rank}")
print("*"*25)

print("Hello {} , ur age is: {} and ur rank is: {}".format(name, age, rank))
print("Hello {:s} , ur age is: {:d} and ur rank is: {:.3f}".format(name, age, rank))

print("*"*25)
money = 123456789
print("Money = {:,d}".format(money))
print("Money = {:_d}".format(money))

print("*"*25)
a,b,c = 1,2,3
print("{} , {} , {}".format(a,b,c))
print("{1} , {0} , {2}".format(a,b,c))
print("{2:d} , {1:d} , {0:.2f}".format(a,b,c))