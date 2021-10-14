# 3. เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4]
#    ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข

NumberList = []
MaxNumber = 0
MaxNumberIndex = 0
count = 0
TotalIndex = int(input("How many index in NumberList?\n"))

while count < TotalIndex:
    number = int(input("Enter a number: "))
    NumberList.append(number)

    if number > MaxNumber:
        MaxNumber = number
        MaxNumberIndex = count

    count += 1

print("")
print(NumberList)
print("Max Number is in Index = " + str(MaxNumberIndex))
