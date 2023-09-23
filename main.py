from math import pi,sin,cos,tan
import math
while True:
    print("1. Сложить два числа")
    print("2. Вычесть два числа")
    print("3. Умножение двух чисел")
    print("4. Деление двух чисел")
    print("5. Возвести в степень")
    print("6. Факториал числа")
    print("7. Квадратный корень числа")
    print("8. Синус числа")
    print("9. Тангенс числа")
    print("10. Косинус числа")
    print("0. Выход")
    choice = input("Выберите операцию")
    if choice == "1":
        num1 = float(input("Введите первое число"))
        num2 = float(input("Введите второе число"))
        total = num1 + num2
        print("Результат:" + str(total))
    elif choice == "2":
        num1 = float(input("Введите первое число"))
        num2 = float(input("Введите второе число"))
        total = num1 - num2
        print("Результат:" + str(total))
    elif choice == "3":
        num1 = float(input("Введите первое число"))
        num2 = float(input("Введите второе число"))
        total = num1 * num2
        print("Результат:" + str(total))
    elif choice == "4":
        num1 = float(input("Введите первое число"))
        num2 = float(input("Введите второе число"))
        total = num1 / num2
        if num1 or num2 == 0:
            print("Нельзя делить на 0")
        print("Результат:" + str(total))
    elif choice == "5":
        num1 = float(input("Введите первое число"))
        num2 = float(input("Введите степень в которую нужно возвести"))
        total = num1 ** num2
        print("Результат" + str(total))
    elif choice == "6":
        num1 = float(input("Введите число"))
        total = num1
        for i in range(1,num1):
            total = total * i
            print("Результат" + str(total))
    elif choice == "7":
        num1 = float(input("Введите число"))
        total = num1 ** 0,5
        print("Результат" + str(total))
    elif choice == "8":
        num1 = float(input("Введите число"))
        total = sin(pi/num1)
        print("Результат" + str(total))
    elif choice == "9":
        num1 = float(input("Введите число"))
        total = tan(pi/num1)
        print("Результат" + str(total))
    elif choice == "10":
        num1 = float(input("Введите число"))
        total = cos(pi/num1)
        print("Результат" + str(total))
    elif choice == "0":
        break


