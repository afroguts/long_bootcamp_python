import json
import helper_functions
path ="C:\\Users\ismail\\Documents\\py first shit\\long_dev_bootcamp\\task_8.py\\selfdev_members.json"
path2="C:\\Users\ismail\\Documents\\py first shit\\long_dev_bootcamp\\task_8.py\\selfdev_members_enriched.json"
if __name__ == "__main__":
    members_list= helper_functions.my_file_opener(path)
    for member in members_list: 
        print (member['name' ]+' (' + member['discord_name'] + ') ' + ' ' + 'likes to learn how to program beacuse' + ' ' + member['reason_to_code'] )   
        member.update( {'addicted_to':"discord"})      
        new_list = json.dumps(members_list , indent=4)   
        
    with open(path2, "w") as enriched_members_list :
        enriched_members_list.write(new_list)
    

