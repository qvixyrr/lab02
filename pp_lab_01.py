import math


def calculate_triangle_area():
    print("=== Задание 1.1: Калькулятор площади и определение вида треугольника ===")
    try:
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))

        if a + b > c and a + c > b and b + c > a:
            # Расчет площади по формуле Герона
            p = (a + b + c) / 2
            area = math.sqrt(p * (p - a) * (p - b) * (p - c))

            # Определение вида треугольника
            sides = sorted([a, b, c])
            a_sq, b_sq, c_sq = sides[0] ** 2, sides[1] ** 2, sides[2] ** 2

            if math.isclose(c_sq, a_sq + b_sq, rel_tol=1e-7):
                triangle_type = "Прямоугольный"
            elif c_sq < a_sq + b_sq:
                triangle_type = "Остроугольный"
            else:
                triangle_type = "Тупоугольный"

            print(f"Площадь треугольника: {area:.2f}")
            print(f"Вид треугольника: {triangle_type}\n")
        else:
            print("Ошибка: треугольник с такими сторонами не существует!\n")
    except ValueError:
        print("Ошибка: введены некорректные данные.\n")


def convert_distance():
    print("=== Задание 1.2: Конвертер единиц измерения расстояния ===")
    # Добавлены футы (ft) и дюймы (in)
    units = {
        'км': 1000.0,
        'м': 1.0,
        'см': 0.01,
        'мм': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    src = input("Исходная единица (км, м, см, мм, mi, yd, ft, in): ").strip().lower()
    dst = input("Целевая единица (км, м, см, мм, mi, yd, ft, in): ").strip().lower()

    if src in units and dst in units:
        try:
            val = float(input(f"Введите значение в [{src}]: "))
            if val >= 0:
                result = (val * units[src]) / units[dst]
                print(f"Результат: {val} {src} = {result:.4f} {dst}\n")
            else:
                print("Ошибка: расстояние не может быть отрицательным!\n")
        except ValueError:
            print("Ошибка: введено некорректное число!\n")
    else:
        print("Ошибка: неподдерживаемая единица измерения!\n")


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_closest_leap_year(year):
    if is_leap(year):
        return year
    offset = 1
    while True:
        if is_leap(year + offset):
            return year + offset
        if is_leap(year - offset):
            return year - offset
        offset += 1


def check_leap_year():
    print("=== Задание 1.3: Определение високосного года ===")
    try:
        year = int(input("Введите год: "))
        if year > 0:
            closest_year = get_closest_leap_year(year)
            if is_leap(year):
                print(f"Год {year} — ВИСОКОСНЫЙ.")
            else:
                print(f"Год {year} — НЕВИСОКОСНЫЙ.")
            print(f"Ближайший високосный год к {year}: {closest_year}\n")
        else:
            print("Ошибка: год должен быть положительным числом!\n")
    except ValueError:
        print("Ошибка: введено некорректное значение.\n")


if __name__ == "__main__":
    calculate_triangle_area()
    convert_distance()
    check_leap_year()
