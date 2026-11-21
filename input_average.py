
# input_average.py
# โปรแกรมรับคะแนนและคำนวณค่าเฉลี่ย

def average(a, b, c):
    return (a + b + c) / 3

# รับข้อมูลจากผู้ใช้
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

# คำนวณผลรวมและค่าเฉลี่ย
total = score1 + score2 + score3
avg = average(score1, score2, score3)

# แสดงผลลัพธ์
print("-------------------------")
print(f"Total = {total:.2f}")
print(f"Average = {avg:.2f}")
print("-------------------------")
