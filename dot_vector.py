
# dot_vector.py
# โปรแกรมคำนวณ Dot Product ของเวกเตอร์

def dot_vector(a, b):
    result = 0

    for i in range(len(a)):
        result += a[i] * b[i]

    return result


# กำหนดเวกเตอร์
a = (1, 2, 3)
b = (3, 0, 0)

# เรียกใช้ฟังก์ชัน
dot = dot_vector(a, b)

# แสดงผลลัพธ์
print("Vector A =", a)
print("Vector B =", b)
print("Dot Product =", dot)
