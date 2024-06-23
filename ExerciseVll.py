odd_numbers = []
even_numbers = []

for number in range(1, 21):
    # ตรวจสอบว่าเลขนั้นเป็นคู่หรือคี่
    if number % 2 == 0:
        even_numbers.append(number)  
    else:
        odd_numbers.append(number)  

print("จำนวนคี่:", odd_numbers)
print("จำนวนคู่:", even_numbers)

# 04 จิราวรรณ กมลทิพย์สุคนธ์
