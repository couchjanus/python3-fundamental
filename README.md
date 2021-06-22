# python3-fundamental

Первый код языка Python написан в 1989 году сотрудником голландского института CWI Гвидо ван Россумом (Guido van Rossum). 

На Python существенное влияние оказали языки программирования ABC, C и Modula-3. До 2018 Гвидо занимал пост великодушного пожизненного диктатора - Benevolent Dictator For Life (BDFL) Python. BDFL означает, что дактар продолжает наблюдать за процессом разработки Python, принимая окончательные решения, когда это необходимо.

В 2008 году вышла 3-я версия языка.

Python - высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. 

Синтаксис ядра Python минималистичен. стандартная библиотека включает большой объём полезных функций.

Python поддерживает структурное, объектно-ориентированное, функциональное, императивное и аспектно-ориентированное программирование. 

Основные архитектурные черты - динамическая типизация, автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений, высокоуровневые структуры данных. 

Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты.

Развитие языка происходит согласно регламентированному процессу создания, обсуждения, отбора и реализации документов PEP (Python Enhancement Proposal) - предложений по развитию Python. В настоящий момент Python занимает 2 место в рейтинге TIOBE с показателем 11.84%. 

Python назван в честь BBC-шоу «Летающий цирк Монти Пайтона» и не имеет ничего общего с рептилиями. 

Python – это интерпретируемый язык программирования: исходный код частями преобразуется в машинный в процессе выполнения программой-интерпретатором.

Python – это полноценный, универсальный, язык программирования. Он разрабатывался как объектно-ориентированный язык.

Python даёт возможность писать компактные и читабельные программы. 
Программы, написанные на Python отличаются большей краткостью чем эквиваленты на C, C++ или Java, по нескольким причинам:
- высокоуровневые типы данных позволяют выражать сложные операции в одной инструкции;
- группировка инструкций выполняется отступами, а не операторными скобками;
- нет необходимости в описании переменных и аргументов.

Python используется во многих компаниях: Dropbox, Google (Youtube, Youtube API), Facebook, Instagram.
Python используется как универсальная среда для научных расчётов с пакетами NumPy, SciPy, Astropy и MatPlotLib.
В программах трёхмерной графики, таких как Autodesk Maya, Blender, Houdini и Nuke, Python используется для расширения стандартных возможностей программ. В
Microsoft Power BI Desktop Python используется на этапе загрузки данных в ETL-процессах, расчётах и графической визуализации данных. 
В проекте Google Test Python используется для генерации исходного кода mock-объектов для классов языка C++.

Python поставляется с системой Linux, во многих дистрибутивах инсталляторы и визуальный интерфейс системных утилит написаны на Python. Используется он и в администрировании других Unix-систем, в частности, в Solaris и macOS. 

Эталонной реализацией Python является интерпретатор CPython, поддерживающий большинство активно используемых платформ. Он распространяется под свободной лицензией Python Software Foundation License, позволяющей использовать его без ограничений в любых приложениях, включая проприетарные. 

Есть реализация интерпретатора для JVM с возможностью компиляции, CLR, LLVM, другие независимые реализации. Проект PyPy использует JIT-компиляцию, которая значительно увеличивает скорость выполнения Python-программ.

Python - активно развивающийся язык программирования, новые версии выходят примерно раз в два с половиной года. Язык не подвергался официальной стандартизации, роль стандарта де-факто выполняет CPython, разрабатываемый под контролем автора языка. 
## Интерпретатор Python
Интерпретатор Python в CPython использует потоко-небезопасные данные, во избежание разрушения которых при совместной модификации из разных потоков применяется глобальная блокировка интерпретатора - GIL (Global Interpreter Lock). 
В ходе исполнения кода поток интерпретатора блокирует GIL, выполняет некоторое количество инструкций (по умолчанию 100), после чего освобождает блокировку и приостанавливается, давая возможность работать другим потокам. 
GIL также освобождается во время ввода-вывода, изменения и проверки состояния синхронизирующих примитивов, при исполнении кода расширений, не обращающихся к данным интерпретатора. 
Таким образом, в каждый момент времени в одном процессе интерпретатора Python может исполняться только один поток кода на Python, независимо от числа доступных процессорных ядер.

## Установить python
Для Windows: Загрузите установщик Python 3 с официального сайта https://python.org/downloads/windows/.
Для Mac Os: Загрузить и установить Python с помощью Homebrew brew: brew install python3

