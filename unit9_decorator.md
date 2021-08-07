# Декоратор

Функции - это объекты первого уровня. Функцию можно динамически создавать, передавать в функцию и изменять. 
```py

def moo(string):
   lowercase = string.lower()
   return lowercase

moo.yloo = 'You Live Only Once'
print(moo.yloo)

# можно присвоить переменной функцию, так же как обычные значения этой переменной.
foo = moo
print(foo("Hello world")) # hello world

```
Функцию можно передавать в качестве аргумента другим функциям. Например, есть список целых чисел, на базе него получить другой список,  элементами которого будут квадраты первого, 

```py
a = [1, 2, 3, 4, 5] # исходный список
# функция, возводящая переданное ей число в квадрат
sq = lambda x: x**2
b = list(map(sq, a)) # получаем список квадратов
print(b)
# такую задачу можно решить в одну строчку:
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))

lo = lambda x: x.lower()
print(lo("Hello Lambda"))

```
В Python функция – это специальный объект, который имеет метод __call__(). 
```py
# создадим класс.
class LowerCall():
   def __call__(self, string):
       return string.lower()

# объект такого класса можно вызывать как функцию.
hello = LowerCall()
print(hello("HELLO LOWER CALL"))
```
## Определение функции внутри другой функции
```py
def mul(a): # функция умножает два числа.
   def helper(b):
       return a * b
   return helper
# внутри функции mul() создается еще одна функция, которая называется helper();
# функция mul() возвращает функцию helper как результат работы.
# Вызывается эта функция так:
mul(4)(2)
# на базе функции mul() можно создавать кастомизированные функции.
# создадим функцию three_mul, которая умножает на три любое переданное ей число.
three_mul = mul(3)
three_mul(5)

```
Внутри функций можно создавать другие функции, вызывать их и возвращать как результат через return.  На этом построена идея замыкания (closures).
```py
def call_this(f):
   f()
   print("Called it!")

def call_foo(f):
   f('Hell ')

def bar(hell = ""):
   print(hell + "Called bar!")

call_this(bar)
call_foo(bar)

```
## Декоратор - это шаблон проектирования
Декоратор - это шаблон проектирования, который мы можем использовать для добавления новых функциональных возможностей к уже существующей функции без необходимости изменять ее структуру. Декоратор должен вызываться непосредственно перед функцией, которая должна быть расширена. С помощью декораторов вы можете динамически изменять функциональные возможности методов, функции или класса без непосредственного использования наследования. Это хороший, способ расширения функциональности функции, которую не хотите изменить напрямую.
Декоратор модифицирует принятую функцию и выдает измененную. Это значит, что когда вы вызываете декорированную функцию, вы получите функцию, которая может иметь небольшие отличия, в виде дополнительных функций, совмещенных с базовым определением.

## Определение функции decorator
```py
def lowercase(f): 
   def wrapper():
       return f().lower()
   return wrapper

def test_lowercase(): 
   return 'HELLO DECORATORS WORLD'

decorate = lowercase(test_lowercase) 
print(decorate()) 

```
Конструктивно декоратор в Python представляет собой некоторую функцию, аргументом которой является другая функция. Декоратор предназначен для добавления дополнительного функционала к данной функции без изменения содержимого последней.
1. Декораторы расположены перед объявлением функций и служат для того, чтобы добавить какой-то функционал не скрывая цель исходной функции.

