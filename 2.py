print("Введите трехзначное число: ")
n = int(input())
summ = 0
while n>0:
    x = n % 10
    summ= summ + x
    n = n//10
print(summ)

