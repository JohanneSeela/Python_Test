empty={}
empty

food={"ham":"yes", "egg":"yes", "spam":"no"}
food
food["spam"]="yes"
food

en_de={"red":"rot", "green":"grün","blue":"blau", "yellow":"gelb"}
print(en_de)
de_fr={"rot":"rouge", "grün":"vert", "blau":"bleu", "gelb":"jaune"}
print("The French word for red is: "+de_fr[en_de["red"]])

dictionaries={"en_de":en_de, "de_fr":de_fr}
print(dictionaries["de_fr"]["blau"])

dic={(1,2,3):"abc", 3.1415:"adc"}
dic