Установить python3 для Debian, Ubuntu, Mint,:
```bash
	$ sudo add-apt-repository ppa:deadsnakes/ppa
	$ sudo apt-get update
	$ sudo apt-get install python3.9
```
Установить python3 для CentOS: 
```bash
$ sudo yum install python39u
$ sudo yum install python39u-pip
```
Установить python3 для Fedora: $ sudo dnf install python39
Установить python3 для Arch Linux: $ packman -S python

Есть несколько веб-сайтов, где вы можете взаимодействовать с интерпретатором Python онлайн:

	Python.org Online Console: www.python.org/shell 
	Python Fiddle: pythonfiddle.com
	Repl.it: repl.it
	Trinket: trinket.io
	Python Anywhere: www.pythonanywhere.com

Python может использоваться в интерактивном режиме, при котором введённые с клавиатуры операторы сразу же выполняются, а результат выводится на экран (REPL). 

Термин REPL является аббревиатурой от Read, Evaluate, Print and Loop:
- Read - Прочитать ввод пользователя
- Evaluate - Оценить свой код
- Print - Напечатать результаты (ответ компьютера)
- Loop - Вернитесь к шагу 1.

Этот режим удобен как при изучении языка, так и в процессе профессиональной разработки - для быстрого тестирования отдельных фрагментов кода, - так как обеспечивает немедленную обратную связь. 

Интерпретатор Python после установки располагается, обычно, в /usr/local/bin/python3.x. На машинах с ОС Windows, инсталляция Python обычно осуществляется в каталог C:\Python3x, но он может быть изменен во время установки. 

Добавление каталога /usr/local/bin к пути поиска Unix-шелла (переменная PATH) позволит запустить интерпретатор набором команды python. Чтобы добавить этот каталог к пути поиска в Windows, вы можете набрать в окне DOS следующую команду:
set path=%path%;C:\python3x

## Запуск интерпретатора
Интерпретатор работает в двух режимах: интерактивном и интерпретатора. Вход в интерактивный режим осуществляется вводом python без параметров, параметр file вызывает интерпретацию указанного файла.

Запуск интерпретатора осуществляется командой python. В интерактивном режиме интерпретатор отображает основное приглашение (обычно три знака больше - >>>). Перед выводом первого приглашения интерпретатор выдает приветственное сообщение, содержащее номер его версии и пометку о правах копирования:
```python


python
Python 3.8.0 (default, Oct 14 2019, 23:13:30)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
REPL позволяет использовать интерпретатор в качестве калькулятора с большим набором функций: вы вводите выражение, а в ответ он выводит значение. 
>>> 2+2
```

