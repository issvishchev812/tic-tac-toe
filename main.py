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


def rules(cells, current):
    print(f"Ходит {current}")
    current_cell = input_check(cells)
    cells[current_cell-1] = current
    if current == 'X':
        current = 'O'
    else:
        current = 'X'
    print_board(cells)
    return current


def print_board(cells):
    count = 0
    print('-------------------')
    for cell in cells:
        count += 1
        if count % 3 == 0:
            print(f'|  {cell}  |', end='\n')
            print('-------------------')
        else:
            print(f'|  {cell}  ', end='')

def main():
    cur = 'X'
    while True:  # Потом здесь будет на победителя/ничью
        cur = rules(cells, cur)


if __name__ == '__main__':
    print_board(cells)
    main()