
with open("hello.txt", "a") as file:
    file.write("\ngood bye, world")

with open("hello.txt", 'r') as filehandle:

    for line in filehandle:

        print(line)

# Еще один способ записи в файл представляет стандартный метод print(), который применяется для вывода данных на консоль:

with open("hello.txt", "a") as hello_file:
    print("Hello, world", file=hello_file)

