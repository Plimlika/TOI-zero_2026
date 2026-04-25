text = input().upper()
length = len(text)

# กรณีที่ 1: มีคำว่า BUU
if "BUU" in text:
    max_u = 0
    # วนลูปหาตัว B ทุกตำแหน่ง
    for i in range(length):
        if text[i] == "B":
            current_u = 0
            # พอเจอ B แล้ว ให้เช็กตัวถัดๆ ไปว่าเป็น U หรือไม่
            for j in range(i + 1, length):
                if text[j] == "U":
                    current_u += 1
                else:
                    break
            if current_u > max_u: # เก็บค่าตัว U ที่มากที่สุดที่เคยเจอ
                max_u = current_u
    
    print(f"Yes {max_u}")

# กรณีที่ 2: ไม่มี BUU แต่มี B
elif "B" in text:

    first_b_index = text.find("B") # หาตำแหน่ง (Index) ของ B ตัวแรก
    part1 = text[:first_b_index + 1] # ส่วนแรก: ตั้งแต่ต้นจนถึงตัว B ตัวแรก
    remaining_length = length - (first_b_index + 1) # ส่วนที่สอง: หลัง B ตัวแรกไปจนจบ ให้เปลี่ยนเป็น U ทั้งหมด
    part2 = "U" * remaining_length
    
    print(part1 + part2)

# กรณีที่ 3: ไม่มีตัว B เลย
else:
    pattern = "BUU"
    result = ""
    # วนลูปเติมตัวอักษรจากคำว่า BUU จนครบความยาวเดิม
    for i in range(length):
        # ใช้ % 3 เพื่อให้ตำแหน่งวนกลับมาที่ 0, 1, 2 (B, U, U)
        result += pattern[i % 3]
    
    print(result)