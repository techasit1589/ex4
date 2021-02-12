# while
print("while")
a = 2
b = 1
while a < 13:
    print("  [", a, "]")
    while b < 13:
        print(a, "*", b, ":", a * b)
        b += 1
    print("------------")
    a += 1
    b -= 11


# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
print("for")
c = 2
for number in range(2, 13):
    print("  [", c, "]")
    for i in range(1, 13):
        result = number * i
        print(number, "*", i, ":", result)
    print("-------------")
    c += 1
