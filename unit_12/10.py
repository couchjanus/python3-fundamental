# Встроенные функции сортировки Python
# метод sort()

# Создадим новый список, чтобы отсортировать его содержимое с помощью метода sort():
 
apples_eaten_a_day = [2, 1, 1, 3, 1, 2, 2]  
apples_eaten_a_day.sort()  
print(apples_eaten_a_day) # [1, 1, 1, 2, 2, 2, 3]  

# можем использовать функцию sorted() для создания нового отсортированного списка:

apples_eaten_a_day_2 = [2, 1, 1, 3, 1, 2, 2]  
sorted_apples = sorted(apples_eaten_a_day_2)  
print(sorted_apples) # [1, 1, 1, 2, 2, 2, 3]  

# Оба списка сортируются в порядке возрастания
# можете отсортировать в порядке убывания, установив для флага реверса значение True:

# Reverse sort the list in-place
apples_eaten_a_day.sort(reverse=True)  
print(apples_eaten_a_day) # [3, 2, 2, 2, 1, 1, 1]

# Reverse sort to get a new list
sorted_apples_desc = sorted(apples_eaten_a_day_2, reverse=True)  
print(sorted_apples_desc) # [3, 2, 2, 2, 1, 1, 1]  

# Функция sorted() может сортировать любой итеративный объект, который включает в себя — списки, строки, кортежи, словари, наборы (set) и пользовательские итераторы.

# Встроенная функция сортировки реализуют алгоритм сортировки Тима. Этот алгоритм, основан на сортировке слиянием и сортировке вставкой.