Заставить Python интерпретировать введенную строку можно клавишей Enter.
Для группировки можно использовать скобки:
```python


>>> (50-5*6)/4 # 5.0
>>> 8/5 # 1.6000000000000001 При делении целых чисел дробные части не теряются
>>> print(8/5) # 1.6
Для получения целого результата при делении целых чисел предназначена операция: //:
>>> # Деление целых чисел возвращает округленное к минимальному значению:
... 7//3 # 2
>>> 7//-3 # -3
```
Присутствует полная поддержка операций с плавающей точкой. Операции над операндами смешанного типа конвертируют целочисленный операнд в число с плавающей запятой.
```python


>>> 2 * 2 + 8 / 2 # 8.0
>>> 2 * (2 + 8) / 2  # 10.0
>>> 2 ** 2 ** 2 # 16
>>> 3 ** 3 ** 3 # 7625597484987
>>> 3**3 # 27
>>> 27**3 # 19683
>>> 3**27 # 7625597484987
>>> "Hello"+" world"
'Hello world'
>>> "Hello"+ 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> "Hello" * 3
'HelloHelloHello'
```
Переменные в Python не требуют объявления и могут первоначально содержать любой тип данных. 
```python


>>> width = 20
>>> height = 5*9
>>> width * height
>>>some_string = “Это очень хорошая строка”
>>>some_string
```
Вначале вы можете присвоить переменной width целый тип, переменной some_string строчный тип, но впоследствие нельзя присвоить переменной width переменную some_string, так как они будут иметь разный тип:
```python


>>> width = 20
>>>some_string = “Это очень хорошая строка”
>>>width = some_string
ERROR: не могу присвоить переменные разных типов
```
Переменные должны быть определены (defined) (должны иметь присвоенное значение) перед использованием, иначе будет сгенерирована ошибка:
```python


>>> # попытка получить доступ к неопределённой переменной
... n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```
Знак равенства ('=') используется для присваивания переменной какого-либо значения:
```python


>>> width = 20
>>> height = 5*9
>>> width * height
```
Значение может быть присвоено нескольким переменным одновременно:
```python


>>> x = y = z = 0  # Нулевые x, y и z
>>> x
>>> y
>>> z
```
Продолжающие строки используются в случаях, когда необходимо ввести многострочную конструкцию. Для продолжающих строк выводится вспомогательное приглашение (по умолчанию - три точки - ...). 
Например, оператор if:
```python


>>> hey = "Hey You"
>>> if hey:
... 	print("Be careful not to fall off!")
...
Be careful not to fall off!
```
Запрашиваем у Python справочную информацию
```python


>>> help
```
В интерактивном режиме доступна система помощи (вызывается по help()), работающая для всех модулей, классов и функций, которые содержат строки документации.
Запускаем справочную утилиту
```python
>>> help()

Welcome to Python 3 help utility!
If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.
help>
Запрашиваем справку о keywords
help> keywords
help> quit

```
Язык Python включает много встроенных функций. 
Встроенная функция print() отвечает за вывод данных, по-умолчанию на экран. 
В скобках могут быть любые типы данных. Кроме того, количество данных может быть различным:
```python


print("a:", 2)
```
Можно передавать в функцию print() как литералы, так и переменные, вместо которых будут выведены их значения. Аргументы функции (то, что в скобках), разделяются между собой запятыми. 
В выводе вместо запятых значения разделены пробелом.
```python
>>>help(print)
Help on built-in function print in module builtins:
print(...)
	print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
	Prints the values to a stream, or to sys.stdout by default.
	Optional keyword arguments:
	file:  a file-like object (stream); defaults to the current sys.stdout.
	sep:   string inserted between values, default a space.
	end:   string appended after the last value, default a newline.
	flush: whether to forcibly flush the stream.
>>> print(2, 3, 4)
2 3 4
>>> print(2, ":", 3, ":", 4)
2 : 3 : 4
>>> print(2, 3, 4, sep=":")
2:3:4
>>> print(2,3,4, sep=":", end="")
2:3:4>>>
```
Для того, чтобы выйти из интерпретатора python с нулевым статусом выхода, воспользуйтесь комбинацией клавиш Ctrl-D в Unix, Ctrl-Z в Windows.
Если это не сработает - вы можете выйти из интерпретатора путем ввода команды:
```python


>>> quit()
```
Нажатие клавиш прерывания процесса (Ctrl-C или DEL), в ответ на приглашение в основном или вспомогательном режиме, отменяет ввод и возвращает вас к основному приглашению. 

Система модулей позволяет логически организовать код на Python. Группирование кода в модули значительно облегчает процесс написания и понимания программы. Модуль в Python это  просто файл, содержащий код на Python. Каждый модуль в Python может содержать переменные, объявления классов и функций. Кроме того, в модуле может находиться исполняемый код.

