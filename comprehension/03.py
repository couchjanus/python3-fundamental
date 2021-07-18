# В Python существует возможность использования условных выражений, 
# поэтому вместо написания if .. else с присваиванием переменной в каждой ветке 
# вы можете делать следующее:

count = 13
# делаем число всегда нечетным 

number = count if count % 2 else count - 1
print (number)
# вызываем функцию, если объект не None 

name = None
name = name if name is not None else 'Guest'
print ("Hello", name)

# Приведенный выше код очень легко читается, по сравнению с оператором ternary, который выглядит следующим образом , a ? b : c , и используется в других языках. 


## Условные списки

# Можно добавить один или несколько условий if для фильтрации значений.

## Добавим фильтрацию или условный оператор:


num = [x for x in (1, 2, 3) if x % 2 == 0]
print (num)

numbers = [1, 2, 3, 4, 5, 6, 7]

# квадраты всех нечетных чисел
squares = [num * num for num in numbers if num % 2]
print (squares)

# умножаем четные числа на 2 и нечетные на 3
mul = [num * 3 if num % 2 else num * 2 for num in numbers]
print(mul)

# Извлечение только четных чисел из последовательности целых чисел:

e = [x for x in range(10) if x % 2 == 0] #Out: [0, 2, 4, 6, 8]
print(e)
# Приведенный код эквивалентен:

even_numbers = [] 
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers) #Out: [0, 2, 4, 6, 8]

## Подсчет вхождений с использованием включений
# Посчитать числа в range(1000) которые чётные или содержат цифру 9:
# Перебрать элементы в диапазоне (1000).
# Объединть все необходимые if условия.
# Используйте 1 в качестве выражения, чтобы вернуть 1 для каждого элемента, который соответствует условиям.
# Суммируйте все 1, чтобы определить количество, которые соответствуют условиям.

print(sum(
    1 for x in range(1000)
    if x % 2 == 0 and
    '9' in str(x)
))  # Out: 95

# else можно использовать в списковых включениях, но нужно следить за синтаксисом. Условие if или else следует использовать перед циклом for, а не после:

# создать список символов из apple, replacing согласные на '*'

# Ex - 'apple' --> ['a', '*', '*', '*' ,'e']
# print([x for x in 'apple' if x in 'aeiou' else '*']) # Out: SyntaxError: invalid syntax

# При использовании if / else используйте их перед циклом
print([x if x in 'aeiou' else '*' for x in 'apple']) # Out:['a', '*', '*', '*', 'e']

print([x + 1 if x % 2 == 0 else x for x in (1, 2, 3)])

# списковое включение с фильтрацией
print([x + 1 if x % 2 == 0 else x for x in range(-3,4) if x > 0])





# Применение условного списка вида [e for x in y if c], где e и c являются выражениями, эквивалентно list(filter(lambda x: c, map(lambda x: e, y)))


print([x if x % 2 == 0 else None for x in range(10)]) # Out: [0, None, 2, None, 4, None, 6, None, 8, None]
# Здесь условное выражение - не фильтр, а оператор, определяющий значение, которое будет использоваться для элементов списка:
# <value-if-condition-is-true> if <condition> else <value-if-condition-is-false>
 
# Это становится более очевидным, если вы объедините его с другими операторами:

print([2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]) #Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

# Приведенный выше код эквивалентен:

numbers = []
for x in range(10):
    if x % 2 == 0:
        temp = x
    else:
        temp = -1
    numbers.append(2 * temp + 1)

print(numbers)
