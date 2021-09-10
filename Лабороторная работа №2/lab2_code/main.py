from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from PIL import Image, ImageDraw


def painting(r, c, s):
    im = Image.new('RGB', (500, 300), (245, 245, 220))
    draw = ImageDraw.Draw(im)
    t = 10
    print("Выбери нужное(один из пунктов): 1. Круг   2. Квадрат   3. Прямоугольник")
    v = int(input())
    if v == 1:
        draw.ellipse((t * c.r, t * c.r, 3 * t * c.r, 3 * t * c.r), fill=(0, 255, 0), outline=(0, 0, 0))
        im.show()
    elif v == 2:
        draw.rectangle((-10, -10, 2 * t * s.side, 2 * t * s.side), fill=(255, 0, 0), outline=(255, 255, 255))
        im.show()
    elif v == 3:
        draw.rectangle((-10, -10, 2 * t * r.width, 2 * t * r.height), fill=(0, 0, 255), outline=(255, 255, 255))
        im.show()


def main():
    r = Rectangle("синего", 5, 10)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)
    print("Нарисуем фигуры?) Если да, то нажми 1, если нет - любую другую цифру")
    v = int(input())
    if v == 1:
        painting(r, c, s)


if __name__ == "__main__":
    main()
