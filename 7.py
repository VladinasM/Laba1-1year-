num=int(input('Введите трехзначное число: '))
firstNum=num//100
num=(num-firstNum*100)*10+firstNum
print(num)