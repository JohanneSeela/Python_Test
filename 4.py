10//3
1 in [3,2,1]
txt="Hello World"
txt[0]
txt[4]
txt[-1]
txt[-5]

colours=['red', 'green', 'blue']
colours[0]
colours

a=["Swen", 45, 3.54, "Basel"]
a[3]

pers=[["Marc", "Mayer"], ["Haupstr. 17", "12345", "Musterstadt"], "07876/7876"]
name=pers[0]
name[1]
adresse=pers[1]
adresse[1]
pers[2]
strasse=pers[1][0]
strasse

t = ("tuples", "are", "immutable")
t[0]
t[0]="assignments to elements are not possible"

txt[0]
txt[1:5]
txt[0:5]
txt[:5]
txt[5:]
txt[:6]
txt[:]
txt[0:-6]

colours[1:3]
colours[2:]
colours[:2]
colours[-1]

tyt = "Python ist ganz toll"
tyt[2:15:3]
tyt[::3]

s="Hamburg"
s[::-1]
d="Frankfurt"
d[::-2]

staedte=["Berlin", "Frankfurt", "Stuttgart", "Zürich", "Basel"]
stadte=staedte[::-1]
stadte

len(txt)
len(a)

firstname = "Homer"
surname = "Simpson"
name = firstname + " " + surname
print(name)

colours1=["red", "green", "blue"]
colours2=["black", "white"]
colours3=colours1+colours2
colours3

s=1
t=3
s+=t

abc=["a", "b", "c", "d", "e"]
"a" in abc
"a" not in abc
"e" not in abc
"f" in abc

str="Python ist toll!"
"y" in str
"x" in str

3*"xyz-"
"xyz-"*3
3 * ["a","b","c"]

x=["a", "b", "c"]
y=[x]*4
y
y[0][0]="p"
y
x
