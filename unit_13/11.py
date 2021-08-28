## Можно написать аналог функции islice, используя генератор.
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
