## Поймать несколько исключений в одном блоке Except
# Обратите внимание, что вы можете отделить исключения от переменной запятой, которая применима в Python 2.6 / 2.7. Но вы не можете сделать это в Python 3. Поэтому вы должны использовать ключевое слово as.


except (Exception1, Exception2) as e:
    pass

# Есть много способов обработки нескольких исключений. Первый из них требует размещения всех исключений, которые могут возникать в виде кортежа.

try:
    file = open('input-file', 'open mode')
except (IOError, EOFError) as e:
    print("Testing multiple exceptions. {}".format(e.args[-1]))

# Следующий метод заключается в обработке каждого исключения в выделенном блоке Except. Вы можете добавить столько, Except блоков, сколько необходимо.

try:
    file = open('input-file', 'open mode')
except EOFError as ex:
    print("Caught the EOF error.")
    raise ex
except IOError as e:
    print("Caught the I/O error.")
    raise ex
