
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
    cells[current_cell - 1] = current
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


def win(cells):
    if cells[0] == cells[1] == cells[2] != ' ':
        return cells[0]
    if cells[3] == cells[4] == cells[5] != ' ':
        return cells[3]
    if cells[6] == cells[7] == cells[8] != ' ':
        return cells[6]
    if cells[0] == cells[4] == cells[8] != ' ':
        return cells[0]
    if cells[2] == cells[4] == cells[6] != ' ':
        return cells[2]
    if cells[0] == cells[3] == cells[6] != ' ':
        return cells[0]
    if cells[1] == cells[4] == cells[7] != ' ':
        return cells[1]
    if cells[2] == cells[5] == cells[8] != ' ':
        return cells[2]
    return None


def draw(cells):
    return all(cell != ' ' for cell in cells)


def main():
    cells = [" " for i in range(9)]
    print_board(cells)
    cur = 'X'
    winner = win(cells)
    is_draw = draw(cells)
    while not winner and not is_draw:
        cur = rules(cells, cur)
        winner = win(cells)
        is_draw = draw(cells)
    if winner:
        print(f"Победил {winner}")
    else:
        print("Ничья")


if __name__ == '__main__':
    restart = 'да'
    while restart.lower() == 'да':
        main()
        restart = input('Сыграть еще раз? (да/нет)\n')


