capitals={"Österreich":"Wien", "Deutschland":"Berlin", "Niederlande":"Amsterdam"}
capital=capitals.pop("Deutschland")
print(capital)
print(capitals)
capital=capitals.pop("Schweiz")

capital=capitals.pop("Schweiz","unbekannt")
print(capital)
capitals.pop("Niederlande","unbekannt")
capitals.pop("Niederlande","unbekannt")

if "car" in capitals: print(capitals["car"])

if "Österreich" in capitals: print(capitals["Österreich"])

print(capitals)

capital=capitals.get("Österreich")
print(capital)
capital=capitals.get("Deutschland")
print(capital)
capital=capitals.get("Deutschland","Berlin")
print(capital)
print(capitals)

c=capitals.copy()
capitals["Österreich"]="Passau"
print(c)
print(capitals)
capitals.pop("Österreeich")
print(capitals)

# -*- coding: utf-8 -*-

trainings={ "course1":{"title":"Python Training Course for Beginners", "location":"Frankfurt", "trainer":"Steve G. Snake"},
            "course2":{"title":"Intermediate Python Training", "location":"Berlin", "trainer":"Ella M. Charming"},
            "course3":{"title":"Python Text Processing Course", "location":"München", "trainer":"Monica A. Snowdon"}}

trainings2=trainings.copy()

trainings["course2"]["title"]="Perl Training Course for Beginners"
print(trainings2)

trainings2.clear()
print(trainings2)
print(trainings)

trainings2={"course4":{"title":"Python Numbers Processing Course", "location":"Stuttgart", "trainer":"Der Papst"}}
print(trainings2)
trainings.update(trainings2)
print(trainings)

d = {"a":123, "b":34, "c":304, "d":99}
for key in d:
    print(key)

for value in d.values():
    print(value)

