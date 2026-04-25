import sys
def main():
    # อ่านข้อมูลทั้งหมดจาก standard input และแยกด้วยช่องว่างเป็น list ของข้อความ
    input_data = sys.stdin.read().split()
    
    # ตรวจสอบว่ามีข้อมูลถูกส่งเข้ามาหรือไม่
    if not input_data:
        return
    
    unique_list = []  # เก็บตัวเลขที่ต้องการแสดงผลตามลำดับก่อนหลัง
    seen = set()      # ใช้ set เพื่อตรวจสอบความซ้ำซ้อนอย่างรวดเร็ว (O(1))
    
    for num in input_data:
        # ถ้าตัวเลขนี้ยังไม่เคยปรากฏมาก่อน
        if num not in seen:
            unique_list.append(num)  # เพิ่มลงใน list สำหรับแสดงผล
            seen.add(num)            # บันทึกไว้ใน set ว่าพบแล้ว
            
    # นำตัวเลขใน list มาเชื่อมกันด้วยเว้นวรรคแล้วแสดงผลเป็นบรรทัดเดียว
    print(" ".join(unique_list))

if __name__ == "__main__":
    main()