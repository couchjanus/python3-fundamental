# Generator (генератор)
Словом генератор обычно обозначается функция-генератор (или метод-генератор), возвращающая итератор генератора. Однако иногда слово может быть использовано и для обозначения самого итератора. В случаях, когда контекст непонятен лучше использовать полные термины: функция-генератор и итератор генератора. Итератор генератора — это объект, порождаемый функцией-генератором.

Когда вы создаёте список (list) вы можете считывать его элементы по одному — это называется итерацией.
```py
lst = [1, 2, 3]

for i in lst:
    print(i)
```
lst — итерируемый объект (iterable). Когда вы используете списковые выражения (list comprehensions), вы создаёте список — итерируемый объект:
```py
st = [x*x for x in range(3)]
for i in st:
    print(i)
```
Любое объект который вы можете использовать в конструкции for … in … является итерирумым: списки, строки, файловые объекты и т.п.. Итерирумые объекты достаточно удобны потому что вы можете считывать из них столько данных, сколько вам необходимо, но при этом вы храните все значения последовательности в памяти и это не всегда приемлемо, особенно если вы имеете достаточно большие последовательности.

## Генераторы
Генераторы — итерируемые объекты, но, в общем случае, вы можете их использовать только один раз. Генераторы не хранят все значения в памяти, а генерируют значения на лету — по мере запроса:
```py
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
```
Код выглядит почти так же, как и в предыдущем примере, только вместо квадратных скобок («[<…>]») были использованы круглые («(<…>)»). вы не можете выполнить цикл по generator во второй раз, поскольку ничего в памяти не хранится, попытка пройтись второй раз будет просто проигнорирована, т.к. generator выбросит при первом запросе на получение следующего значения StopIterationError, однако, вы это не заметите, если будете использовать цикл for, это исключение будет перехвачено и интерпретировано как конец цикла). 
```py
# это можно проверить:
generator.next()
# next — это метод для получения следующего значения генератора, 
# если вы его используете не в цикле for.
# StopIteration:
```
## Yield 
Yield — это ключевое слово которое используется так же, как и слово return. Разница в том, что функция при этом начинает возвращать генератор вместо значения.
```py
def generator():
for i in (1, 2, 3):
    yield i

g = generator() # create a generator
rint(g) # <generator object generator at 0x2e58870>
for i in g:
    print(i)
```
когда вы вызываете функцию, в теле которой находится yield, выполнение этой функции не происходит. Вместо выполнения, функция вернёт объект-генератор. Код будет выполнятся при каждой итерации — будь то цикл «for <…> in <generator>» или вызов метода <generator>.next().

При первом исполнении кода тела функции код будет выполнен с начала и до первого встретившегося оператора yield. После этого будет возвращено первое значение и выполнение тела функции опять приостановлено. Запрос следующего значения у генератора во время итерации заставит код тела функции выполняться дальше (с предыдущего yield), пока не встретится следующий yield. Генератор считается закончившимся в случае если при очередном исполнении кода тела функции не было встречено ни одного оператора yield.

## Функции генератора
Выглядят функции-генераторы также как и обычные, но содержат выражения с ключевым словом yield для последовательного генерирования значений, которые могут быть использованы в циклах for in, либо их получения при помощи функции next().

Чтобы создать генератор, необходимо определить функцию, как обычно, но использовать yield вместо return, указывая интерпретатору, что эту функцию следует рассматривать как итератор:
```py
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
```
Оператор yield приостанавливает функцию и сохраняет локальное состояние, чтобы его можно было возобновить с того места, где оно было остановлено.

Что происходит, когда вы вызываете эту функцию?
```py
val = countdown(5)
val # <generator object countdown at 0x10213aee8>
```
Вызов функции не выполняет ее. Вместо этого функция возвращает объект-генератор, который используется для управления выполнением.

Объекты генератора выполняются при вызове next():
```py
next(val)
```
При первом вызове next() выполнение начинается с начала тела функции и продолжается до следующего оператора yield, где возвращается значение справа от оператора, последующие вызовы next() продолжаются с оператора yield до конец функции, затем новый обход цикла и продолжение с начала тела функции, пока не будет вызван другой выход. Если yield не вызывается (что в нашем случае означает, что условие while не отрабатывается, потому что num <= 0), возникает исключение StopIteration:
```py
next(val)
next(val)
next(val)
next(val)
next(val)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

y = yrange(3)
print(y) # <generator object yrange at 0x401f30>
```

## Генераторы являются простым средством для создания итераторов. 
Всё, что можно сделать при помощи генераторов можно также сделать при помощи итераторов, построенных на классах. 
```py
# в случае генераторов методы __iter__() и __next__() создаются автоматически
next(y)
next(y)
next(y)
next(y)

# также автоматически возбуждается StopIteration

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>

# StopIteration
```
поддерживать генераторы проще и удобнее, чем реализовывать то же с использованием классов.

