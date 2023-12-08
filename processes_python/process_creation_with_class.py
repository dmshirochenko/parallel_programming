from multiprocessing import Process, Queue

class Worker(Process):
    def __init__(self, func, func_args, queue):
        super().__init__()
        self.func = func
        self.func_args = func_args
        self.queue = queue

    def run(self):
        result = self.func(*self.func_args)
        self.queue.put(result)

def sample_function(x, y):
    return x + y

if __name__ == '__main__':
    queue = Queue()
    
    worker = Worker(sample_function, (2, 3), queue)
    worker.start()
    worker.join()

    result = queue.get()
    print(f"Result: {result}")
