from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __init__(self, collection, cursor=0):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class JustIter:
    def __init__(self, collection, cursor=0):
        self.collection = collection
        self.cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.cursor += 1
            return self.collection[self.cursor - 1]
        except:
            raise StopIteration


class EvenIter:
    def __init__(self, collection, cursor=0):
        self.collection = collection
        self.cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.cursor += 1
            if (self.collection[self.cursor - 1]) % 2 == 0:
                return self.collection[self.cursor - 1]
            else:
                return 'Нечетное'
        except:
            raise StopIteration


class Collection(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def iterator(self):
        pass


class JustCollection(Collection):
    def __init__(self, collection):
        self.collection = collection

    def iterator(self, cursor=0):
        return JustIter(self.collection, cursor)


class EvenCollection(Collection):
    def __init__(self, collection):
        self.collection = collection

    def iterator(self, cursor=0):
        return EvenIter(self.collection, cursor)


def client_code(collection, cursor=0):
    for x in collection.iterator(cursor):
        print(x)


if __name__ == "__main__":
    client_code(JustCollection([1, 2, 3, 4, 5]), 1)
    client_code(EvenCollection([1, 2, 3, 4, 5]))