На каждой yield работа функции временно приостанавливается, при этом сохраняется состояние исполнения, включая локальные переменные, указатель на текущую инструкцию, внутренний стек и состояние обработки исключения. При последующем обращении к итератору генератора (при вызовах его методов) функция продолжает своё исполнение с места, на котором была приостановлена. Этим функции-генераторы отличаются от обычных функций, при вызове которых исполнение всякий раз начинается с начала.

Если функция достигает инструкции return, либо конца (без указания упомянутой инструкции), возбуждается исключение StopIteration и итератор исчерпывает себя.
```py
    def my_animal_generator():

        yield 'корова'

        for animal in ['кот', 'собака', 'медведь']:
            yield animal

        yield 'кит'


    for animal in my_animal_generator():
        print(animal)
        # корова кот собака медведь кит
```

Функции-генераторы похожи на coroutin: могут выдывать значения несколько раз, имеют более одной точки входа, их выполнение может быть приостановлено. Единственным различием является то, что функции-генераторы не могут определять то, что должно происходить после выдачи значения — управление всегда передаётся коду, вызвавшему генератор.
```py
# The program creates a very simple generator.
def gen():

   x, y = 1, 2
   yield x, y
   
   x += 1
   yield x, y
```
Инструкция yield может употребляться и в конструкции try except. Если к генератору не обратились до его финализации (финализация происходит, когда счётчик ссылок доходит до нуля, либо когда происходит сборка мусора), будет вызван метод итератора .close(), что позволяет выполнить оставшиеся в блоке finally инструкции.
```py
def gen():
   x, y = 1, 2
   yield x, y
  
   x += 1
   yield x, y

g = gen()

print(next(g))
print(next(g))

try:
   print(next(g))
   
except StopIteration:
   print("Iteration finished")

# (1, 2)
# (2, 2)

# yield and call to __next__ method on generator object.

def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")

f = foo()
next(f)
next(f)
next(f)
next(f)

# Infinite sequence of integers:

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

print(take(5, squares())) # prints [1, 4, 9, 16, 25]
```

генератор, подобно итератору, запоминает последний момент, когда к нему обращались, но при этом оперирует не абстрактными элементами, а конкретными блоками кода. 
То есть если итератор по умолчанию будет перебирать элементы в контейнере, пока они не кончатся, то генератор будет гонять код, пока не выполнится какое-нибудь конкретное условие возврата.
```py
def my_generator(step=4):
  with open("file.txt", "r") as f:
    for l in f:
      if "foo" in l:
        yield l

myiterator = my_generator()

for item in myiterator:
  print(item)

## вывод из файла file.txt всех строк, где есть подстрока "foo"
```

## Чтение нескольких файлов
```py
## like cat command in unix

# Допустим, мы хотим написать программу, которая принимает список имен файлов в качестве аргументов и печатает содержимое всех этих файлов, как команда cat в unix.

# Традиционный способ реализации:

def cat(filenames):
    for f in filenames:
        for line in open(f):
            print(line, end="")

## like grep command in unix
# Теперь предположим, что мы хотим напечатать только строку с определенной подстрокой

def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print(line, end="")
```
Обе эти программы имеют много общего кода. Трудно перенести общую часть в функцию. 
Но с генераторами это возможно.
```py
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print(line, end="")

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

```
## Это генератор чисел Фибоначчи:
```py
# Fibonacci numbers
class FibonacciGenerator:
    def __init__(self):
        self.prev = 0
        self.cur = 1

    def __next__(self):
        result = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        return result

    def __iter__(self):
        return self

for i in FibonacciGenerator():
    print(i)
    
    if i > 100:
        break


## используя ключевое слово yield можно сильно упростить реализацию:

def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

for i in fibonacci():
    print(i)
    if i > 100:
        break
```

Любая функция в Python, в теле которой встречается ключевое слово yield, называется генераторной функцией — при вызове она возвращает объект-генератор.

Объект-генератор реализует интерфейс итератора, соответственно с этим объектом можно работать, как с любым другим итерируемым объектом.
```py
fib = fibonacci()
print(next(fib))
print(next(fib))

for num, fib in enumerate(fibonacci()):
    print('{0}: {1}'.format(num, fib))
    if num > 9:
        break


# fibonacci_gen

import time

def fib():
   a, b = 0, 1
   while True:
      yield b
      a, b = b, a + b

g = fib()

try:
   for e in g:
      print(e)
      
      time.sleep(1)
            
except KeyboardInterrupt:
   print("Calculation stopped")

```
## метод send.

У объектов-генераторов еще есть метод send, который на первый взгляд тоже кажется довольно бесполезным

Если вызвать метод send у генератора, тогда yield внутри функции-генератора вернет значение, отправленное методом send. По умолчанию yield возвращает значение None.

