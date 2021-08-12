# Избегайте генерирования общих исключений, потому что если вы это сделаете, то должны быть перехвачены и все другие более конкретные исключения. Следовательно, лучшая практика заключается в том, чтобы поднять наиболее конкретное исключение, близкое к вашей проблеме.


# Плохой пример:

def bad_exception():
    try:
        raise ValueError('Intentional - do not want this to get caught')
        raise Exception('Exception to be handled')
    except Exception as error:
        print('Inside the except block: ' + repr(error))
        
bad_exception()

# Пример получше:

# Здесь мы приводим конкретный тип исключения, а не общий тип. И мы также используем опцию args для вывода неверных аргументов, если они есть. Давайте посмотрим на приведенный ниже пример.

try:
    raise ValueError('Testing exceptions: The input is in incorrect order', 'one', 'two', 'four') 
except ValueError as err:
    print(err.args)
