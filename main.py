print("Выполнить сложение")
try:
    first_value = float(input("Введите первое число: "))
    second_value = float(input("Введите второе число: "))
    print("Результат сложения: ", first_value + second_value)
except ValueError:
    print("Некорректное значение")

print("\nВыполнить вычитание")
try:
    first_value = float(input("Введите первое число: "))
    second_value = float(input("Введите второе число: "))
    print("Результат вычитания: ", first_value - second_value)
except ValueError:
    print("Некорректное значение")

print("\nВыполнить уможение")
try:
    first_value = float(input("Введите первое число: "))
    second_value = float(input("Введите второе число: "))
    print("Результат умноженя: ", first_value * second_value)
except ValueError:
    print("Некорректное значение")

print("\nВыполнить деление")
try:
    first_value = float(input("Введите первое число: "))
    second_value = float(input("Введите второе число: "))
    print("Результат деления: ", first_value / second_value)
except ValueError:
    print("Некорректное значение")
except ZeroDivisionError:
    print("Деление на ноль запрещено")

print("Конец работы программы")
