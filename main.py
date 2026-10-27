cells = [" " for i in range(9)]


def input_check(cells):
    print("Введите номер клетки, которую хотите отметить (1-9)")
    while True:
        try:
            num = int(input())
            if not 1 <= num <= 9:
                print("Клетки с таким номером не существует. Введите цифру от 1 до 9")
            else:
                if cells[num - 1] != " ":
                    print("Клетка занята. Попробуйте еще раз")
                else:
                    return num
        except ValueError:
            print("Некорректный номер клетки. Введите цифру от 1 до 9")


input_check(cells)