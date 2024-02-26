###############################
###### Dictionary (dict) ######
###############################

# the key must be immutable data type
# the value can be any data type

dict1 = {
    "name" : "Mohamed" ,
    "age" : 22 ,
    "grades" : [1,2,3] ,
    "%" : 15.5 ,
    3 : 4 ,
    (5,6,7) : 8
}

print (dict1)
print(len(dict1))
print(dict1['name'])
print(dict1[3])
print(dict1["grades"][1])

print("="*40)
dict2 = {
    "one" : {
        "lang" : "English" ,
        "grade" : 10
    } ,
    "two" : {
        "lang" : "french" ,
        "grade" : 20
    } ,
    "three" : {
        "lang" : "deutsch" ,
        "grade" : 30
    }
}

print(dict2)
print(len(dict2))
print(len(dict2["three"]))
print(dict2["one"]['grade'])
print(dict2.keys())
print(dict2.values())

############### Methods ##################

print("======== clear =============")
d = {"name" : "Mohamed" , "age" : 22}
print(d)
d.clear()
print(d)

print("======== update =============")
d = {"name" : "Mohamed" , "age" : 22}
print(d)
d["job"] = "student"
print(d)
d.update({"lang" : "English"})
print(d)

print("======== copy (shallow) =============")
d = {"name" : "Mohamed" , "age" : 22}
c= d.copy()
print(d)
print(c)
d["job"] = "student"
print(d)
print(c)

print("======== setdefault =============")
d = {"name" : "Mohamed" }
print(d)
d.setdefault("age" , 11)
# d.setdefault("name" , "Student")
print(d)

print("======== popitem =============")
d = {"name" : "Mohamed" , "age" :13}
print(d)
print(d.popitem())
print(d)

print("======== items =============")
view = {
  "name": "Mansour",
  "lang": "English"
}

print(view)
allItems = view.items()
view["age"] = 36
print(view)
print(allItems)

print("======== fromkeys =============")
a = ('key_one', 'key_two', 'key_three')
b = "X","y"

print(dict.fromkeys(a, b))