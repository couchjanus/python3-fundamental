f = open('text.txt', 'r')
print(f.read(5))

# метод read, читающий файл целиком

f = open('text.txt')
print(f.read())


# В первой строке файла f_in записаны два целых числа через пробел. 
# Записать во второй файл (f_out) сумму этих двух чисел.

fin  = open('sum.in',  'r') # объект связан с файлом из которого будем получать данные
fout = open('sum.out', 'w') # объект связан с файлом в который будем записывать

# Считываем строку файла при помощи метода readline(),
# результат разбиваем на поля по пробельным символам методом split()
# и записываем в список InputData
line = fin.readline().split()
# Теперь в элементах списка line[0] и line[1]
# записаны два входных числа в виде строк.
# Преобразуем их к типу int и запишем их сумму в переменную sum
sum = int(line[0]) + int(line[1])
# Выведем результат в файл, но перед этим преобразуем переменную sum в тип строки (str)
fout.write(str(sum))
# Закроем файлы
fin.close()
fout.close()


# определим имя файла, который читаем
filename = "text.txt"

# открываем файл для чтения
filehandle = open(filename, 'r')  
while True:  
    # читаем одну строку
    line = filehandle.readline()
    if not line:
        break
    print(line)

# закрываем указатель на этот файл
filehandle.close()  


for line in open(filename, 'r'):  
    print(line)