Вы можете использовать любой питоновский файл как модуль в другом файле, выполнив в нем команду import. Синтаксис команды import:import module_1[, module_2[,... module_N]
Python, встрая команду import, импортирует этот модуль, если он присутствует в пути поиска. Путь поиска Python это список директорий, в которых интерпретатор производит поиск перед попыткой загрузить модуль.
Если мы напечатаем в приглашении Python help('modules') или введем modules в приглашении справки, мы получим список доступных модулей.  Получаем список доступных модулей: >>> help('modules')
Запрашиваем справку о модулях с ключевыми словами
```python


>>> help('modules keywords')
```
Модуль keyword содержит ключевые слова. Открыв файл keyword.py в текстовом редакторе, можно увидеть, что Python действительно создает список ключевых слов, явно доступных в виде атрибута kwlist модуля keyword. В модуле keyword также приводятся комментарии о том, что этот модуль генерируется автоматически на основе исходного кода самого Python, гарантируя точность и полноту списка ключевых слов.

## Список ключевых слов модуля keyword:
```python


>>> import keyword
>>> keyword.kwlist
```
Разработчики языка Python придерживаются определённой философии программирования, называемой «The Zen of Python» («Дзен Питона», или «Дзен Пайтона»). Автор этой философии - Тим Петерс. Её текст выдаётся интерпретатором Python по команде import this (работает один раз за сессию).
```python


>>> import this
```
Beautiful is better than ugly. Красивое лучше, чем уродливое.
Explicit is better than implicit. Явное лучше, чем неявное.
Simple is better than complex. Простое лучше, чем сложное.
Complex is better than complicated. Сложное лучше, чем запутанное.
Flat is better than nested. Плоское лучше, чем вложенное.
Sparse is better than dense. Разреженное лучше, чем плотное.
Readability counts. Читаемость имеет значение.
Special cases aren't special enough to break the rules. Особые случаи не настолько особые, чтобы нарушать правила.
Although practicality beats purity. При этом практичность важнее безупречности.

Для того, чтобы выйти из интерпретатора python набе­рите в ответ на приглашение интерпретатора(>>>):
```python

>>> import sys 
>>> sys.exit() 

или:
>>> import sys; sys.exit() 
```
## Виртуальное окружение
Виртуальное окружение - это независимый от установленных в системе набор библиотек, модулей и самого интерпретатора Python, которые используются при работе с текущим проектом.  Главная задача виртуальной среды Python – создание изолированной среды для проектов Python. Каждый проект может иметь свои собственные зависимости, вне зависимости от того, какие зависимости у другого проекта. В Python 3 уже есть модуль venv.

## Создать virtual environment: python -m venv env

эта команда создает каталог под названием env, структура которого схожа со следующей:

├── bin
│   ├── activate
│   ├── easy_install
│   ├── pip
│   ├── python -> python3.8
│   └── python3.8 -> /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
├── include
├── lib

bin – файлы, которые взаимодействуют с виртуальной средой;
include – С-заголовки, компилирующие пакеты Python;
lib – копия версии Python вместе с папкой site-packages, в которой установлена каждая зависимость.

Также здесь присутствуют копии или символические ссылки нескольких различных инструментов Python.  Эти файлы используются для того, чтобы команды и код Python выполнялись в контексте текущей среды и, таким образом, достигается изоляция виртуальной среды от глобальной среды.

Скрипт activate в папке bin активирует настройки по умолчанию оболочки  виртуальной среды Python. Чтобы использовать пакеты в изолированной среде: source env/bin/activate

Вернуться назад в контекст «system» , позволит команда deactivate: (env) $ deactivate

После этого сеанс оболочки вернется в норму, а команда python будет ссылаться на общую установку Python. 

Существует несколько специализированных IDE для разработки на Python.
- Eric - полнофункциональный редактор Python и IDE, написанный на Python. 
- PyCharm - полнофункциональная IDE для Python от JetBrains, существует в бесплатном (Community) и платном (Professional) вариантах.
- Wing IDE - линейка Python-IDE от американской фирмы Wingware, включает три варианта: «Wing 101», «Wing Personal», «Wing Pro». 
- Spyder - open-source (MIT) IDE, ориентирована на data science, в ней удобно работать с библиотеками SciPy, NumPy, Matplotlib. 
- Существуют плагины для поддержки программирования на Python для универсальных IDE Eclipse, Atom и Microsoft Visual Studio Code.(Python-vscode, Pylint, Flake8)
## Pip
pip - это система управления пакетами, которая используется для установки и управления программными пакетами, написанными на Python. Pip - это рекурсивный акроним - Pip Installs Packages или Pip Installs Python. Начиная с Python версии 3.4, pip поставляется вместе с интерпретатором python.

Если вы используете виртуальные окружения на базе venv или virtualenv, pip уже установлен.
```python


(env) (base) ~/www/python-base $ pip --version
pip 19.2.3 from /home/janus/www/python-base/env/lib/python3.8/site-packages/pip (python 3.8)
```
Пакеты можно найти в Python Package Index (PyPI).
https://packaging.python.org/tutorials/installing-packages/ 
pip help - помощь по доступным командам.
pip install package_name - установка пакета(ов).
pip uninstall package_name - удаление пакета(ов).
pip list - список установленных пакетов.
pip show package_name - показывает информацию об установленном пакете.
pip search - поиск пакетов по имени.
pip --proxy user:passwd@proxy.server:port - использование с прокси.
pip install -U - обновление пакета(ов).
pip install --force-reinstall - при обновлении, переустановить пакет, даже если он последней версии.
## PyLint
PyLint  - программное обеспечение с открытым исходным кодом для статического анализа кода на языке программирования Python. Поддерживает рекомендации PEP 8.
Этот инструмент поможет выявлять множество фактических или потенциальных проблем в программах на языке Python.

pip install pylint --upgrade

pylint --generate-rcfile > .pylintrc

Файлы с программным кодом на языке Python обычно имеют расширение .ру, хотя в некоторых UNIX-подобных системах (таких как Linux и Mac OS X) некоторые приложения на языке Python не имеют расширения, а программы на языке Python с графическим интерфейсом, в частности в Windows и Mac OS X, обычно имеют расширение .pyw.
## PEP
Аббревиатура PEP расшифровывается как Python Enhancement Proposal (предложение по расширению Python). 
Если кто-то желает изменить или дополнить язык Python, и его стремление пользуется широкой поддержкой сообщества, он посылает PEP с подробным описанием своего предложения, чтобы его можно было рассмотреть в официальном порядке; в некоторых случаях, как это произошло с PEP 3131, предложение принимается и реализуется. 

Ключевая идея Гуидо такова: код читается намного больше раз, чем пишется. Рекомендации о стиле написания кода направлены на то, чтобы улучшить читабельность кода и сделать его согласованным между большим числом проектов. 
В идеале, весь код будет написан в едином стиле, и любой сможет легко его прочесть. 
Как говорится в PEP 20 «Читабельность имеет значение».
Все предложения PEP можно найти на странице www.py-thon.org/dev/peps/. 

Python обладает четким и последовательным синтаксисом, продуманной модульностью и масштабируемостью, благодаря чему исходный код написанных на Python программ легко читаем. 

Одной из интересных синтаксических особенностей языка является выделение блоков кода с помощью отступов (пробелов или табуляций), поэтому в Python отсутствуют операторные скобки begin/end, как в языке Паскаль, или фигурные скобки, как в Си. Такой «трюк» позволяет сократить количество строк и символов в программе и приучает к «хорошему» стилю программирования. 

С другой стороны, поведение и даже корректность программы может зависеть от начальных пробелов в тексте. 

Комментарии в Python начинаются с символа решетки # (hash) и продолжаются до физического конца строки. Комментарии могут находиться как в начале строки, так и следовать за пробельными символами или кодом, но не содержаться внутри строки. 
```python


# это первый комментарий
SPAM = 1 # а это второй комментарий
# ... и наконец третий!
STRING = "# Это не комментарий."
```
Комментарии в строке с кодом не нужны и только отвлекают от чтения, если они объясняют очевидное. Старайтесь реже использовать подобные комментарии.
```python


x = x + 1                 # Увеличиваем X на один 
>>> # Это комментарий
... 2+2
>>> 2+2  # а вот комментарий на одной строке с кодом
```
Комментарии, которые противоречат коду, хуже, чем отсутствие комментариев. Всегда исправляйте комментарии, если меняете код!  Комментарии должны являться законченными предложениями. 
Если комментарий - фраза или предложение, первое слово должно быть написано с большой буквы, если только это не имя переменной, которая начинается с маленькой буквы (кстати, никогда не отступайте от этого правила для имен переменных). Если комментарий короткий, можно опустить точку в конце предложения.  Ставьте два пробела после точки в конце предложения.

Если вы пишете по-английски, не забывайте о Strunk & White (книга Strunk & White, “Elements of style”, которая является практически эталонным руководством по правильному написанию текстов на английском языке.)

Программисты, которые не говорят на английском языке, пожалуйста, пишите комментарии на английском, если только вы не уверены на 120 процентов, что ваш код никогда не будут читать люди, не знающие вашего родного языка.

Блок комментариев обычно объясняет код (весь, или только некоторую часть), идущий после блока, и должен иметь тот же отступ, что и сам код. 

Каждая строчка такого блока должна начинаться с символа # и одного пробела после него (если только сам текст комментария не имеет отступа).
Абзацы внутри блока комментариев лучше отделять строкой, состоящей из одного символа #.

Блок комментариев обычно состоит из одного или более абзацев, составленных из полноценных предложений, поэтому каждое предложение должно заканчиваться точкой.

По умолчанию, исходники Python считаются созданными в кодировке UTF-8. В этой кодировке в строковых литералах, идентификаторах и комментариях могут быть использованы символы большинства языков мира. 
Начиная с версии python 3.0 в стандартной библиотеке действует следующее соглашение: все идентификаторы обязаны содержать только ASCII символы, и означать английские слова везде, где это возможно.  Кроме того, строки и комментарии тоже должны содержать лишь ASCII символы. 

Исключения составляют:  (а) test case, тестирующий не-ASCII особенности программы, и (б) имена авторов. 

Авторы, чьи имена основаны не на латинском алфавите, должны транслитерировать свои имена в латиницу. Проектам с открытым кодом для широкой аудитории также рекомендуется использовать это соглашение. 

Создавая элемент данных, мы можем либо присвоить его переменной, либо вставить в коллекцию. (когда в языке Python выполняется операция присваивания, в действительности происходит связывание ссылки на объект с объектом в памяти, который хранит данные.)

Имена, которые ссылаются на объекты, называются идентификаторами. Допустимый идентификатор в языке Python - это последовательность символов произвольной длины, содержащей начальный символ и ноль или более символов продолжения. 

Идентификатор должен следовать определенным правилам и соглашениям:
Имя (идентификатор) может начинаться с латинской буквы (в Python 3 - буквы любого алфавита в Unicode) любого регистра или подчеркивания, после чего в имени можно использовать и цифры. В качестве имени нельзя использовать ключевые слова и нежелательно переопределять встроенные имена. 

Имена, начинающиеся с символа подчеркивания, имеют специальное значение.

Первое правило касается начального символа и символов продолжения: 
Начальным символом может быть любой символ, который в кодировке Юникод рассматривается как принадлежащий диапазону алфавитных символов ASCII 
```python
(«а», «Ь», ..., «z», «А», «В», ..., «Z»), символ подчеркивания («__»), 
```
а также символом большинства национальных (не английских) алфавитов. 
Каждый символ продолжения может быть любым символом из тех, что пригодны в качестве начального символа, а также любым непробельным символом, включая символы, которые в кодировке Юникод считаются цифрами, такие как («О», «1», ..., «9»), и символ Каталана «•». Идентификаторы чувствительны к регистру, поэтому TAXRATE, Tax rate, TaxRate, taxRate и tax rate - это пять разных идентификаторов.

Точный перечень символов, допустимых для использования в качестве начального символа и символов продолжения, описан в справочнике Language reference, раздел Lexical analysis, подраздел Identifiers and keywords) или в PEP 31312 (раздел Supporting Non-ASCII Identifiers).