2. Выглядит это примерно так:
```py
@custom_decorator
def generic_example_function():
   # ...
   pass

```
3. При определении функции декоратора, она должна использоваться как ввод и выводить новую, измененную функцию.
```py
def custom_decorator(func):
   # *args, **kwargs allow your decorated function to handle
   # the inputs it is supposed to without problems

   def modified_function(*args, **kwargs):
       # Do some extra stuff
       # ...
       return func(*args, **kwargs)
# Call the input function as it
# was originally called and return that
   return modified_function

def foo(x):
   return x**2
def bar(x):
   return x - 2

# Обе функции завершатся ошибкой при вызове со строкой '2'.  Мы можем добавить функцию преобразования типа и декорировать этой функцией foo и bar.

# Trespassers will be prosecuted
def trespassers_w(f):
   def new_f(x):   # определяем функцию
       return f(float(x))
   return new_f    # возвращаем новую функцию


# функция-обёртка trespassers_w требует функцию в качестве аргумента и возвращает новую функцию.
foo_new = trespassers_w(foo)

# trespassers_w возвращает функцию:
print(foo_new)

print(foo_new('2')) # OUT: 4.0
print(trespassers_w(bar)('2')) # OUT: 0
# trespassers_w принимает функцию (A) в качестве аргумента и возвращает новую функцию (B).
# Новая функция (B) при вызове вызывает функцию (A), но не с аргументом x,
# а с float(x), и таким образом решает проблему TypeError.

```
## Синтаксис декоратора
```py
@trespassers_w
def foom(x):
   return x**2

@trespassers_w
def boom(x):
   return x - 2

print(foom('2'))
print(boom('2'))
```
Декоратор начинается с символа @, за которым следует название функции, которую мы собираемся «декорировать». Для получения декоратора python, вам нужно разместить его в строке перед определением функции. 
```py
def logger(func): # Logging before and after a function be executed
   def wrapper(): # Function called by the decorator
       print('Start')
       func() # External function
       print('End')
   return wrapper

@logger # Decorator
def my_function(): # External function
   print('...Executing function...')
my_function()

```
Если функция требует наличие аргумента, то его можно передать через декоратор.
```py
def print_them_args(fn):
   def the_name_of_this_one_doesnt_matter(*args):
       # внутренняя функция перехватит значения аргументов в виде *args, **kwargs.
       print("{} called with {}".format(fn.__name__, [*args]))
       return fn(*args)
   return the_name_of_this_one_doesnt_matter
@print_them_args
def add(a, b):
   return a + b
add(5, 8)

```
## Передача аргументов в функцию через декоратор
```py
from time import sleep
def delay(seconds):
   def decorator(fn):
       def inner(*args, **kwargs):
           print("{} called with {} and {}".format(fn.__name__, [*args], {**kwargs}))
           sleep(seconds)
           return fn(*args, **kwargs)
       return inner 
   return decorator

@delay(5)
def it_may_be(times, name = ''):
   return name + " said: It is nearly Luncheon Time! " * times

print(it_may_be(3, name = 'Winnie-the-Pooh'))


```
Довольно часто, создаваемые функции возвращают какое-либо значение. Для того, чтобы его можно было возвращать через декоратор необходимо соответствующим образом построить внутреннюю функцию.
```py
def decor_with_return(fn):
  def wrapper(*args, **kwargs):
      print("Run method: " + str(fn.__name__))
      return fn(*args, **kwargs)
  return wrapper

@decor_with_return
def calc_sqrt(val):
  return val**0.5
print(calc_sqrt(16))

```
В математике и в программировании это называют композицией функций. Так же как f o g(x) == f(g(x)),  если положить в стек @pop на @lock на drop, то получится pop(lock(drop(it))).
```py
def pop(func):
   def inner(*args, **kwargs):
       print("Pop!")
       return func(*args, **kwargs)
   return inner

def lock(func):
   def inner(*args, **kwargs):
       print("Lock!")
       return func(*args, **kwargs)
   return inner

```
Мы можем спрятать функцию, которая уже была спрятана.
```py
@pop
@lock
def drop(it):
   print("Drop it!")
   return it[:-2]

print(drop("That's the end of that one, isn't it"))

def decor(fn):
  def wrapper(self):
      print("Run method: " + str(fn.__name__))
      fn(self)
  return wrapper

class Vector(): # Vector - класс для представления двумерного вектора.
  def __init__(self, px = 0, py = 0):
      self.px = px
      self.py = py
  @decor
  def normalize(self):  # метод normalize() выводит модуль вектора.
      print((self.px**2 + self.py**2)**0.5)
vector = Vector(px=10, py=5)
vector.normalize()

```
## Декоратор на основе классов без переменных
```py
class FunnyDecorator:
   def __init__(self, fn):
       print("Initializing Funny decorator class")
       self.fn = fn
       fn()

   def __call__(self):
       print("Calling Funny decorator call method")
       self.fn()



@FunnyDecorator
def simple_function():
   print("Inside the simple function")

print("Funny Decoration complete!")

simple_function()
```

Декораторы на основе классов ведут себя по-разному в зависимости от того, есть у них переменные или нет. Когда в декораторе есть переменные, происходит три вещи.
Переменные декораторов передаются в функцию __init__.
Функция сама по себе является функцией вызова.
Функция __сall__ вызывается немедленно и только один раз, примерно так же работает декоратор в функциях
```py
class SlimCache: # простой кэширующий декоратор
   # This method is called as soon as the decorator is attached to a function.
   def __init__(self, preloads={}):
       if preloads is None:
           self.cache = {}
       else:
           self.cache = preloads

   def __call__(self, func):
       # This method is called when a function is passed to the decorator
       def inner(n):
           if n in self.cache:
               return self.cache[n]
           else:
               result = func(n)
               self.cache[n] = result
               return result
       return inner


@SlimCache({1: 1, 2: 1, 4: 3, 8: 21}) # First __init__, then __call__
def fibonacci(n):
   """Returns the nth fibonacci number"""
   if n in (1, 2):
       return 1
   else:
       return fibonacci(n - 1) + fibonacci(n - 2)

# At runtime, the 'inner' function above will actually be called!
# fibonacci(8) never actually gets called, because it's already in the cache!

print(fibonacci(8))

```
Python содержит несколько встроенных декораторов. самыми важными из них являются:
```py
   @classmethod
   @staticmethod
   @property

```
Также существуют декораторы в различных разделах стандартной библиотеки Python. Одним из примеров является functools.wraps. 

