# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

NumDay = int(input('Enter a number of a weekday '))
if NumDay in range(1,6):
    print ('Oh no... It is not a weekend...')
elif NumDay in range(6,8):
    print ('It is a weekend! Huzzah!')
elif NumDay >7 or NumDay <1:
    print ('Hmmm... There is no such day of the week.')