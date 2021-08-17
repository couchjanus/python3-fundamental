## встроенный итератор для строки
str = "formidable"

for e in str:
   print(e, end=" ")

print()

# В Python строка - это неизменная последовательность символов. 
# Функция iter() возвращает итератор для объекта. 

it = iter(str)

print(it.next())
print(it.next())
print(it.next())

print(list(it))
