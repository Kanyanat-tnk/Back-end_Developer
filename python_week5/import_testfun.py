import testfun  

# ให้ผู้ใช้เลือก
import testfun  

def findvalue(choice, numfirst, numsecond, positive, negative):
    if choice == '1':
        # หาร 3
        divide_three = testfun.nothree(numfirst, numsecond)  
        return divide_three
    
    elif choice == '2':
        # บวกลบ
        return positive, negative
    
    elif choice == '0':
        # ออกจากโปรแกรม
        print("Thank you for using")
        return None, None
    else:
        print("เลือกไม่ถูกต้อง กรุณาเลือกเฉพาะตัวเลือกที่มีให้เท่านั้น")
        return None, None


# รับค่าอินพุตนอกฟังก์ชัน findvalue
while True:
    choice = input('เลือกโปรแกรมต้องการ (1 = หาร 3 หรือ 2 = บวกลบ และ 0 = ออก): \n')
    
    if choice == '1':  # หาร 3
        numfirst = int(input('ป้อนค่าต้น: '))
        numsecond = int(input('ป้อนค่าปลาย: '))
        positive = 0
        negative = 0
        result = findvalue(choice, numfirst, numsecond, positive, negative)
        print(f"ผลลัพธ์ของช่วงตัวเลข {numfirst} ถึง {numsecond} ที่ไม่หาร 3 ลงตัว: {result}\n")
    
    elif choice == '2': # บวกลบ
        positive = 0
        negative = 0
        # รับค่าตัวเลขจากผู้ใช้ภายนอก findvalue()
        while True:
            number = int(input('Enter number (0 to stop): '))
            if number == 0:
                break
            # เรียกใช้ฟังก์ชัน PoNe จาก testfun.py
            positive, negative = testfun.PoNe(positive, negative, number)
        print('ผลลัพธ์ของค่าบวกทั้งหมด =', positive)
        print('ผลลัพธ์ของค่าลบทั้งหมด =', negative)
    
    elif choice == '0':
        findvalue(choice, 0, 0, 0, 0)
        break
    
    # ถามว่าจะทำงานโปรแกรมอื่นหรือไม่
    continue_choice = input("ต้องการทำงานโปรแกรมอื่นหรือไม่? (y/n): ")
    if continue_choice.lower() != 'y':
        print("Thank you for using!")
        break

