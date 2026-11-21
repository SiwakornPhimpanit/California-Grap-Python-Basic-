
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# โหลดข้อมูล California Housing
california = fetch_california_housing()

# เลือกข้อมูลรายได้เฉลี่ยและราคาบ้าน
x = california.data[:, 0]
y = california.target

# สร้างกราฟสีน้ำเงิน
plt.figure(figsize=(10, 6))

plt.scatter(
    x, y,
    color="blue",
    alpha=0.5,
    s=10,
    label="California Housing"
)

# ตั้งชื่อกราฟ
plt.title("California Housing Graph", fontsize=16)
plt.xlabel("Median Income")
plt.ylabel("Median House Value")

# แสดงตารางและคำอธิบาย
plt.grid(True)
plt.legend()

# แสดงกราฟ
plt.show()
