# https://docs.python.org/3/library/random.html
import random
print(random.random()) # 0.8763880227264942

print(random.randint(1,10)) # 7
print(random.randrange(0,10, 2)) # 2 -> Par
print(random.randrange(0,10, 2)) # 6
print(random.randrange(0,10, 2)) # 8

x = ['K', 'd', 13, '34-j', 'x']
print(random.choice(x)) # 34-j
