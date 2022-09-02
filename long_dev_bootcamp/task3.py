community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]

new_a_liste = []

for x in community_members:
  if "a" in str(community_members):
    new_a_liste.append(x)

print(str(new_a_liste) + " the total number of community members with a in their name is " + str( len(new_a_liste)) )