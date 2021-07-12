# Записать в исходный файл input 10 строк в каждой из которых находится случайное число из отрезка [10, 99].
# Получить из этого файла данные чтением построчно с суммированием 
# и отправить среднее арифметическое в файл output. 
# (Представить вещественное число в экспоненциальном формате).

from random import randint
fin = open('input1', 'w+')
try:
    for j in range(10):
        fin.write(str(randint(10, 99)) + '\n')
    s = 0
    for j in fin:
        s += int(j)
finally:
    fin.close()
fout = open('output1', 'w')
try:
    fout.write('{:e}'.format(s/10))
finally:
    fout.close()
