import time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self, before='time: ', after=''):
        self.before = before
        self.after = after
        self.time = time.time()

    def __enter__(self):
        print(self.before, end='')
        return (self.time)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type, exc_val, exc_tb)
        else:
            print(self.after)



with cm_timer_1() as cm_1:
    time.sleep(5.5)
    print('{0:2.1f}'.format(time.time() - cm_1))


@contextmanager
def cm_timer_2(before='time: ', after=''):
    print(before,end='')
    yield time.time()
    print(after)


with cm_timer_2() as cm_2:
    time.sleep(5.5)
    print('{0:2.1f}'.format(time.time() - cm_2))