Соглашение касается использования символа подчеркивания : Не должны использоваться имена, начинающиеся и заканчивающиеся двумя символами подчеркивания. Символ подчеркивания сам по себе может использоваться в качестве идентификатора внутри интерактивной оболочки интерпретатора или в командной оболочке Python. В переменной с именем _ сохраняется результат последнего вычисленного выражения.
```python


>>> 2+2
4
>>> _
4
```
Во время выполнения обычной программы идентификатор _ отсутствует, если мы явно не определяем его в своем программном коде. Программы, которые интернационализируются, часто используют идентификатор _ в качестве имени функции перевода.

Главный принцип: Имена, которые видны пользователю как часть общественного API должны следовать конвенциям, которые отражают использование, а не реализацию.

Имена, которых следует избегать:
- Никогда не используйте символы l (маленькая латинская буква «эль»), O (заглавная латинская буква «о») или I (заглавная латинская буква «ай») как однобуквенные идентификаторы.
- В некоторых шрифтах эти символы неотличимы от цифры один и нуля. Если очень нужно l, пишите вместо неё заглавную L.
- b (одиночная маленькая буква)
- B (одиночная заглавная буква)
- lowercase (слово в нижнем регистре)
- lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
- UPPERCASE (заглавные буквы)
- UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)
CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase). 
- mixedCase первое слово начинается с маленькой буквы
- Capitalized_Words_With_Underscores 
- Ещё существует стиль, в котором имена, принадлежащие одной логической группе, имеют один короткий префикс. Этот стиль редко используется в python. 

