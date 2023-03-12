#  Задача 2. Напишите программу которая на вход принимает число 
#  и на выходе показывает сумму его цифр.
def SumDigit(a):
    sum = 0
    while a != 0:
       sum = sum + a % 10
       a = a // 10


    return sum

def InputDigits():
    
    while True:
        a = input('Введите число :')
        if a.isdigit() == False:
            print('Вы ввели не число')
        else: 
           break
    return int(a)



numbers = InputDigits()
sum = SumDigit(numbers)
print(f'Сумма цифр числа {numbers} = {sum}')