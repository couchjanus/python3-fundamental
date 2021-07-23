def fibonacci(n): # вернуть числа Фибоначчи вплоть до n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
