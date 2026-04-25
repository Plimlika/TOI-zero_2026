import sys

def solve():
    # รับข้อมูลทั้งหมดเข้ามาแล้วแยกด้วยช่องว่าง
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    W = int(input_data[0])
    H = int(input_data[1])
    M = int(input_data[2])
    N = int(input_data[3])

    # 2. ดึงพิกัดการตัดแกน X (มีดแนวตั้ง)
    X_cuts = []
    for i in range(M):
        X_cuts.append(int(input_data[4 + i]))
        
    # 3. ดึงพิกัดการตัดแกน Y (มีดแนวนอน)
    Y_cuts = []
    for i in range(N):
        Y_cuts.append(int(input_data[4 + M + i]))

    # 4. คำนวณความกว้างของขนมปังแต่ละช่วง
    # เพิ่ม 0 และ W เข้าไปที่หัวและท้ายเพื่อคำนวณชิ้นริมสุด
    X_coords = [0] + X_cuts + [W]
    widths = []
    for i in range(1, len(X_coords)):
        widths.append(X_coords[i] - X_coords[i-1])

    # 5. คำนวณความสูงของขนมปังแต่ละช่วง
    # เพิ่ม 0 และ H เข้าไปที่หัวและท้าย
    Y_coords = [0] + Y_cuts + [H]
    heights = []
    for i in range(1, len(Y_coords)):
        heights.append(Y_coords[i] - Y_coords[i-1])

    # 6. เรียงลำดับความกว้างและความสูงมากไปน้อย
    widths.sort(reverse=True)
    heights.sort(reverse=True)

    # ดึงค่าที่มากที่สุด 2 อันดับแรกออกมา
    w1, w2 = widths[0], widths[1]
    h1, h2 = heights[0], heights[1]

    max_area1 = w1 * h1
    max_area2 = max(w1 * h2, w2 * h1)

    print(f"{max_area1} {max_area2}")

if __name__ == '__main__':
    solve()