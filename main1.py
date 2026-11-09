import time, os

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[42m'
BROWN = '\u001b[48;5;130m'
END = '\u001b[0m'

def flag():
    line = ' ' * 4
    lenght = 16
    height = lenght

    for i in range(height):
        if i < height // 2:
            print(f'{WHITE}{line * lenght}{END}') 
        else:
            print(f'{RED}{line * lenght}{END}')

def draw(count=1):
    height = 5
    lenght = 11
    for line in range(height):
        if line % 2 == 0:
            print(f'\x1b[48;5;16m{lenght * '    '}\x1b[0m' * count)
        elif line == 1:
            print(f'\x1b[48;5;67m{lenght // 2 * '    '}\x1b[48;5;16m{'    '}\x1b[48;5;67m{lenght // 2 * '    '}\x1b[0m' * count)
        else:
            print(f'\x1b[48;5;67m{lenght // 5 * '    '}\x1b[48;5;16m{'    '}\x1b[48;5;67m{lenght // 2 * '    '}\x1b[48;5;16m{'    '}\x1b[48;5;67m{lenght // 5 * '    '}\x1b[0m' * count)

def func():
    for y in range(20, 0, -1):
        print(y/2, end=' ')
        for x in range(1, 21):
            print('!!' if round(x ** 0.5 * 2)/2 == (y/2) else '--', end = ' ')
        print()

    print(' ', end='')
    for i in range(10):
        print(i, end='  ')
    for i in range(10, 21):
        print(i, end=' ')

def chart():
    list = []
    for line in open('filelab.txt', 'r'):
        list.append(float(line))
    sum1 = sum(abs(x) for x in list[:125])
    sum2 = sum(abs(x) for x in list[125:])
    frc1 = round(sum1 / (sum1 + sum2), 2)
    frc2 = 1 - frc1
    print(f'  1-125:{RED}{' ' * int(frc1 * 100)}{END}')
    print(f'126-250:{BLUE}{' ' * int(frc2 * 100)}{END}')

def animation():
    p = '  '
    s = [0, 1, 2, 3]
    for i in s:
        print(f'{p * 2}{GREEN}{p * 4}{END}')
        print(f'{p}{GREEN}{p * 6}{END}')
        for _ in range(i):
            print(f'{p * 3}{BROWN}{p * 2}{END}')
        for _ in range(2):
            print(f'{p}{RED}{p * 2}{BROWN}{p * 2}{END}')
        for _ in range(3 - i):
            print(f'{p * 3}{BROWN}{p * 2}{END}')
        time.sleep(1)
        os.system('cls')

# flag()
# draw(3)
# animation()
# chart()
# func()