list_99 =list( range(0,101))
d =[]
for i in list_99:
    if ("9" in str(i)):
          i*=2
          d.append(i)
      
         
print (str(d ) + str(len( d)))
print (d[-1])

for x in list_99:
    if ("7" in str(x)):
        list_99.remove(x)
print (list_99)