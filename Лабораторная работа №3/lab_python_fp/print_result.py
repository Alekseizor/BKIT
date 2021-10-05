def print_result(func):
    def dek(*a):
        print(func.__name__)
        if type(func(*a)) == list:
            for x in func(*a):
                print (x)
        elif type(func(*a)) == dict:
            for x in func(*a).keys():
                print(x, '=', func(*a)[x])
        else:
            print(func(*a))

    return dek


@print_result
def test_1():
    return '1'


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
