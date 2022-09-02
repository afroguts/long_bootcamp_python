#Write a Python function with the name "en_filter" which takes one parameter and checks whether a string has no "e" and "n".
#Use a list comprehension which loops through the previous list from task 3 (community_members) and call (use) that function in the list comprehension.

community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]


def en_filter (x):

    for i in x:  
        if "e" not in x and "n" not in x:
           
         return x
    return " "
            
        
finnal_list = [en_filter(y)  for y in community_members]
print(finnal_list)

