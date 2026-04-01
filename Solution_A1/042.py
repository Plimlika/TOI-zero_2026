commands = input()
x, y = 0, 0

for move in commands:
    if move == 'N':
        y += 1
    elif move == 'S':
        y -= 1
    elif move == 'E':
        x += 1
    elif move == 'W':
        x -= 1

distance = abs(x) + abs(y)
print(x, y, distance)