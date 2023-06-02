import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль!"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Ошибка: невозможно извлечь корень из отрицательного числа!"

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Извлечение корня")

choice = input("Введите номер операции (1/2/3/4/5/6): ")

num1 = float(input("Введите первое число: "))

if choice != '6':
    num2 = float(input("Введите второе число: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print(num1, "^", num2, "=", power(num1, num2))
elif choice == '6':
    print("√", num1, "=", square_root(num1))
else:
    print("Некорректный ввод операции")
