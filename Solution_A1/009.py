score1 = int(input())
score2 = int(input())

sum = score1 + score2

if sum >= 50:
    print(sum)
    print("pass")
elif sum < 50:
    print(sum)
    print("fail")