distance = int(input())

if distance <= 1:
    fare = 35
elif distance <= 10:
    fare = 35 + (distance - 1) * 5
else:
    fare = 35 + (9 * 5) + (distance - 10) * 8

print(int(fare))