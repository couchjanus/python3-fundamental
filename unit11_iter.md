# Итераторы

Итераторы представляют собой инструменты, которые используются для поточной обработки данных. 

Во многих современных языках программирования используют такие сущности как итераторы. Основное их назначение – это упрощение навигации по элементам объекта, который представляет собой некоторую коллекцию (список, словарь и т.п.). Язык Python, в этом случае, не исключение и в нем тоже есть поддержка итераторов. Итератор представляет собой объект перечислитель, который для данного объекта выдает следующий элемент, либо бросает исключение, если элементов больше нет.

Основное место использования итераторов – это цикл for. Если вы перебираете элементы в некотором списке или символы в строке с помощью цикла for, то это означает, что при каждой итерации цикла происходит обращение к итератору, содержащемуся в строке/списке, с требованием выдать следующий элемент, если элементов в объекте больше нет, то итератор генерирует исключение, обрабатываемое в рамках цикла for незаметно для пользователя.

## выведем элементы произвольного списка на экран.
```py

num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)

```
## исключение StopIteration
объекты, элементы которых можно перебирать в цикле for, содержат в себе объект итератор, для того, чтобы его получить необходимо использовать функцию iter(), а для извлечения следующего элемента из итератора – функцию next().
```py
# working of iter() 

itr = iter(num_list)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# Traceback (most recent call last):
#   File "01.py", line 19, in <module>
#     print(next(itr))
# StopIteration

  
# initializing list  
lis1 = [1, 2, 3, 4, 5] 
  
# printing type  
print ("The list is of type : " + str(type(lis1))) 
  
# converting list using iter() 
lis1 = iter(lis1) 
  
# printing type  
print ("The iterator is of type : " + str(type(lis1))) 
  
# using next() to print iterator values 
print (next(lis1)) 
print (next(lis1)) 
print (next(lis1)) 
print (next(lis1)) 
print (next(lis1)) 

```

вызов функции next(itr) каждый раз возвращает следующий элемент из списка, а когда эти элементы заканчиваются, генерируется исключение StopIteration.
```py

# Properties of Iterators

# Iteration object remembers iteration count via internal count variable.
# Once the iteration is complete, it raises a StopIteration exception and iteration count cannot be reassigned to 0.
# Therefore, it can be used to traverse the container just once.
  
# initializing list  
lis1 = [1, 2, 3, 4, 5] 
  
# converting list using iter() 
lis1 = iter(lis1) 
  
# prints this  
print ("Values at 1st iteration : ") 
for i in range(0, 5): 
    print (next(lis1)) 
  
# doesn't print this 
print ("Values at 2nd iteration : ") 
for i in range(0, 5): 
    print (next(lis1)) 

```

## Функция iter

Возвращает объект итератора.
```py

iter(obj[, sentinel]) -> iterator

```
- obj : Объект коллекции, поддерживающей итерирование (реализует __iter__()), либо объект, поддерживающий протокол последовательности (реализует __getitem__(), где аргумент целое, начиная с нуля). Если передан другой объект, возбуждается TypeError.
- sentinel : Если этот аргумент предоставлен, то ожидается, что obj содержит объект, поддерживающий вызов. В этом случае, созданный итератор будет вызывать указанный объект (без аргументов) с каждым обращением к своему __next__() и проверять полученное значение на равенство с sentinel. Если полученное значение равно sentinel, возбуждается StopIteration, иначе возвращается полученное значение.
Функция возвращает итератор по объекту, поддерживающему итерирование по его элементам.

## sentinel
В зависимости от наличия sentinel, в obj ожидаются различные типы объектов.
Одно из применений sentinel — чтение строк, пока не будет достигнута нужная. 
Следующий пример считывает файл, пока метод readline() не вернёт пустую строку:

```py
# callable objects in the presence of sentinel

with open('example.txt') as fp:
    for line in iter(fp.readline, ''):
        print(line[0])

# Here, the program will read the lines of file example.txt, until the sentinel character  ' ' (empty string) is encountered.

```

Python имеет несколько встроенных объектов, реализующих протокол итератора: списки, кортежи, строки, словари и файлы.

## встроенный итератор для строки
```py

str = "formidable"

for e in str:
   print(e, end=" ")

print()

# В Python строка - это неизменная последовательность символов. 
# Функция iter() возвращает итератор для объекта. 

it = iter(str)

print(it.next())
print(it.next())
print(it.next())

print(list(it))

```
Мы также можем использовать функции list() или tuple()