Например, функция os.stat() возвращает кортеж, имена в котором традиционно имеют вид st_mode, st_size, st_mtime и так далее. (Так сделано, чтобы подчеркнуть соответствие этих полей структуре системных вызовов POSIX, что помогает знакомым с ней программистам).

```python
_single_leading_underscore: слабый индикатор того, что имя используется для внутренних нужд. Например, from M import * не будет импортировать объекты, чьи имена начинаются с символа подчеркивания.
single_trailing_underscore_: используется по соглашению для избежания конфликтов с ключевыми словами языка python
__double_leading_underscore: изменяет имя атрибута класса, то есть в классе FooBar поле __boo становится _FooBar__boo.
double_leading_and_trailing_underscore : магические методы или атрибуты, которые находятся в пространствах имен, управляемых пользователем. Например, init, import или file. Не изобретайте такие имена, используйте их только так, как написано в документации.
Выражение является полноправным оператором в Python. Состав, синтаксис, ассоциативность и приоритет операций достаточно привычны для языков программирования и призваны минимизировать употребление скобок.

str_title = "Smart Calculator"
print("It’s me, ", str_title)
+  Сложение - Суммирует два объекта: 3 + 5 даст 8; 'a' + 'b' даст 'ab'
-   Вычитание - Даёт разность двух чисел; если первый операнд отсутствует, он считается равным нулю:  -5.2 даст отрицательное число, а 50 - 24 даст 26.
*   Умножение - Даёт произведение двух чисел или возвращает строку, повторённую заданное число раз.:  2 * 3 даст 6. 'la' * 3 даст 'lalala'.
**  Возведение в степень    Возвращает число х, возведённое в степень y    3 ** 4 даст 81 (т.е. 3 * 3 * 3 * 3)
/   Деление - Возвращает частное от деления x на y:  4 / 3 даст 1.3333333333333333.
//  Целочисленное деление - Возвращает неполное частное от деления: 4 // 3 даст 1. -4 // 3 даст -2.
%  Деление по модулю - Возвращает остаток от деления: 8 % 3 даст 2. -25.5 % 2.25 даст 1.5.

<<  Сдвиг влево - Сдвигает биты числа влево на заданное количество позиций. (Любое число в памяти компьютера представлено в виде битов - или двоичных чисел, т.е. 0 и 1)    2 << 2 даст 8. В двоичном виде 2 представляет собой 10. Сдвиг влево на 2 бита даёт 1000, что в десятичном виде означает 8.
>>   Сдвиг вправо - Сдвигает биты числа вправо на заданное число позиций.: 11 >> 1 даст 5. В двоичном виде 11 представляется как 1011, что будучи смещенным на 1 бит вправо, даёт 101, а это, в свою очередь, не что иное как десятичное 5
&  Побитовое И - Побитовая операция И над числами: 5 & 3 даёт 1.
|    Побитовое ИЛИ - Побитовая операция ИЛИ над числами: 5 | 3 даёт 7
^   Побитовое ИСКЛЮЧИТЕЛЬНО ИЛИ - Побитовая операция ИСКЛЮЧИТЕЛЬНО ИЛИ    5 ^ 3 даёт 6
~   Побитовое НЕ Побитовая операция НЕ для числа x соответствует -(x+1):  ~5 даёт -6.
<    Меньше - Определяет, верно ли, что x меньше y. Все операторы сравнения возвращают True или False.
>   Больше - Определяет, верно ли, что x больше y: 5 > 3 даёт True. Если оба операнда - числа, то перед сравнением они оба преобразуются к одинаковому типу. В противном случае всегда возвращается False.
<=  Меньше или равно - Определяет, верно ли, что x меньше или равно y: x = 3; y = 6; x <= y даёт True.
>=  Больше или равно - Определяет, верно ли, что x больше или равно y: x = 4; y = 3; x >= 3 даёт True.
==  Равно - Проверяет, одинаковы ли объекты: x = 2; y = 2; x == y даёт True. x = 'str'; y = 'stR'; x == y даёт False. x = 'str'; y = 'str'; x == y даёт True.
!=  Не равно - Проверяет, верно ли, что объекты не равны: x = 2; y = 3; x != y даёт True.

not  Логическое НЕ - Если x равно True, оператор вернёт False. Если же x равно False, получим True.:  x = True; not x даёт False.
and  Логическое И - x and y даёт False, если x равно False , в противном случае возвращает значение y: x = False; y = True; x and y возвращает False, поскольку x равно False. В этом случае Python не станет проверять значение y, так как уже знает, что левая часть выражения ‘and’ равняется False, что подразумевает, что и всё выражение в целом будет равно False, независимо от значений всех остальных операндов. Это называется укороченной оценкой булевых (логических) выражений.
or Логическое ИЛИ - Если x равно True, в результате получим True, в противном случае получим значение y: x = True; y = False; x or y даёт True. Здесь также может производиться укороченная оценка выражений.
str_title = "Smart Calculator"
print("It’s me, ", str_title)

a = b = 2
print("a: ", a)
print("b: ", b)
# I Know Kung Fu.
print("a + b = ", a + b)
Python имеет удобные цепочечные сравнения:
a = 2
b = 0
print(1 <= a < 10 and 1 <= b < 20)
```
Логические операции (or и and) являются ленивыми: если для вычисления значения операции достаточно первого операнда, этот операнд и является результатом, в противном случае вычисляется второй операнд логической операции. 

