def solve():
    text = input().strip().upper()
    n = len(text)
    
    # 1. ตรวจสอบกรณี unknown (มีแค่ I หรือ T ทั้งข้อความ)
    all_it = True
    for char in text:
        if char not in "IT":
            all_it = False
            break
    if all_it:
        print(f"unknown {n}")
        return

    # 2. ตรวจสอบกฎ Pure Blood
    max_a = 0
    pure_blood = True
    first_error_index = -1

    for i in range(n):
        char = text[i]
        
        # กฎของ R: ต้องตามด้วย A
        if char == 'R':
            if i + 1 >= n or text[i+1] != 'A':
                pure_blood = False
                first_error_index = i + 1 if i + 1 < n else i
                break
        
        # กฎของ A: ต้องอยู่หลัง R หรือ A ด้วยกันเท่านั้น
        elif char == 'A':
            if i == 0 or text[i-1] not in "RA":
                pure_blood = False
                first_error_index = i
                break
            # ถ้างั้นก็นับจำนวน A ที่ติดกันไปเลยเพื่อหา max_a
            if i == 0 or text[i-1] != 'A': # เริ่มต้นกลุ่ม A ใหม่
                current_a = 0
                temp_idx = i
                while temp_idx < n and text[temp_idx] == 'A':
                    current_a += 1
                    temp_idx += 1
                if current_a > max_a:
                    max_a = current_a

        # กฎของ B: ต้องตามด้วย I หรือ T
        elif char == 'B':
            if i + 1 >= n or text[i+1] not in "IT":
                pure_blood = False
                first_error_index = i + 1 if i + 1 < n else i
                break
        
        # กฎตัวอักษรแปลกปลอม
        elif char not in "IT":
            pure_blood = False
            first_error_index = i
            break

    # 3. แสดงผลลัพธ์
    if pure_blood:
        print(f"yes {max_a}")
    else:
        # ถ้าจุดผิดเกินความยาว ให้บอกตำแหน่งสุดท้าย
        if first_error_index >= n: first_error_index = n
        print(f"no {first_error_index}")

solve()