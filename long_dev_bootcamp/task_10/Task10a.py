# Create a new file Task10a.py and scrape all members of the page https://theselfdev.com/community.
# Your goal is to get all possible data which is visible on the webpage about one single member.

# Those include:
# - Name
# - Category
# - One-line Pitch
# - Image URL

# Find a way by using the packages requests and beautifulsoup to scrape all the members and save them all in a data type which fits your needs.
# Remember what data types we discussed before and be reasonable why you decided to use that specific data type.
# After that, save the data you scraped in a new file called community_members.json.
# zip() : In Python 3, zip returns an iterator. zip() function stops when anyone of the list of all the lists gets exhausted. In simple words, it runs till the smallest of all the lists.
# Below is an implementation of the zip function and itertools.izip which iterates over 3 lists:
import json
import time
import requests
from bs4 import BeautifulSoup as bs


page_link = "https://theselfdev.com/community"


page_request = requests.get(page_link)
time.sleep(1)
content = bs(page_request.text, "lxml")
with open("page_content.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(content.prettify())


specific_member = []
def info_scraper():
    name_tags = content.find_all(class_="name")
    category_tags = content.find_all(class_="category")
    summary_tags = content.find_all(class_="summary")
    for (name_info, category_info, summary_info) in zip(name_tags, category_tags, summary_tags):
        member_dict = {}
        name_info = name_info.string.strip()
        member_dict["name"] = name_info
        category_info = category_info.string.strip()
        member_dict["category"] = category_info
        summary_info = summary_info.string.strip()
        member_dict["summary"] = summary_info
        specific_member.append(member_dict)
    return specific_member


def saving_json_file(p):
    with open("community_members.json", "w", encoding="utf-8") as community_members:
        community_members.write(json.dumps(p, indent=6))


saving_json_file(info_scraper())











# ignore [only for me]
# scraping all the names since they all exist in the h4 tage
# tags = content.find_all("h4")
# for item in tags:
#     print(item.string)
# tags_1 = content.find_all(class_ = "category")
# for item in tags_1:
#     print(item.string)
