myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'Nix'
print(mystring)
mystring = "hello"
print(mystring)

a, b, c = 3, 4, 5
print(c // b)

# Exercise
mystring = "Nix"
myfloat = 10.0
myint = 20


if mystring == "Nix":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