Напишем такую функцию-генератор. Если yield возвращает None, то к i прибавляется единица, если же нет, то i становится равным x. Так можно в генератор посылать новое значение, с которого начнет итерироваться i снова.
```py

# метод send.
# у объекта генератора появилось еще несколько методов: .close(), .throw() и .send(). И это привело, можно сказать, к революции в области Data Flow Programming. С помощью .close() теперь можно извне заставить генератор остановиться на следующем обращении к нему, а с помощью .throw() — заставить его бросить исключение:

import itertools

def my_generator3():
  # Бесконечный счетчик
  counter = itertools.count()
  while True:
    yield next(counter)

myiterator = my_generator3()
myiterator2 = my_generator3()

for item in myiterator:
  print(item, end=" ")
  if item == 3:
    # Корректно завершаем генератор
    myiterator.close()

for item in myiterator2:
  print(item, end=" ")
  if item == 2:
    # Все плохо
    myiterator2.throw(Exception("Everything is bad"))

## 0 1 2 3

## 0 1 2 Traceback (most recent call last):
## File "test.py", line 28, in &lt;module&gt;
## myiterator2.throw(Exception("Everything is bad"))
## File "test.py", line 12, in my_generator3
## yield next(counter)
## Exception: Everything is bad

# метод .send() позволяет отправить данные в генератор перед вызовом следующего блока кода!

def my_coroutine():
  # Бесконечный счетчик
  counter = itertools.count()
  while True:
    y = (yield next(counter))
    if y:
      # Меняем начало отсчета
      counter = itertools.count(y)

myiterator = my_coroutine()

for item in myiterator:
  print(item, end=" ")
  if item == 1:
    # Отправляем число в генератор
    myiterator.send(4)
  elif item == 6:
    myiterator.close()
## 0 1 5 6

# по вызову yield (как, в общем случае, и return) происходит передача управления. Сопрограмма сама решает, когда перенаправить flow в другое место (например, в другую сопрограмму). И это позволяет строить красивые разветвленные деревья обработки потоков данных. 

```
## Как использовать объекты с бесконечной генерацией чисел?
```py
# Модуль itertools содержит специальные функции для работы с итерируемыми объектами. Желаете продублировать генератор? Соединить два генератора последовательно? Сгруппировать значения вложенных списков в одну строчку? Применить map или zip без создания ещё одного списка?
import itertools
# Просто добавьте import itertools.

# Давайте посмотрим на возможные порядки финиширования на скачках (4 лошади):

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
# <itertools.permutations object at 0xb754f1dc>
print(list(itertools.permutations(horses)))

# Как использовать объекты с бесконечной генерацией чисел?
# Функция islice принимает как минимум объект-генератор и значение, до которого нужно итерироваться. Возвращает конечный итератор.

from itertools import islice
def gener():
    i = 0
    while True:
        yield i
        i += 1

for i in islice(gener(), 5):
    print(i),

# 0 1 2 3 4
```

## Можно написать аналог функции islice, используя генератор.
```py
def gener(*args):
    if args == []:
        step = 1
    else:
        step = args[0]
    i = yield
    while True:
        x = yield i
        if not x:
            i += step
        else:
            i = x

def slice(gen, start, stop, step):
    g = gen(step)
    g.send(None)
    x = g.send(start)
    yield x
    
    while True:
        x = next(g)
        if x < stop:
            yield x
        else:
            raise StopIteration

for i in slice(gener, 0, 10, 2):
    print(i)

```

## Свой вариант range:
```py
def cool_range(start, stop, inc):
    x = start
    while x < stop:
        yield x
        x += inc

for n in cool_range(1, 5, 0.5):
    print(n)

print(list(cool_range(0, 2, 0.5))) # [0, 0.5, 1.0, 1.5]
```

## Yield from
Для обхода ограниченно вложенных структур, традиционный подход использовать вложенные циклы. Тот же подход можно использовать когда генераторная функция должна отдавать значения, порождаемые другим генератором.

Функция похожая на itertools.chain:
```py
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

g = chain([1, 2, 3], {'A', 'B', 'C'}, '...')
print(list(g))
# [1, 2, 3, 'A', 'B', 'C', '.', '.', '.']


# Но вложенные циклы можно убрать, добавив конструкцию yield from:

def chain(*iterables):
    for it in iterables:
        yield from it

g = chain([1, 2, 3], {'A', 'B', 'C'}, '...')
print(list(g))
# [1, 2, 3, 'A', 'B', 'C', '.', '.', '.']

```
Основная польза yield from в создании прямого канала между внутренним генератором и клиентом внешнего генератора. 

Функция принимающая итерируемый объект, с любым уровнем вложенности другими итерируемыми объектами, и формирующая плоскую последовательность:
```py
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    """
      str, bytes - являются итерируемыми объектами,
       но их хотим возвращать целыми
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8, ('A', {'B', 'C'})]

for x in flatten(items):
    print(x)
```


## Генераторы отлично работают и для рекурсивного парсинга веб-страниц:
```py
import requests
import re
def get_pages(link):
    links_to_visit = []
    links_to_visit.append(link)
    while links_to_visit:
        current_link = links_to_visit.pop(0)
        page = requests.get(current_link)
        for url in re.findall('<a href="([^"]+)">', str(page.content)):
            if url[0] == '/':
                url = current_link + url[1:]
            pattern = re.compile('https?')
            if pattern.match(url):
                links_to_visit.append(url)
        yield current_link
webpage = get_pages('http://sample.com')
for result in webpage:
    print(result)

```