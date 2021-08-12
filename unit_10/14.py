# Пользовательские исключения (User-defined Exceptions) в Python
# В Python можно создавать собственные исключения. Такая практика позволяет увеличить гибкость процесса обработки ошибок в рамках той предметной области, для которой написана ваша программа.

# Для реализации собственного типа исключения необходимо создать класс, являющийся наследником от одного из классов исключений.

class NegValException(Exception):
   pass

try:
   val = int(input("input positive number: "))
   if val < 0:
       raise NegValException("Neg val: " + str(val))
   print(val + 10)
except NegValException as e:
  print(e)