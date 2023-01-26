# Create a new file Task10c.py which on start awaits for an integer as an input from the user.
# After that, you should get access to your inspirational_quotes.json file and return the quote and author at the index of the user input.
import json


def get_quote():
    with open("inspirational_quotes.json", "r", encoding="utf-8") as quotes_file:
        content = json.load(quotes_file)
        quotes_number = int(input("enter quote number\n"))

        while True:
            if quotes_number in range(0, 100):
                print(content[int(quotes_number)])
                exit()
            else:
                quotes_number = int(input("try again with a number between 0 and 100\n"))


get_quote()
