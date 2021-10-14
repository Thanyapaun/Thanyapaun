# 4. เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial
#    เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

FactorialList = []
FactorialNumber = int(input("Enter a factorial number: "))

while FactorialNumber >= 1:
    FactorialList.append(FactorialNumber)
    FactorialNumber -= 1

total = 1
for N in FactorialList:
    total *= N

print(str(FactorialList[0]) + "! = " + str(total))

stringTotal = str(total)
print("")
FactorialSummary = []
for letter in stringTotal:
    FactorialSummary.append(int(letter))

ZeroCount = 0
index = int(len(FactorialSummary) - 1)

while FactorialSummary[index] == 0:
    ZeroCount += 1
    index -= 1

print("มีเลขศูนย์ต่อท้าย " + str(ZeroCount) + " ตัว")