при работе с итераторами мы можем получить следующий элемент в последовательности, не сохраняя весь набор данных в памяти.

```py

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

```

## Итерируемый класс Stack
Если вы хотите, чтобы ваш собственный класс был итерируемым, добавьте метод __iter__(). 
```py

class Stack:
    
    def __init__(self, data = None):
        # create a list that store data
        if data == None:
            self.stack = list()
        elif isinstance(data, list):
            self.stack = data
        else:
            raise ValueError('input data should be list')

    def __iter__(self):
        return iter(self.stack)

# Now you can do this:

mystack = Stack([4,6,2,1,6,3])


for x in mystack:
  print(x)

```

## Создание собственных итераторов

Если нужно обойти элементы внутри объекта вашего собственного класса, необходимо построить свой итератор. Создадим класс, объект которого будет итератором, выдающим определенное количество единиц, которое пользователь задает при создании объекта. Такой класс будет содержать конструктор, принимающий на вход количество единиц и метод __next__(), без него экземпляры данного класса не будут итераторами.
```py

class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter1 = SimpleIterator(3)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
# при четвертом вызове функции next() будет выброшено исключение StopIteration. 
```
Если мы хотим, чтобы с данным объектом можно было работать в цикле for, то в класс SimpleIterator нужно добавить метод __iter__(), который возвращает итератор, в данном случае этот метод должен возвращать self.
```py
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)
```
## Пользовательский тип, определивший __call__():
```py
    class MyIterable(object):

        def __init__(self):
            self.index = 0
            self.items = [1, 2, 3, 4]

        def __call__(self):
            value = self.items[self.index]
            self.index += 1
            return value


    iterator = iter(MyIterable(), 3)

    print(next(iterator))  # 1
    print(next(iterator))  # 2
    print(next(iterator))  # StopIteration
```
Для получения следующего элемента из объекта итератора вручную можно воспользоваться функцией next. Автоматический проход по элементам возможен при использовании цикла for in.

## Итерируемый объект, итератор и генератор

## Паттерн Итератор(Iterator)
Назначение:
- для доступа к содержимому агрегированных объектов без раскрытия их внутреннего представления;
- для поддержки нескольких активных обходов одного и того же агрегированного объекта (не обязательно);
- для предоставления единообразного интерфейса с целью обхода различных агрегированных структур.

разделение ответственности: клиенты получают возможность работать с разными коллекциями унифицированным образом, а коллекции становятся проще за счет того, что делегируют перебор своих элементам другой сущности.

## Существуют два вида итераторов, внешний и внутренний.
1. Внешний итератор — это классический (pull-based) итератор, когда процессом обхода явно управляет клиент путем вызова метода Next.
2. Внутренний итератор — это push-based-итератор, которому передается callback функция, и он сам уведомляет клиента о получении следующего элемента.

## Классическая реализауия паттерна Итератор:
- Aggregate — составной объект, по которому может перемещаться итератор;
- Iterator — определяет интерфейс итератора;
- ConcreteAggregate — конкретная реализация агрегата;
- ConcreteIterator — конкретная реализация итератора для определенного агрегата;
- Client — использует объект Aggregate и итератор для его обхода.

## Реализация классического итератора

## Абстрактные классы:
```py
class Aggregate(abc.ABC):

    @abc.abstractmethod
    def iterator(self):
        """
        Возвращает итератор
        """
        pass


class Iterator(abc.ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        """
        Возвращает итератор к началу агрегата.
        Так же называют reset
        """
        pass

    @abc.abstractmethod
    def next(self):
        """
        Переходит на следующий элемент агрегата.
        Вызывает ошибку StopIteration, если достигнут конец последовательности.
        """
        pass

    @abc.abstractmethod
    def current(self):
        """
        Возвращает текущий элемент
        """
        pass
```
## реализация итератора для списка:
```py
class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        """
        :param collection: список
        :param cursor: индекс с которого начнется перебор коллекции.
        так же должна быть проверка -1 >= cursor < len(collection)
        """
        super().__init__(collection, cursor)

    def first(self):
        """
        Начальное значение курсора -1.
        Так как в нашей реализации сначала необходимо вызвать next 
         который сдвинет курсор на 1.
        """
        self._cursor = -1

    def next(self):
        """
        Если курсор указывает на послений элемент, то вызываем StopIteration,
        иначе сдвигаем курсор на 1
        """
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        """
        Возвращаяем текущий элемент
        """
        return self._collection[self._cursor]


## реализация агрегата:
```py
class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)
```

Теперь мы можем создать объект коллекции и обойти все ее элементы с помощью итератора:
```py
collection = (1, 2, 5, 6, 8)
aggregate = ListCollection(collection)
itr = aggregate.iterator()

