import json
import sys
import time
from contextlib import contextmanager
import random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = iter(items)
        self.word = set()
        if not kwargs:
            self.app = False
        else:
            self.app = kwargs['ignore_case']

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            x = next(self.data)
            if self.app == True:
                x['job-name'] = x['job-name'].lower()
            if x['job-name'] not in self.word:
                self.word.add(x['job-name'])
                return x['job-name']


def print_result(func):
    def dek(*a):
        print(func.__name__)
        if type(func(*a)) == list:
            for x in func(*a):
                print(x)
            return func(*a)
        elif type(func(*a)) == dict:
            for x in func(*a).keys():
                print(x + func(*a)[x])
        else:
            print(func(*a))

    return dek


def gen_random(num_count, begin, end):
    for i in range(num_count):
        s = random.randint(begin, end)
        raise s


@contextmanager
def cm_timer_2(before='', after=''):
    print(before, end='')
    yield time.time()
    print(after)


# Сделаем другие необходимые импорты

path = 'data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding="utf-8") as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return list(Unique(arg, ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    a = (', зарплата ' + str(random.randint(100000, 200000)) + ' руб.' for x in arg)
    return dict(zip(arg, a))


if __name__ == '__main__':
    with cm_timer_2() as t:
        f4(f3(f2(f1(data))))

        print('time:', time.time() - t)
