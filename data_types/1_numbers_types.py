#####################
###### Numbers ######
#####################

###### int ######
print(type(10))
print(type(-10))

###### float ######
print(type(10.0))
print(type(-10.2))
print(type(-0.2))

###### complex number ######
my_complex_number = 5+6j
print(type(my_complex_number))
print(f"real part is: {my_complex_number.real} and imaginary part is: {my_complex_number.imag}")

# u can convert int or float into complex but u can't convert complex to int or float
print(100)
print(float(100))
print(complex(100))
print("\n")

print(100.2)
print(int(100.2))
print(complex(100.3))
print("\n")

print(100.2+3j)
# print(int(100.2+3j))          #wrong
# print(float(100.2+3j))        #wrong
