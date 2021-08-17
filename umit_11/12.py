import abc

## Реализация классического итератора

## Абстрактные классы:

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

## реализация итератора для списка:

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

class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)


# Теперь мы можем создать объект коллекции и обойти все ее элементы с помощью итератора:

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

# А так как мы реализовали метод first, который сбрасывает итератор в начальное состояние, то можно воспользоваться этим же итератором еще раз:

# возвращаем итератор в исходное состояние
itr.first()

while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())
