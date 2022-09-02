from email import message
from re import S
from this import d, s


remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)


name = "hello man"
age = 20
rank = 5
print("the message is %s my age is %d" % (name,age))
print("the message is {:s} my age is {:d} my rank is {:.2f}" .format(name,age,rank))

a, b, c = "one", " two", "three"

print("hello {1} {0} {2}".format(a ,b ,c )) #nbdlo tartib 

x, y, z = 2, 4, 5
print("hello {1:d} {0:.1f} {2:.2f}".format(x ,y ,z )) #for floating shitt

nameee = "osama"
ageee = 26

print("my name is : {nameee} and my age is : {ageee}")
print(f"my name is : {nameee} and my age is : {ageee}".upper() )

