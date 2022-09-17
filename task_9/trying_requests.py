#Create a new file and get familiar working with that module by requesting a page of your choice and printing the whole HTML code of it.
#Your code shouldn't be longer than 10 lines.
#Now that you have the HTML code of your whole webpage, 
#find a way to count all "e"s in that whole HTML code and print the number of counts.
#Do the same for the word "<p>" and print the number of counts as well.
#print(page.status_code ) if the code printed start with 2 all is working
#we can use the "xml parser" istead of the lxml but it's old .
from bs4 import BeautifulSoup
import requests 
url="https://quotes.toscrape.com"
file_name= "quotes_html_file.txt"
page = requests.get(url)
soup = BeautifulSoup(page.text , "lxml")
with open(file_name , "r+" , encoding="utf-8") as txt_file :
    txt_file.write(f'{soup.prettify()}\n')

with open(file_name , "r+" , encoding="utf-8") as txt_file2 :
    text = txt_file2.read()
    counting_e = text.count("e")
    counting_p = text.count("p")
    print (f"there are {counting_e} e and {counting_p} p in this file")
    

