import logging
import threading
import time


def thread_func(*args):
    thread_name = threading.current_thread().name
    print(f"Thread {thread_name} started")

    time.sleep(1)
    print(f"Thread {thread_name} finished")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for idx in range(4):
        logging.info(f"Thread {idx} created")

        th = threading.Thread(target=thread_func, args=(idx,), name="th-{}".format(idx))
        threads.append(th)
        th.start()

    for idx, thread in enumerate(threads):
        logging.info(f"Join call for thread {idx}")
        thread.join()
        logging.info(f"Thread finished {idx}")
