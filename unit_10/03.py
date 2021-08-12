# Обработка общего класса исключений Exception

# try:
#     #your code
# except Exception as ex:
#     print(ex)

# 

try:
    x = int(input("Введите целое число x (для вычисления 1/x): "))
    res = 1 / x

    print("1/{} = {:.2f}".format(x, res))
except Exception as err:
    print("Произошла ошибка!")
    print("Тип:", type(err))
    print("Описание:", err)
