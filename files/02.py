# Запись в файл:

f = open('hello.txt', 'w')
f.write('Hello, World!')
f.close()


f = open('hello.txt', 'w')
f.write('Hello, ')
f.write('World!')
f.close()

# Дозапись в файл:

f = open('hello.txt', 'a')
f.write('Hello, ')
f.write('World!')
f.close()

# записать в файл список:
l = [str(i)+str(i-1) for i in range(20)]
print(l)

# Откроем файл на запись:
f = open('list.txt', 'w')
# Запись в файл осуществляется с помощью метода write:
for index in l:
	f.write(index + '\n')

# метод write возвращает число записанных символов.
# После окончания работы с файлом его обязательно нужно закрыть с помощью метода close:
f.close()

# Откроем файл на чтение, и прочитаем строки.

f = open('list.txt', 'r')

l = [line.strip() for line in f]
print(l)
f.close()