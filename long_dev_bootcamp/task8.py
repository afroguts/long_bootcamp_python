import json

if __name__ == "__main__":
    dic ={}


    with open(r"C:\Users\ismail\Documents\py first shit\long_dev_bootcamp\selfdev_members.json" ) as json_file:
    
        dic = json.load(json_file)
        for x in dic :
            print (x['name' ]+' (' + x['discord_name'] + ') ' + ' ' + 'likes to learn how to program beacuse' + ' ' + x['reason_to_code'] )
            #a= (x['name' ]+ x['discord_name'] +  'likes to learn how to program beacuse' +  x['reason_to_code'] ).split(' ')
            #print (a)  #/tried to make the output cleaner with this but it seems to be wrong
            
            x.update( {'addicted_to':"discord"})  
            
        aa = json.dumps(dic ,sort_keys=True, indent=4)   
        
    json_file.close()
    f = open(r"C:\Users\ismail\Documents\py first shit\long_dev_bootcamp\selfdev_members_enriched.json","w")
       
    f.write(aa )
    f.close()

