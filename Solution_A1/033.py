n = int(input())

minimum = int(input())

for i in range(n - 1):
    num = int(input())
    if num < minimum:
        minimum = num

print(minimum)