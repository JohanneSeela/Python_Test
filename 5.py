
l=[42,98,77]
l.append(103)
l
x=l.pop()
x
l.pop()
l

l=[42,98,77]
l2=[8,69]
l.append(l2)
l

l=[42,98,77]
l2=[8,69]
l.extend(l2)
l

l=[42,98,77]
l.extend("hello")
l

l=[42,98,77]
l.extend((3,4,5))
l

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