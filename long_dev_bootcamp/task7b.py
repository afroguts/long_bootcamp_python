#Create a new file called python7b.py 
# and write a new function called save_list_into_file(my_list) 
# with one parameter which should be a list.
#After that, check out task 5 again and 
# save the result of that task (the filtered list) into a new file called my_first_saved_list.txt.
#1/a function with 1 patrametre == list [] 
#2/open the  task 5
#3/save the result the results to a text file

if __name__ == "__main__":
    def save_list_into_file(my_list=[]):
    
        a_list=open(r"C:\Users\ismail\Documents\py first shit\long_dev_bootcamp\my_first_saved_list.txt" , "w") 

        a=a_list.write(str(my_list))
        a_list.close()
        print(a)    
        
y=[' ', ' ', 'arth', ' ', ' ', ' ', ' ', 'darthtilda']   
save_list_into_file(y)
