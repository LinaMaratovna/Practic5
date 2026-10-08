import random


def input_size():
    """Запрашивает у пользователя размер массива (положительное целое число)."""
    while True:
        try:
            n = int(input("Введите размер массива: "))
            if n > 0:
                return n
            print("Ошибка: размер должен быть положительным числом.")
        except ValueError:
            print("Ошибка: введите целое число.")


def fill_array(size):
    """Заполняет массив элементами, введенными пользователем или случайными."""
    choice = input("Заполнить массив вручную? (да/нет): ").strip().lower()
    arr = []
    if choice in ("да", "д", "yes", "y"):
        for i in range(size):
            while True:
                try:
                    arr.append(int(input(f"Элемент [{i}]: ")))
                    break
                except ValueError:
                    print("Ошибка: введите целое число.")
    else:
        arr = [random.randint(1, 100) for _ in range(size)]
    return arr


def indices_divisible_by_10(arr):
    """Формирует массив индексов элементов исходного массива, которые делятся на 10."""
    return [i for i in range(len(arr)) if i % 10 == 0]


def save_to_file(data, filename, title):
    """Сохраняет массив в текстовый файл."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(title + "\n")
        f.write(" ".join(map(str, data)) + "\n")
    print(f"Массив сохранен в файл: {filename}")


def print_array(data, title):
    """Выводит массив на экран."""
    print(f"\n{title}")
    print(" ".join(map(str, data)) if data else "(пусто)")

def main():
    print("=== Практическая работа №5. MASkарад. Вариант 3 ===\n")

    # 1. Формирование начального массива
    size = input_size()
    initial_array = fill_array(size)

    # Вывод и сохранение начального массива
    print_array(initial_array, "Первоначальный массив:")
    save_to_file(initial_array, "initial_array.txt", "Первоначальный массив:")

    # 2. Формирование массива индексов, делящихся на 10
    indices_array = indices_divisible_by_10(initial_array)

    # Вывод и сохранение промежуточного массива индексов
    print_array(indices_array, "Массив с индексами, кратными 10:")
    save_to_file(indices_array, "indices_array.txt", "Массив с индексами, кратными 10:")

    # 3. Очистка первоначального массива
    initial_array.clear()

    # Сохранение финального (очищенного) массива
    save_to_file(initial_array, "cleared_array.txt", "Первоначальный массив после очистки:")
    print_array(initial_array, "Первоначальный массив после очистки:")
if __name__ == "__main__":
    main()