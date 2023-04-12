print("Введите номер билета: ")
n = int(input())
summ1 = 0
summ2 = 0
num123 = n//1000
num456 = n%1000
while num123>0:
    x = num123 % 10
    summ1= summ1 + x
    num123 = num123//10
print(f"Сумма первых трех чисел: {summ1}")

while num456>0:
    x = num456 % 10
    summ2= summ2 + x
    num456 = num456//10
print(f"Сумма последних трех чисел: {summ2}")

if summ1==summ2:
    print('yes')
else:
    print('no')
        