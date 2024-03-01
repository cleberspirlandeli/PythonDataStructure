#TUPLAS

tupla = ('AAA', 'BBB', 'CCC') # AAA 0, BBB 1, CCC 2
print(tupla)
print(tupla[0])

tupla.index('BBB') # Result 1

for elemento in tupla:
  print(elemento)



# LISTs
l1 = ['AAA', 'BBB', 'CCC']
l2 = ['DDD', 'EEE']
l3 = l1 + l2
print(l3) # 'AAA', 'BBB', 'CCC', 'DDD', 'EEE'

l2_2 = l2 * 2
print(l2_2) # 'DDD', 'EEE', 'DDD', 'EEE'

print(l1) # 'AAA', 'BBB', 'CCC'
print(l1[0:2]) # 'AAA', 'BBB'

l1.append('ZZZ')
print(l1) # 'AAA', 'BBB', 'CCC', 'ZZZ'

l1.remove('CCC')
print(l1) # 'AAA', 'BBB', 'ZZZ'

del(l1)
print(l1) # Error

for item in l2_2:
  print(item)



# DICTIONARIES
dictionary = {'AAA': 32, 'BBB': 22, 'CCC': 14}
print(dictionary['AAA']) # 32

dictionary['DDD'] = 11
print(dictionary) # {'AAA': 32, 'BBB': 22, 'CCC': 14, 'DDD': 11}

del(dictionary)['BBB']
print(dictionary) # {'AAA': 32, 'CCC': 14, 'DDD': 11}

print(dictionary.items()) # dict_items([('AAA', 32), ('CCC', 14), ('DDD', 11)])

print(dictionary.keys()) # dict_keys(['AAA', 'CCC', 'DDD'])

print(dictionary.values()) # dict_keys([32, 14, 11])

coleta2 = {'YYY': 13, 'ZZZ': 14}
dictionary.update(coleta2)
print(dictionary) # {'AAA': 32, 'CCC': 14, 'DDD': 11, 'YYY': 13, 'ZZZ': 14}

for k, v in dictionary.items():
    print(f'Key: {k}, Value: {v}')


# SETs
sets = ('a', 'b', 'c', 'd',
        'b', 'c', 'c', 'c')

print(sets) # 'a', 'b', 'c', 'd', 'b', 'c', 'c', 'c'
print(set(sets)) # 'a', 'b', 'c', 'd'

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3) # {3, 4, 5}

print(c1.difference(c2)) # {1, 2}
print(c2.difference(c1)) # {6, 7}