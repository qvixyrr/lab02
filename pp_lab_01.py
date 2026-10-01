import math

print("=== Задание 1.1: Калькулятор площади треугольника ===")
def calculate_triangle_area():
    try:
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"Площадь треугольника: {area:.2f}\n")
        else:
            print("Ошибка: треугольник с такими сторонами не существует!\n")
    except ValueError:
        print("Ошибка: введены некорректные данные.\n")

print("=== Задание 1.2: Конвертер единиц измерения расстояния ===")
def convert_distance():
    units = {'км': 1000.0, 'м': 1.0, 'см': 0.01, 'мм': 0.001, 'mi': 1609.344, 'yd': 0.9144}
    src = input("Исходная единица (км, м, см, мм, mi, yd): ").strip().lower()
    dst = input("Целевая единица (км, м, см, мм, mi, yd): ").strip().lower()
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

print("=== Задание 1.3: Определение високосного года ===")
def check_leap_year():
    try:
        year = int(input("Введите год: "))
        if year > 0:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"Год {year} — ВИСОКОСНЫЙ.\n")
            else:
                print(f"Год {year} — НЕВИСОКОСНЫЙ.\n")
        else:
            print("Ошибка: год должен быть положительным числом!\n")
    except ValueError:
        print("Ошибка: введено некорректное значение.\n")

if __name__ == "__main__":
    calculate_triangle_area()
    convert_distance()
    check_leap_year()
