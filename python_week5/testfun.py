# ไม่หาร 3 ลงตัว
def nothree(a, b):
    return [i for i in range(a, b + 1) if i % 3 != 0]

# ค่าบวกลบ
def PoNe(positive, negative, number):
    if number > 0:
        positive += number
    elif number < 0:
        negative += number
    return positive, negative