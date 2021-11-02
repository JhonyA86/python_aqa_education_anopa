mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
print(mylist[-1])  # prints 3
print(mylist[-2])  # prints 2
print(mylist[-3])  # prints 1


for x in mylist:
    print(x)


mylist = [2, 4, 6, 8, 10]
print(mylist[:3])
print(mylist[3:])

#  Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
