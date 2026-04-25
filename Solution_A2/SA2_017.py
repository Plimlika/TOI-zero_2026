# 1. รับข้อมูลบรรทัดแรก: ขนาด และ ประเภท
size, menu_type = input().split()

# 2. รับข้อมูลบรรทัดที่สอง: Topping
topping_input = input().split()
topping_type = topping_input[0] # ตัวแรกคือชนิด Topping (P, E หรือ N)

# ส่วนที่ 1: คำนวณราคาราเมนจากตาราง
price = 0

if size == "S":
    if menu_type == "R": price = 60
    elif menu_type == "T": price = 80
elif size == "M":
    if menu_type == "R": price = 80
    elif menu_type == "T": price = 100
elif size == "L":
    if menu_type == "R": price = 100
    elif menu_type == "T": price = 120

# ส่วนที่ 2: คำนวณค่า Topping
topping_price = 0

if topping_type == "P":
    amount = int(topping_input[1]) # ถ้ามี Topping ต้องอ่านจำนวนตัวที่สองด้วย
    topping_price = amount * 15
elif topping_type == "E":
    amount = int(topping_input[1])
    topping_price = amount * 10
# ถ้าเป็น N: topping_price จะเป็น 0 ตามที่ตั้งต้นไว้

total_price = price + topping_price
print(total_price)