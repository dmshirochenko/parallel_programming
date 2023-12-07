from multiprocessing import Process
import os

def custom_func(i):
    pid = os.getpid()
    print(f'Function call for process: {i}, PID: {pid}')
    for j in range(0, i):
        print(f'Function output: {j}, PID: {pid}')

if __name__ == '__main__':
    for i in range(6):
        process = Process(target=custom_func, args=(i,))
        process.start()
        process.join()
