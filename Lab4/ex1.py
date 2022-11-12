import sorts as s
import timeit as ti


mas = list(map(int, input("Введите массив: ").split()))
print(mas)
start_time = ti.default_timer()
while True:
    m = int(input("Выберите метод сортировки: 1 (Быстрая сортировка), 2 (Сортировка расческой): "))
    if m == 1:
        print(s.quick_sort(mas))
        print("Время работы программы: ", ti.default_timer() - start_time)
        break
    elif m == 2:
        print(s.r_sort(mas))
        print("Время работы программы: ", ti.default_timer() - start_time)
        break
    else:
        print("Вы ввели неверное значение. Выберите заново метод сортировки (1 или 2).")
