import multiprocessing as mp

class Worker(mp.Process):
    def __init__(self, func, func_args, queue):
        super().__init__()
        self.func = func
        self.func_args = func_args
        self.queue = queue

    def run(self):
        result = self.func(self.func_args)
        self.queue.put(result)
        
def hello_world(func_args):
    return func_args

if __name__ == "__main__":
    mp.set_start_method('fork')
    queue = mp.Queue()
    worker = Worker(hello_world, ['text', 'new'], queue)
    worker.start()