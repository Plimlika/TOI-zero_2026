month = int(input())
day = int(input())

if (month < 3) or (month == 3 and day < 21):
    print("winter")
elif (month < 6) or (month == 6 and day < 21):
    print("spring")
elif (month < 9) or (month == 9 and day < 21):
    print("summer")
elif (month < 12) or (month == 12 and day < 21):
    print("fall")
else:
    print("winter")