def analyza_numbers(numbers):
    average = sum(numbers) / len(numbers)  
    summation = sum(numbers)  
    maximum = max(numbers)  #
    minimum = min(numbers)  

    return average, summation, maximum, minimum

result = analyza_numbers([10, 20, 30, 40])
print(f"ผลลัพธ์ที่คาดหวัง: {result}")