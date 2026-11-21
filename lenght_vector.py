
import math

# ฟังก์ชันคำนวณความยาวเวกเตอร์ 2 มิติ
def lenv2(v):
    sumofPower2 = v[0]**2 + v[1]**2
    return math.sqrt(sumofPower2)


# ฟังก์ชันคำนวณความยาวเวกเตอร์ 3 มิติ
def lenv3(v):
    sumofPower2 = v[0]**2 + v[1]**2 + v[2]**2
    return math.sqrt(sumofPower2)


# กำหนดเวกเตอร์
a = (1, 2, 3)
b = (3, 0, 0)
c = (3, 4)

# คำนวณความยาว
lena = lenv3(a)
lenb = lenv3(b)
lenc = lenv2(c)

# แสดงผลลัพธ์
print("=== Vector Length ===")
print(f"Length of vector a = {a} is {lena:.2f}")
print(f"Length of vector b = {b} is {lenb:.2f}")
print(f"Length of vector c = {c} is {lenc:.2f}")
