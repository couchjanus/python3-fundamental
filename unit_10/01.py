# Самый простейший пример исключения - деление на ноль (ZeroDivisionError) :

## Пример встроенного возбуждения исключения:

## ZeroDivisionError исключение:
100 / 0
# Traceback (most recent call last):
#   File "", line 1, in
#     100 / 0
# ZeroDivisionError: division by zero

## TypeError исключение:
# TypeError (операция применена к объекту несоответствующего типа)
2 + '1'
# Traceback (most recent call last):
#   File "", line 1, in
#     2 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

## ValueError исключение
# ValueError (аргумент правильного типа, но некорректного значения)
int('qwerty')
# Traceback (most recent call last):
#   File "", line 1, in
#     int('qwerty')
# ValueError: invalid literal for int() with base 10: 'qwerty'

