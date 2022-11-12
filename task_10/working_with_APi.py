# Your task now is to build a script which requests the API every 5 seconds and saves the quote and author of the returned string into a list of dictionaries.
# If the list reached 100 entries, you shall stop the loop and save the whole list of dictionaries into a file called inspirational_quotes.json.
# keep requesting the API every 5 seconds
# save the quote and author of the returned string into a list of dictionaries
# once the list reaches 100 entries break
# save the the whole list of dictionaries into a json file
import requests
import time
import json

page = "https://api.goprogram.ai/inspiration"
all_quotes = []


def quotes_scraper():
    while len(all_quotes) < 101:
        content = requests.get(page)
        time.sleep(5)
        formated_content = content.json()
        all_quotes.append(formated_content)
    return all_quotes


quotes_scraper()

with open("inspirational_quotes.json", "w", encoding="utf-8") as quotes:
    quotes.write(json.dumps(all_quotes, indent=4))
