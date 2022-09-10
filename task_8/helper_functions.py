#Create a module called helper_functions.py with a function called my_file_opener(file_name)which takes the file name as a parameter,
#opens it and returns it as a dictionary. Use that function every time you have to read a file.
from fileinput import close
import json
def my_file_opener(file_name):

    my_file=open(file_name , encoding='utf-8')
    file_dictioanary = json.load(my_file)
    my_file.close()
    return file_dictioanary