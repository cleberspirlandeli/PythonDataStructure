# Manipulação de strings
text = 'Lorem Ipsum é um texto modelo da indústria tipográfica e de impressão.'
print('Default:', text)

up = text.upper()
print('Upper:', up)

low = up.lower()
print('Lower:', low)

capital = text.capitalize()
print('Capitalize:', capital)
print('')

# Get the first 4 words
half_text = text[0:4]
print('\nHalf Text:', half_text)

last_words = text[3:]
print('Last Words:', last_words)


print('\nReplaces')
replaceText = text.replace('Lorem', 'Hello')
print(text)
print(replaceText)

replaceText = text.replace('o', 'a')
print(replaceText)

print('\nFind')
print(text.find('s'))
print(text.find('a'))
print(text.find('z'))

print('\nLength')
print(len(' texto '))

print('\nRemove space with strip')
f = ' texto '.strip()
print(f)
print(len(f), '\n')

n1 = 14
n2 = 16
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')
