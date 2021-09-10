import math
import sys
import numpy


def print_result(roots):
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} , {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} , {} , {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


def get_coef(index, prompt):
    '''
 Читаем коэффициент из командной строки или вводим с клавиатуры
 Args:
 index (int): Номер параметра в командной строке
 prompt (str): Приглашение для ввода коэффицента
 Returns:
 float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef = float(sys.argv[index])
    except ValueError:
        print("Пожалуйста, введите число")
        return get_coef(index, prompt)
    except:
        # Вводим с клавиатуры
        try:
            print(prompt)
            coef = float(input())
        except ValueError:
            print("Пожалуйста, введите число")
            return get_coef(index, prompt)

    # Переводим строку в действительное число
    return coef


def get_roots(a, b, c):
    '''
 Вычисление корней квадратного уравнения
 Args:
 a (float): коэффициент А
 b (float): коэффициент B
 c (float): коэффициент C
 Returns:
 list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def get_biroots(a, b, c):
    result = get_roots(a, b, c)
    resultfinal = []
    for x in result:
        if x > 0:
            resultfinal.append(numpy.sqrt(x))
            resultfinal.append(-numpy.sqrt(x))
        elif x == 0:
            resultfinal.append(0)
    return resultfinal


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    if a!=0:
       b = get_coef(2, 'Введите коэффициент B:')
       c = get_coef(3, 'Введите коэффициент C:')
       # Вычисление корней
       print('Какое уравнение будем решать? 1. Биквадратное. 2. Квадратное')
       choice = int(input())
       if choice == 1:
        roots = get_biroots(a, b, c)
       elif choice == 2:
          roots = get_roots(a, b, c)
       else:
          print('Выберите один из возможных вариантов')
       # Вывод корней
       print_result(roots)
    else:
        print('Ввод данного коэффициента невозможен')
        main()

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
