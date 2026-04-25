# 1. รับค่ากว้าง, ยาว, จำนวนชั้น
# ใช้ split() หั่นข้อความ และ เปลี่ยนเป็นตัวเลขพร้อมกัน
width, length, layers = map(int, input().split())

# 2. รับค่าบรรทัดที่สอง: ราคาต่อเมตร
price_per_meter = int(input())

# 3. คำนวณเส้นรอบรูป 1 รอบ 2 * (กว้าง + ยาว)
one_round = 2 * (width + length)

# 4. คำนวณความยาวลวดหนามทั้งหมด (เส้นรอบรูปคูณจำนวนชั้น)
total_length = one_round * layers

# 5. คำนวณราคาทั้งหมด
total_price = total_length * price_per_meter

print(total_length)
print(total_price)