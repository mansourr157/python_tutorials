# ---------------------
# -- Type Conversion --
# ----------------------

# str()

a = 15
print(a)
print(type(a))
print(str(a))
print(type(str(a)))
print("*"*25)

# tuple()
a = "Mansour"  # String
b = [1, 2, 3, 4, 5]  # List
c = {"A", "B", "C"}  # Set
d = {"A": 1, "B": 2}  # Dictionary

print(tuple(a))
print(tuple(b))
print(tuple(c))
print(tuple(d))
print("*"*25)

# list()
a = "Mansour"  # String
b = (1, 2, 3, 4, 5)  # tuple
c = {"A", "B", "C"}  # Set
d = {"A": 1, "B": 2}  # Dictionary

print(list(b))
print(list(a))
print(list(c))
print(list(d))
print("*"*25)

# set()
a = "Mansour"  # String
b = [1, 2, 3, 4, 5]  # List
c = ("A", "B", "C")  # tuple
d = {"A": 1, "B": 2}  # Dictionary

print(set(b))
print(set(a))
print(set(c))
print(set(d))
print("*"*25)

# dict()
b = [[1, 2], [3, 4]]  # List
c = ( ("A", "B"), ("C","D"))  # tuple

print(dict(b))
print(dict(c))
print("*"*25)
