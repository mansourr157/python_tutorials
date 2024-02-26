##################################
######## string methods ##########
##################################

###### indexing and slicing #########
str1 = "Mansour"
print(str1)
print(str1[0])
print(str1[-1])
print(str1[:])
print(str1[:3])
print(str1[::2])
print(str1[::-1])

print("*"*50)
print(len(str1))

print("========== strip ============")
st = "  Mansour   "
print(st.strip())
print(st.lstrip())
print(st.rstrip())
print("*"*20)
st = "###$$$  Mansour ###$$"
print(st.strip("#$ "))

print("========== title ============")  # the first char in each word capital 3d=>3D
st = "mY NaME iS MoHaMeD 3d"
print(st.title())
st.title()
print(st)
st = st.title()
print(st)

print("========== capitalize ============") # the first char in the sentence capital
st = "mY NaME iS MoHaMeD 3d"
print(st.capitalize())
st.capitalize()
print(st)
st = st.capitalize()
print(st)

print("========== upper ============") # the all chars are capital
st = "mY NaME iS MoHaMeD 3d"
print(st.upper())
st.upper()
print(st)
st = st.upper()
print(st)

print("========== lower ============") # the all chars are small
st = "mY NaME iS MoHaMeD 3d"
print(st.lower())
st.lower()
print(st)
st = st.lower()
print(st)

print("========== swapcase ============") # change the case of the characters
st = "mY NaME iS MoHaMeD 3d"
print(st.swapcase())
st.swapcase()
print(st)
st = st.swapcase()
print(st)

print("========== zfill ============")
a,b,c = "1","11","111"
print(a)
print(b)
print(c)
print("******")
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

print("========== index ============")
st = "my name is Mohamed Mansour"
print(st.index("n"))
print(st.index("n" ,0 ,9 ))
# print(st.index("d" ,0 ,9 ))  # error

print("========== find ============")
st = "my name is Mohamed Mansour"
print(st.find("n"))
print(st.find("n" ,0 ,9 ))
print(st.find("d" ,0 ,9 ))  # No error  (-1)

print("========== count ============")
st = "i love Clopp because Clopp is a great manager "
print(st.count("Clopp"))
print(st.count("Clopp" ,0 ,12 ))

print("========== startswith ============")
st = "i love Clopp because Clopp is a great manager "
print(st.startswith("i"))
print(st.startswith("C" ,7 ,12 ))

print("========== endswith ============")
st = "i love Clopp because Clopp is a great manager"
print(st.endswith("r"))
print(st.endswith("e" ,0 ,6 ))

print("========== center ============")
st = "Mansour"
print(st.center(11 ))
print(st.center(13 , "$"))
print(st.center(13 , "%"))

print("========== split & rsplit ============")
st = "my name is Mohamed Mansour"
print(st.split())
st = "my-name-is-Mohamed-Mansour"
print(st.split())
st = "my-name-is-Mohamed-Mansour"
print(st.split("-"))
print(st.split("-" , 2))
print("*"*20)
print(st.rsplit("-" , 2))

print("========== rjust ============")
st = "Mansour"
print(st.rjust(9))
print(st.rjust(11 , "#"))

print("========== ljust ============")
st = "Mansour"
print(st.ljust(9))
print(st.ljust(11 , "#"))

print("========== splitlines ============")
st = '''line1
line2
line3'''
print(st.splitlines())
print(type(st.splitlines()))
st = "line1\nline2\nline3"
print(st.splitlines())

print("========== expandtabs ============")
st = "txt1\ttxt2\ttxt3"
print(st.expandtabs(2))
print(st.expandtabs(20))

print("========== replace ============")
st = "one two three one two three"
print(st.replace("one" , "1"))
print(st.replace("one" , "1" , 1))
print(st.replace("one" , "1" , 2))

print("========== join ============")
list1 = ["one", "two", "three" ]
print("".join(list1))
print(" ".join(list1))
print("-".join(list1))
print(type("-".join(list1)))

print("*"*30 + "\n" + "*"*30)
print("========== booleans ============")

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())