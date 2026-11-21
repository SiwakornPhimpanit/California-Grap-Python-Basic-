
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# โหลดข้อมูล California Housing
california = fetch_california_housing()

# กำหนดข้อมูลแกน X และ Y
x = california.data[:, 0]  # Median Income
y = california.target      # Median House Value

# สร้างกราฟ
plt.figure(figsize=(12, 7))

# กราฟจุดหลากสี
scatter = plt.scatter(
    x,
    y,
    c=y,
    cmap="rainbow",
    s=15,
    alpha=0.7
)

# ตั้งชื่อกราฟ
plt.title("California Housing - Colorful Graph", fontsize=16)
plt.xlabel("Median Income", fontsize=12)
plt.ylabel("Median House Value", fontsize=12)

# เพิ่มแถบแสดงระดับสี
plt.colorbar(scatter, label="House Value")

# เพิ่มเส้นตาราง
plt.grid(True, linestyle="--", alpha=0.4)

# จัดตำแหน่งกราฟ
plt.tight_layout()

# แสดงกราฟ
plt.show()
