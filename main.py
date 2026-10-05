try:
    n = int(input("Введите размер массива (от 1 до 10000): "))
    while n < 1 or n > 10000:
        print("Ошибка! Размер массива должен быть от 1 до 10000.")
        n = int(input("Введите размер массива (от 1 до 10000) ну пж пж:"))
    a = []
    for i in range(n):
        while True:
            try:
                x = int(input("Введите элемент {i}: "))
                a.append(x)
                break  # выходим из while, если ввели число
            except ValueError:
                print("Ошибка! Введите целое число.")
    print("Вывод первоначального массива:")
    indexes = []
    for i in range(n):
        if a[i] % 10 == 0:
            indexes.append(i)
    # Очищает первоначальный массив
    a.clear()
    # Вывод индексов
    print("Массив индексов:", indexes)
except ValueError:
    print("Ошибочка чутка: размер массива должен быть целым числом еyyy.")
