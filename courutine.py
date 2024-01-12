def coroutine():
    a = yield 47
    b = yield 50
    yield a + b

if __name__ == '__main__':
    coro = coroutine()
    first = next(coro)
    coro.send(4)
    result = coro.send(first)
    print(result) 