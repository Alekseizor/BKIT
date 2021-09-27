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
            if self.app == True and type(x) != int:
                x = x.lower()
            if x not in self.word:
                self.word.add(x)
                return x


def gen_random(num_count, begin, end):
    for i in range(num_count):
        s = random.randint(begin, end)
        yield s


def main():
    data = gen_random(2, 1, 15)
    # data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    for i in Unique(data, ignore_case=False):
        print(i)


if __name__ == "__main__":
    main()
