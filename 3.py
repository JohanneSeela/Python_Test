print("Hallo Welt!")
print("Python lernen!")

i = 42
i += 1
i

x = 42
id(x)
y = x
id(x), id(y)
y = 78
id(x), id(y)

s='Python'
print(s[0])
print(s[3])
index_last_char = len(s)-1
print(s[index_last_char])
print(s[index_last_char-1])

last_character =s[-1]
print(last_character)

s [2:4]

a="Linux"
b="Linux"
a is b

a="Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
b="Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
a is b

a="Baden-Württemberg"
b="Baden-Württemberg"
a is b
a==b

a="Baden!"
b="Baden!"
a is b
a==b

a="Baden1"
b="Baden1"
a is b

x=b"Hallo"
t=str(x)
u=t.encode("UTF-8")
print(u)

