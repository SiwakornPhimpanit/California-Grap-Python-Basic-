
import matplotlib.pyplot as plt

# ข้อมูลแกน X และ Y
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 3, 6, 5, 8, 7, 9, 8, 10]

# สร้างกราฟเส้นสีแดง
plt.plot(x, y, color="red", marker="o",
         linestyle="-", linewidth=2)

# ตั้งชื่อกราฟและแกน
plt.title("Red Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# แสดงเส้นตาราง
plt.grid(True)

# แสดงกราฟ
plt.show()
