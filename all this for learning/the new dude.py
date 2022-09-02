from typing import Dict


a = [1,2,3,4,5,6,7,]
n = 4



for i in range(0 , n):
    print(i)


print(a)

numbers_100 = range (0 , 100)


for i in numbers_100:
    if i == 99:
     print(i)


d={}
d["hamid"]= 20
d["ahmed"]= 17
d["hiba"]= 15
d["hind"]= 16

name = input("the student name ?\n")
#print (d.get(name))   ez way to do it if the name entred does not exist it prints none we can programe it to say somethin else instade of non / print(d.get(name , "student name does not exist"))
print(d.get(name , "student name does not exist"))  #one line of code can replace all of that shit
print(d.pop("hind")) # to remove something from the dictionary == del d["hind"]
print(d)
if name in d :
    print ("the student mark is : " + str(d[name]))
    
else:
   print("sorry the name does not exist")
   exit()





