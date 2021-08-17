with open('data.txt', 'r') as f:

    while True:
        line = f.readline()
    
        if not line: 
            break
            
        else: 
            print(line.rstrip())

# Вместо использования цикла while мы можем применить итератор

# Функция open() возвращает файловый объект, который является итератором. Мы можем использовать его в цикле for. Благодаря использованию итератора код становится чище.

with open('data.txt', 'r') as f:

    for line in f:
        print(line.rstrip())
