# The program creates a very simple generator.

def genn():
   x, y = 1, 2
   yield x, y
   
   x += 1
   yield x, y

g = genn()
print(next(g))
print(next(g))

# Инструкция yield может употребляться и в конструкции try except. 
# Если к генератору не обратились до его финализации 
# (финализация происходит, когда счётчик ссылок доходит до нуля, либо когда происходит сборка мусора), 
# будет вызван метод итератора .close(), что позволяет выполнить оставшиеся в блоке finally инструкции.
def gen():
   x, y = 1, 2
   yield x, y
 
   x += 1
   yield x, y

g = gen()
print(next(g))
print(next(g))

try:
   print(next(g))
   
except StopIteration:
   print("Iteration finished")

# (1, 2)
# (2, 2)