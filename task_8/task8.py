# Given is a list of 5 self.dev members of your choice.
# Create a list of dictionaries with the following keys for each member: instagram username, discord name, reason why they want to learn programming.
# Save that dictionary in a file called selfdev_members.json
# Now you need to recall your memory and open the newly created .json file. Check the previous tasks again if you forgot.
# Read the dictionary from the .json file into a variable of your choice and iterate through the list of dictionaries. Print a text which could look like the following example down below for each member of the dictionary:
# Long (long#0003) likes to learn how to program because he is lazy"
# Now, it gets tricky. Try to loop through your list of dictionary again and this time, append a new key and value of your choice to each member.
# After this, save the new and enhanced dictionary into a new file called selfdev_members_enriched.json
# There are many ways to do that, try to find an easy way.
import json
import helper_functions
import random

path = ("C:\\Users\\ismail\\Documents\\py\\long_dev_bootcamp\\task_8\\selfdev_members.json")
path2 = ("C:\\Users\\ismail\\Documents\\py\\long_dev_bootcamp\\task_8\\selfdev_members_enriched.json")
if __name__ == "__main__":
    members_list = helper_functions.my_file_opener(path)
    for member in members_list:
        print("{name} {discord_name} likes to learn how to program because {reason_to_code}".format(**member))
        # games_list = ["apex legends", "lol", "fortnite", "wow", "valorant"]
        # member["favorite_game"] = games_list[random.randrange(5)]    #long methode
        # using list comprehension
        # enriched_list = [dict(member, **{'favorite_game':games_list[random.randrange(5)]}) for member in members_list]
        # now if we have a dictionary of games
        games_dictionary = {
            "first_game": "apex legends",
            "second_game": "lol",
            "third_game": "fortnite",
            "fourth_game": "valorant",
            "fifth_game": "black_desert",
        }
        # member["favorite_game"] = random.choice(list(games_dictionary.values()))
        # Dictionary Comprehension
        enriched_list = [dict(member,**{"favorite_game": random.choice(list(games_dictionary.values()))})for member in members_list]
        new_list = json.dumps(enriched_list, indent=4)

    with open(path2, "w") as enriched_members_list:
        enriched_members_list.write(new_list)
