## Вложенные итерации

# Списки могут использовать любое количество вложенных циклов for. Каждый цикл for может иметь дополнительный связанный if. При этом порядок следования for такой же, как при написании серии вложенных for. 
# Общая структура списочных представлений:
# [ expression for target1 in iterable1 [if condition1]
#              for target2 in iterable2 [if condition2]...
#              for targetN in iterableN [if conditionN] ]


# использование нескольких for операторов:

# Вложенные циклы, дает [11, 21, 12, 22]
[x + y for x in [1, 2] for y in [10, 20]] 

# Списковые включения могут использовать вложенные итерации по переменным:

[(x, y) for x in range(1, 10) for y in range(1, 10) if x % y == 0]

[x + y for x in [1, 2, 3] if x > 2 for y in [3, 4, 5]]

[x + y for x in [1, 2, 3] for y in [3, 4, 5] if x > 2] 


data = [[1, 2], [3, 4], [5, 6]]
output = []

for each_list in data:
    for element in each_list:
        output.append(element)
print(output) # Out: [1, 2, 3, 4, 5, 6]

# эквивалентно:

data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]
print(output) # Out: [1, 2, 3, 4, 5, 6]

## Двойная итерация
# Порядок двойной итерации [... for x in ... for y in ...] является контр-логичным. 
# Эмпирическое правило - это следовать циклу for:

def foo(i):
    return i, i + 0.5

# for i in range(3):
#     for x in foo(i):
#         yield str(x)

 
# Результат:

[str(x)
    for i in range(3)
        for x in foo(i)
]

 
# можно сжать в одну строку:
print([str(x) for i in range(3) for x in foo(i)])


data = [[1,2],[3,4],[5,6]]

def f():
     output=[]
     for each_list in data:
         for element in each_list:
             output.append(element)
     return output
# timeit f()
print(f())


# Встроенный if:

data = [[1], [2, 3], [4, 5]]

output = [element for each_list in data
                if len(each_list) == 2
                for element in each_list
                if element != 5]
print(output)