Декоратор @classmethod может быть вызван при помощи экземпляра класса, или напрямую, через собственный класс Python в качестве первого аргумента. Декоратор может быть вызван как в классе (например, C.f()), или в экземпляре (например, C().f()). Экземпляр игнорируется, за исключением его класса. Если метод класса вызван для выведенного класса, то объект выведенного класса передается в качестве подразумеваемого первого аргумента.
Декоратор @classmethod, в первую очередь, используется как чередуемый конструктор или вспомогательный метод для инициализации.
Декоратор @staticmethod - это просто функция внутри класса. Вы можете вызывать их обоих как с инициализацией класса так и без создания экземпляра класса. Обычно это применяется в тех случаях, когда у вас есть функция, которая, по вашему убеждению, имеет связь с классом. По большей части, это выбор стиля.
```py
   print(decor.doubler)
   print(decor.class_tripler)
   print(decor.static_quad)

```
Можно вызывать обычный метод и оба метода декоратора одним и тем же путем. Обе функции @classmethod и @staticmethod можно вызывать прямо из класса или из экземпляра класса. 
Если попытаться вызвать обычную функцию при помощи класса (DecoratorTest.doubler(2)),  получите ошибку TypeError. 

@staticmethod — используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван. Он просто получает переданные аргументы, без неявного первого аргумента, и его определение неизменяемо через наследование.
@staticmethod — это вроде обычной функции, определенной внутри класса, которая не имеет доступа к экземпляру, поэтому ее можно вызывать без создания экземпляра класса.
```py
# Синтаксис:
class ClassName:
   @staticmethod
   def method_name(arg1, arg2, ...): ...

# Здесь мы используем декоратор @staticmethod для определения статического метода
# статический метод не принимает self в качестве первого аргумента для метода.
class Myclass():
   @staticmethod
   def staticmethod():
       print('static method called')

# мы можем получить доступ к статическому методу класса без создания экземпляра.
Myclass.staticmethod()

# Хотя вызов метода из экземпляра класса тоже возможен.
my_obj = Myclass()
my_obj.staticmethod()

# Статический метод помогает в достижении инкапсуляции в классе, поскольку он не знает о состоянии текущего экземпляра. Кроме того, статические методы делают код более читабельным и повторно используемым, а также более удобным для импорта по сравнению с обычными функциями, поскольку каждую функцию не нужно отдельно импортировать.

class Person():
   @staticmethod
   def is_adult(age):
       if age > 18:
           return True
       else:
           return False
# мы можем проверить, является ли человек взрослым, без инициирование создания экземпляра.
Person.is_adult(23)

```
@classmethod — это метод, который получает класс в качестве неявного первого аргумента, точно так же, как обычный метод экземпляра получает экземпляр. Это означает, что вы можете использовать класс и его свойства внутри этого метода, а не конкретного экземпляра.
@classmethod — это обычный метод класса, имеющий доступ ко всем атрибутам класса, через который он был вызван. Следовательно, classmethod — это метод, который привязан к классу, а не к экземпляру класса.
```py
# Синтаксис:
class Class:
   @classmethod
   def method(cls, arg1, arg2, ...): ...


class MyClass:
   @classmethod
   def classmethod(cls):
       print('Class method called')

# Функцию classmethod также можно вызывать без создания экземпляра класса, но его определение следует за подклассом, а не за родительским классом, через наследование.

MyClass.classmethod()

# @classmethod используется, когда вам нужно получить методы, не относящиеся к какому-либо конкретному экземпляру, но каким-то образом привязанные к классу. Самое интересное в них то, что их можно переопределить дочерними классами.

# Поэтому, если вы хотите получить доступ к свойству класса в целом, а не к свойству конкретного экземпляра этого класса, используйте classmethod.

class ParentClass():
  
   TOTAL_OBJECTS=0
  
   def __init__(self):
       ParentClass.TOTAL_OBJECTS = ParentClass.TOTAL_OBJECTS+1
     
   @classmethod
   def total_objects(cls):
       print("Total objects: ",cls.TOTAL_OBJECTS)

# Создаем объекты       

my_obj1 = ParentClass()
my_obj2 = ParentClass()
my_obj3 = ParentClass()

# Вызываем classmethod

ParentClass.total_objects()

# Теперь, если мы унаследуем этот класс в дочерний класс и объявим там переменную TOTAL_OBJECTS и вызовем метод класса из дочернего класса, он вернет общее количество объектов для дочернего класса.

# Создаем дочерний класс
class ChildClass(ParentClass):
  
   TOTAL_OBJECTS=0

   def __init__(self):
       super().__init__()
       ChildClass.TOTAL_OBJECTS = ChildClass.TOTAL_OBJECTS+1

chil_obj = ChildClass()

ParentClass.total_objects()

ChildClass.total_objects()

# @classmethod используется в суперклассе для определения того, как метод должен вести себя, когда он вызывается разными дочерними классами. В то время как @staticmethod используется, когда мы хотим вернуть одно и то же, независимо от вызываемого дочернего класса.

# вызов @classmethod включает в себя дополнительное выделение памяти, чего нет при вызове @staticmethod или обычной функции.

```
