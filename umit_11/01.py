## выведем элементы произвольного списка на экран.

num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)

## исключение StopIteration
# объекты, элементы которых можно перебирать в цикле for, содержат в себе объект итератор, для того, чтобы его получить необходимо использовать функцию iter(), а для извлечения следующего элемента из итератора – функцию next().

itr = iter(num_list)
print(next(itr))

print(next(itr))

print(next(itr))

print(next(itr))
print(next(itr))
print(next(itr))
