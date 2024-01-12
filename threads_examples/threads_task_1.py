from concurrent.futures import ThreadPoolExecutor


def f1(item):
    return item * item


def f2(data):
    return sum(data)


def worker(data, pool_size=5):
    with ThreadPoolExecutor(max_workers=pool_size) as pool:
        squared_data = list(pool.map(f1, data))
        result = f2(squared_data)

    return result


data = range(1, 10)
result = worker(data)
print("Result = ", result)