Это основывается на свойствах алгебры логики: например, если один аргумент операции «ИЛИ» (or) является истиной, то и результат этой операции всегда является истиной. В случае, если второй операнд является сложным выражением, это позволяет сократить издержки на его вычисление:
```python


a < b and "меньше" or "больше или равно"
print(a < b and b < 10 or b >= 1)
```
За ввод в программу данных с клавиатуры в Python отвечает функция input(). Когда вызывается эта функция, программа останавливает свое выполнение и ждет, когда пользователь введет текст. После этого, когда он нажмет Enter, функция input() заберет введенный текст и передаст его программе, которая уже будет обрабатывать его согласно своим алгоритмам.

Функция input() передает введенные данные в программу. Их можно присвоить переменной:

a = input()

В данном случае строка сохраняется в переменной a и при желании мы можем вывести ее значение на экран:
```python


print("a: ", a)
b = input()
print(1 <= a < 10 and 1 <= b < 20)
```
При запуске программы, компьютер ждет, когда будет введена сначала одна строка, потом вторая. Они будут присвоены переменным a и b. 
```python


a = input()
b = input()

#После этого значения этих переменных выводятся на экран с помощью вывода.
print("a: ", a)
print("b: ", b)
```
Для функции input() предусмотрен специальный параметр-приглашение. Это приглашение выводится на экран при вызове input():
```python

a = input("Enter a: ")
print("a: ", a)
# Даже если ввести число, функция input() все равно вернет его строковое представление. Если надо получить число нужно использовать функции преобразования типов.
# Чтобы преобразовать строку из цифр в целое число, воспользуемся функцией int(). Например, int('23') вернет число 23.
a = int(input())
b = int(input())
s = a + b
print(s)
a = int(input("Enter a: "))
print("a: ", a)
b = int(input("Enter b: "))
print("b: ", b)
print(1 <= a < 10 and 1 <= b < 20)
print(a < b and b < 10 or b >= 1)
print("a / b = ", a / b)
```
Набор операторов достаточно традиционен.

