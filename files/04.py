# Прочитать файл и записать его содержимое в другой файл:

f = open('text.txt')

lines = f.readlines()
f.close()

lines[0] = "This is a file2.txt \n" # изменяем 1-ю строку
f = open('file2.txt','w')
f.writelines(lines)
f.close()
