from random import *
play = True
funtions = ['+','-','*']

while play:
 
 ammount = int(input('кількість спроб: '))

 for i in range(ammount):
     wins = 0
     number1 = randrange(1,100)
     number2 = randrange(1,100)
     b = choice(funtions)
     c = str(number1)+b+str(number2)
     print(c)
     answer = input('Відповідь: ')

     if int(answer) == eval(c):
         print("правильно!")
         wins += 1
     elif int(answer) != eval(c):
         print("невірно") 

 if wins == ammount:
     print('ви повний переможець!')
 else:
     pass
 
 question = input('Зіграємо ще раз? (1 is yes, 2 is no) ')
 if question == '1':
     pass
 elif question == '2':
     print('ну гаразд :(')
     play = False
 