Условный оператор if (если). 

Альтернативный блок после else (иначе). Если условий и альтернатив несколько, можно использовать elif (сокр. от else if).

Операторы цикла while (пока) и for (для). Внутри цикла возможно применение break и continue для прерывания цикла и перехода сразу к следующей итерации, соответственно.

Оператор определения класса class.

Оператор определения функции, метода или генератора def. Внутри возможно применение return (возврат) для возврата из функции или метода, а в случае генератора — yield (давать).

Оператор обработки исключений try — except — else или try — finally (начиная с версии 2.5, можно использовать finally, except и else в одном блоке).

Оператор pass ничего не делает. Используется для пустых блоков кода.
Используйте 4 пробела на каждый уровень отступа.

При использовании висячего отступа следует применять следующие соображения: на первой линии не должно быть аргументов, а остальные строки должны четко восприниматься как продолжение линии.
```python


Правильно:
# Выровнено по открывающему разделителю
if o == '+':
    print("a + b = ", a + b)
```
Пробелы - самый предпочтительный метод отступов. Табуляция должна использоваться только для поддержки кода, написанного с отступами с помощью табуляции. Python 3 запрещает смешивание табуляции и пробелов в отступах.

Утверждение с использованием оператора if содержит в себе логическое условие, в котором производится сравнение данных и по результату выбирается дальнейшее действие.
```python

if условие:
   действие(s)

# Если логическое условие является истиной (true), тогда блок действия в выражении будет выполнен. Если условие считается ложью (false) – тогда будет выполнен следующий блок кода после этого выражения.
a = int(input("Enter a: "))
print("a: ", a)
b = int(input("Enter b: "))
print("b: ", b)
if b != 0:
    print("a / b = ", a / b)
# Оператор else может использоваться вместе с оператором if. else содержит блок кода, который будет выполнен если результат выражения равен нулю или считается ложью. Это опциональный оператор, и он может быть только один во всем выражении после if.
a = int(input("Enter a: "))
print("a: ", a)
b = int(input("Enter b: "))
print("b: ", b)
if b != 0:
    print("a / b = ", a / b)
else:
    print("Oops, division by zero")
# Оператор elif позволяет выполнять множественную проверку выражения и выполнять блок кода, как только результат будет считаться истиной. Как и оператор else, elif опционален, однако в отличии от else он может использоваться многократно.
if условие:
   действие(я)
elif условие2:
   действие(я)
else:
   действие(я)
# В Python нет таких операторов как switch или case, но можно использовать операторы if..elif... вместо них.
o = input("Enter o: ")
if o == '+':
    print("a + b = ", a + b)
elif o == '-':
    print("a - b = ", a - b)
elif o == '*':
    print("a * b = ", a * b)
elif o == '/':
    if b != 0:
        print("a / b = ", a / b)
    else:
        print("Oops, division by zero")
else:
    print("Oops, not operation yet")
# Оператор while позволяет многократно выполнять блок команд до тех пор, пока выполняется некоторое условие. Это один из так называемых операторов цикла. Он также может иметь необязательный пункт else. Блок else выполняется тогда, когда условие цикла while становится ложным (False) – это может случиться даже при самой первой проверке условия. Если у цикла while имеется дополнительный блок else, он всегда выполняется, если только цикл не будет прерван оператором break.
running = True
while running:
    # Convert strings into integers
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    # Store the user input an operator
    o = input('Enter Operator: ')
    if o == 'q':
        print('Programm done.')
        running = False # это останавливает цикл while
    if o == "+":
        print("a + b = ", a + b)
    elif o == '-':
        print("a - b = ", a - b)
    elif o == '*':
        print("a * b = ", a * b)
        elif o == '/':
        if b != 0:
            print("a / b = ", a / b)
        else:
            print("Oops, division by zero")
    # If none of the above conditions were true then execute this by default
    else:
        print("Use either + - * / or % next time")
```