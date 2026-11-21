
# string_format.py
# Python String Formatting

name = "Siwakorn"
lastname = "Phimpanit"
age = 26
score = 85.756
department = "Computer Engineering"

# 1. การแสดงข้อความทั่วไป
print("===== String Formatting =====")

# 2. ใช้ f-string
print(f"Name: {name}")
print(f"Lastname: {lastname}")
print(f"Age: {age}")
print(f"Department: {department}")

# 3. แสดงทศนิยม 2 ตำแหน่ง
print(f"Score: {score:.2f}")

# 4. ใช้ format()
print("Full Name: {} {}".format(name, lastname))

# 5. ใช้ % Formatting
print("Age: %d years" % age)

# 6. การคำนวณใน f-string
a = 10
b = 20

print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")

print("===== End Program =====")
