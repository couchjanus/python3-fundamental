import os
tree = os.walk('test')
print(tree) # <generator object walk at 0x7f1119ca0518>
for i in tree:
    print(i)

# Если передать абсолютный адрес, то получится так:

for i in os.walk('/home'):
    print(i)