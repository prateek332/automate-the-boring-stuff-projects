"""Comma Code."""

spam = ['apples', 'bananas', 'tofu', 'cats']

def list_joiner(list):
    count = 0
    joined = ''
    while count < len(list) - 1:
        joined += list[count] + ' ,'
        count += 1
    joined += 'and '
    joined += list[-1]

    return joined



print(list_joiner(spam))


"""Character Picture Grid"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
