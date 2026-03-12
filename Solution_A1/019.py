a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("all the same")
elif a != b and a != c and b != c:
    print("all different")
else:
    print("neither")