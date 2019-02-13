import time

n= 100000

s = time.time()
l = []
for i in range(n):
    l += [i * 2]


d = time.time()
print(d-s)

import time

n= 100000

start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]

print(time.time() - start_time)

start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]

print(time.time() - start_time)

start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)

print(time.time() - start_time)

colours = ["red", "green", "blue", "green", "yellow"]
colours.remove("green")
colours
colours.remove("green")
colours
colours.remove("green")

colours = ["red", "green", "blue", "green", "yellow"]
colours.index("green") 
colours.index("green",2)
colours.index("green", 3,4)
colours.index("black")

colours.insert(1,"black")
colours
colours.insert(len(colours),"orange")
colours

