print("ตรวจสอบเกรดที่ได้")
score = int(input('กรุณากรอกคะแนน'))
if score < 0 or score > 100 :
    print('ใส่ 0 - 100 เท่านั้น')
elif score >= 80 :
    print('เกรด 4')
elif score >= 70 :
    print('เกรด 3')
elif score >= 50 :
    print('เกรด 2')
elif score < 50 :
    print('เกรด 1')
else :
    print('ป้อนค่าไม่ถูกต้อง')


