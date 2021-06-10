import random

randomNumber = random.randint(1,9)
print(randomNumber)
chances = 0
inputNumber = int(input('Guess A Number : '))

while chances < 5:

    if inputNumber == randomNumber :
        print('You were Correct !')

    elif inputNumber > randomNumber :
        print('The Number you guessed was to high')    

    elif inputNumber < randomNumber :
        print('The Number you guessed was to Low')        

        break

    chances = chances + 1
    
    if not chances <  5:
        print('You lose ! It was ' , randomNumber)

    