
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