power = 'ON'

# my game works when my code does not equal the phrase to cancel it.
while power != 'No more Magic':

    # asking user what the weather is like
    weather = input('Whats the weather like? I can give you advice. :)')

    #my control flow
    if weather == 'sunny':
        print('take your shorts!')
    elif weather == 'rainy':
        print('Take your umbrella')
    elif 'rainy' and 'stormy' in weather:
        print('stay home')
    else:
        print("sorry, i didn't quite catch that")

    #inside my while loop, asking if i want to enter my code to cancel this
    power = input("if you want to end the program, enter 'No more Magic',\n if not press enter!")