# обход коллекции
while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())
```

А так как мы реализовали метод first, который сбрасывает итератор в начальное состояние, то можно воспользоваться этим же итератором еще раз:
```py
# возвращаем итератор в исходное состояние
itr.first()

while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())
```

Реализации могут быть разные, но основная идея в том, что итератор может обходить различные структуры, вектора, деревья, хеш-таблицы и много другое, при этом имея снаружи одинаковый интерфейс.


## Протокол итерирования в Python

Минимальный интерфейс класса Iterator состоит из операций First, Next, IsDone и CurrentItem. Но если очень хочется, то этот интерфейс можно упростить, объединив операции Next, IsDone и CurrentItem в одну, которая будет переходить к следующему объекту и возвращать его. Если обход завершен, то эта операция вернет специальное значения(например, 0), обозначающее конец итерации.

Именно так и реализовано в Python, но вместо специального значения, о конце итерации говорит StopIteration. Проще просить прощения, чем разрешения.

Рассмотрим итерируемый объект (Iterable). В стандартной библиотеке он объявлен как абстрактный класс collections.abc.Iterable:
```py
class Iterable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            return _check_methods(C, "__iter__")
        return NotImplemented
```

У него есть абстрактный метод __iter__ который должен вернуть объект итератора. И метод __subclasshook__ который проверяет наличие у класса метод __iter__. Таким образом, получается, что итерируемый объект это любой объект который реализует метод __iter__
```py
class SomeIterable1(collections.abc.Iterable):
    def __iter__(self):
        pass

class SomeIterable2:
    def __iter__(self):
        pass

print(isinstance(SomeIterable1(), collections.abc.Iterable))
# True
print(isinstance(SomeIterable2(), collections.abc.Iterable))
# True
```
## Функция iter()
Функция iter() используется в цикле for для получения итератора. Функция iter() в первую очередь для получения итератора из объекта, вызывает его метод __iter__. Если метод не реализован, то она проверяет наличие метода __getitem__ и если он реализован, то на его основе создается итератор. __getitem__ должен принимать индекс с нуля. Если не реализован ни один из этих методов, тогда будет вызвано исключение TypeError.
```py
from string import ascii_letters

class SomeIterable3:
    def __getitem__(self, key):
        return ascii_letters[key]

for item in SomeIterable3():
    print(item)

```
Итерируемый объект — это любой объект, от которого встроенная функция iter() может получить итератор. Последовательности(abc.Sequence) всегда итерируемые, поскольку они реализуют метод __getitem__

Итератор в Python представлен абстрактным классом collections.abc.Iterator:
```py
class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented

```
__next__ Возвращает следующий доступный элемент и вызывает исключение StopIteration, когда элементов не осталось.
__iter__ Возвращает self. Это позволяет использовать итератор там, где ожидается итерируемых объект, например for.
__subclasshook__ Проверяет наличие у класса метода __iter__ и __next__

Итератор в python — это любой объект, реализующий метод __next__ без аргументов, который должен вернуть следующий элемент или ошибку StopIteration. Также он реализует метод __iter__ и поэтому сам является итерируемым объектом.

Таким образом можно реализовать итерируемый объект на основе списка и его итератор:
```py
class ListIterator(collections.abc.Iterator):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        return self._collection[self._cursor]

class ListCollection(collections.abc.Iterable):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return ListIterator(self._collection, -1)


# Варианты работы:

collection = [1, 2, 5, 6, 8]
aggregate = ListCollection(collection)

for item in aggregate:
    print(item)

print("*" * 50)

itr = iter(aggregate)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break
```
Функция next() вызывает метод __next__. Ей можно передать второй аргумент который она будет возвращать по окончанию итерации вместо ошибки StopIteration.
```py
itr = iter(aggregate)
while True:
    item = next(itr, None)
    if item is None:
        break
    print(item)
```
