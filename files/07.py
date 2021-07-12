# Чтение определённой строки из файла
# Чтобы это сделать, применим счётчик и напечатаем соответствующую строку, когда дойдём до неё, проходя итерациями по файлу.

# определим имя файла, который читаем
filename = "text.txt"

# определим номер строки
line_number = 3

print ("line %i of %s is: " % (line_number, filename))

with open(filename, 'r') as filehandle:  

    current_line = 3  

    for line in filehandle:
        if current_line == line_number:
            print(line)
            break
        current_line += 1


# определим имя файла, который читаем

with open(filename, 'r') as filehandle:  
    filecontent = filehandle.read()
    print (filecontent)

# метод readlines() В отличие от read(), содержимое файла сохраняется в список, где каждый элемент есть строка содержимого:

# определим имя файла, который читаем

with open(filename, 'r') as filehandle:
    
    filecontent = filehandle.readlines()
    for line in filecontent:
        print (line)
