import random
print('โปรแกรมเป่ายิงฉุบ')
while True : 
    a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(a)
    b = str(input('ระบุคำตอบของคุณ : '))
    if b == a :
        print('เสมอ')
    elif a =="กรรไกร" and b =="ค้อน":
        print("You win!")
    elif a =="กระดาษ" and b =="กรรไกร":
        print("You win!")
    elif a =="ค้อน" and b =="กระดาษ":
        print("You win!")
    elif a =="ค้อน" and b =="กรรไกร":
        print("You lose!")
    elif a =="กรรไกร" and b =="กระดาษ":
        print("You lose!")
    elif a =="กระดาษ" and b =="ค้อน":
        print("You lose!")
    else :
        print('\"กรุณาระบุเฉพาะ ค้อน , กรรไกร , กระดาษ เท่านั้น!!!\"')
        