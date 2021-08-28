## like cat command in unix
## Чтение нескольких файлов

# Допустим, мы хотим написать программу, которая принимает список имен файлов в качестве аргументов и печатает содержимое всех этих файлов, как команда cat в unix.

# Традиционный способ реализации:

def cat(filenames):
    for f in filenames:
        for line in open(f):
            print(line, end="")

## команда grep в unix

# Теперь предположим, что мы хотим напечатать только строку с определенной подстрокой

def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print(line, end="")

# Обе эти программы имеют много общего кода. 
# Трудно перенести общую часть в функцию.

filenames = ['01.py','02.py','03.py','04.py']
cat(filenames)

pattern = "yield"
grep(pattern, filenames)