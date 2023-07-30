import time


def exec_time(func):
    def wrapper(*args):
        start = time.time()
        execution_func = func(*args)
        end = time.time()
        difference = end - start
        return difference
    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
       count += 1


print(loop())