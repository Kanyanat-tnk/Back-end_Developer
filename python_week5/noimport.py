
def nothree(a, b):
    return [i for i in range(a, b + 1) if i % 3 != 0]


numfirst = int(input('ป้อนค่าต้น'))
numsecond = int(input('ป้อนค่าปลาย'))

divide_three = nothree(numfirst,numsecond)

print(f"ผลลัพธ์ของช่วงตัวเลข {numfirst} ถึง {numsecond} ที่ไม่หาร 3 ลงตัว: {divide_three}")

        
def PoNe(positive, negative, number):
    if number > 0:
        positive += number
    elif number < 0:
        negative += number
    return positive, negative
    
positive = 0
negative = 0

while True:
    number = int(input('Enter number (0 to stop): '))
    
    if number == 0:
        break 
    
    positive, negative = PoNe(positive, negative, number)

print('ผลลัพธ์ของค่าบวกทั้งหมด =', positive)
print('ผลลัพธ์ของค่าลบทั้งหมด =', negative)
