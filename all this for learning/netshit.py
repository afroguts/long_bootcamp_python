#trying r0bot shit ahah

from cmath import inf


print("hello welcome to the coffe shop!")

name = input("what is your name?\n")

if name == "hadman" or name == "hamid" or name == "loki":
        state = input("are you evil?\n")
        if state == "yes":
         print("get out of here " + name + "! and don't come back again")
         exit()
        else:
            print("welcome homie!")
else: 
    print("welcome %s" % name .upper())




foodlist = []

foodlist.append("coffe")
foodlist.append("latte")
foodlist.append("ice")
foodlist.append("coke")

print("you can choose your drink : " .upper())

for x in foodlist:
    print(x)

order = input()


price = 8 
#if order == "coffe":
   # price = int(4)
#else:
    #if order == "latte":
       # price = int(2)
   # else:                        this is the old long way did it by myself
       # if order == "ice":
         #   price == int(1)
     #   else:
          #  if order == "coke":
           #     price = int(3)
           # else:
           #   print("wrong order, please try again")
            #  exit()

#the tuto way now
if order == "coffe":
    price = 2
elif order == "latte":
    price = 3
    webcream = input("do you want extra webcream?\n")
    if webcream == "yes":
        price = 8
    else:
        price= 3

elif order == "ice":
    price = 4
elif order == "coke":
    price = 5
else:
    print("wrong order, sorry,we don't have that here")             
    exit()
     
            






quantity = input("how much would you like ?\n")

total = price * int(quantity)

print("your total cost is : " + str(total) )

print("looks good " .upper() + name + " we will get you your " .upper() + str(quantity) + " " + order + " in a moment." .upper())

