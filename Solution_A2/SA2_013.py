# 1. รับข้อมูลไข่มุก: ชนิด (H, O, J) และ น้ำหนัก (กรัม)
pearl_type, pearl_weight = input().split()
pearl_weight = int(pearl_weight)

# 2. รับข้อมูลน้ำชา: ชนิด (R, T, M), ระดับความหวาน (1, 2, 3) และ ปริมาตร (cc.)
tea_type, sweetness, tea_volume = input().split()
sweetness = int(sweetness)
tea_volume = int(tea_volume)

# พลังงานไข่มุก
pearl_calories = 0
if pearl_type == "H":
    pearl_calories = 5 * pearl_weight
elif pearl_type == "O":
    pearl_calories = 3 * pearl_weight
elif pearl_type == "J":
    pearl_calories = 2 * pearl_weight

# พลังงานน้ำชา
tea_rate = 0

if tea_type == "R":
    if sweetness == 1: tea_rate = 12
    elif sweetness == 2: tea_rate = 18
    elif sweetness == 3: tea_rate = 25
elif tea_type == "T":
    if sweetness == 1: tea_rate = 15
    elif sweetness == 2: tea_rate = 20
    elif sweetness == 3: tea_rate = 30
elif tea_type == "M":
    if sweetness == 1: tea_rate = 10
    elif sweetness == 2: tea_rate = 15
    elif sweetness == 3: tea_rate = 20

tea_calories = tea_rate * tea_volume

total_calories = pearl_calories + tea_calories
print(total_calories)