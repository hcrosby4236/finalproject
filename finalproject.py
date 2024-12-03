import random
print('----------------------------------------------------------------------------------------------------')
print('Hello! Welcome to Helenas final project!')
print('----------------------------------------------------------------------------------------------------')
print('What type of game would you like to play?')
game = input('Scary Forest, Cat Simulator or Rock, Paper, Scissors? (1, 2 or 3) ')
print('----------------------------------------------------------------------------------------------------')
print('Okay! Game Starting!')
print('----------------------------------------------------------------------------------------------------')
if game == "1":
    print('Its 8 Am. You wake up suddenly in an unknown enviroment, and all of sudden feel much smaller. You have been turned into a cat for 24 hours.')
    print('----------')
    total = 24
    choices = ['Sleep (-4 hours)', 'Eat and clean (-1 hour)', 'Explore (-5 hours)', 'Litter box and zoomies (-2 Hours)', 'Knock stuff over (-2 hours)']
    while total > 0:
        print(f'You have {total} hours left in the day.')
        for i in choices:
            print(i)
        print('----------')
        choice = input('What do you do? ')
        print('----------')
        if choice == 'Sleep':
            total = total - 4
            print('You Went back to sleep.')
            print('----------')
        if choice == 'Eat and clean':
            total = total - 1
            print('You went to get some food and then cleaned yourself up.')
            print('----------')
        if choice == 'Explore':
            total = total - 5
            toys = ['Cat Tree', 'Fish','Cat Tunnel']
            print('You chose to go and explore the enviroment your in. When your there you see some toys.')
            for i in toys:
                print(i)
            what_toy = input('Which one do you pick? ')
            if what_toy == "Cat Tree":
                print('You played on the cat tree.')
                print('----------')
            elif what_toy == 'Fish':
                print("You Played with the fish.")
                print('----------')
            elif what_toy == 'Cat Tunnel':
                print('You played with the cat tunnel')
                print('----------')
        if choice == 'Litter box and zoomies':
            total = total - 2
            print('You used the litter box and then got the zoomies.')
            print('----------')
        if choice == 'Knock stuff over':
            print('You decide to walk around and start knocking stuff over.')
            print('----------')
    while total <= 0:
        print('The day is over! Thank you for playing!')
        break
if game == "3":
    while True:
        user = input("Thanks for playing rock, paper, scissors. Pick either Rock, Paper or Scissors ")
        print('-------------------')
        possible_choices = ['Rock', 'Paper', 'Scissors']
        computer = random.choice(possible_choices)

        if user == computer:
            print("Tie!")
            print('-------------------')
        elif user == 'Rock':
            if computer == "Paper":
                print('Computer chose paper. Paper covers Rock. You lose.')
                print('-------------------')
            else: 
                print('Computer chose Scissors. Rock beats Scissors. You Win!')
                print('-------------------')
        elif user == "Paper":
            if computer ==  "Scissors":
                print('Computer chose Scissors. Scissors cut paper. You lose.')
                print('-------------------')
            else:
                print('Computer chose Rock. Paper covers Rock. You win.')
                print('-------------------')
        elif user == 'Scissors':
            if computer == "Rock":
                print('Computer chose Rock. Rock beats Scissors. You lose.')
                print('-------------------')
            else:
                print('Computer chose Paper. Scissors cuts Paper. You win.')
                print('-------------------')
        playagain = input('Want to play again? (Y/N) ')
        if playagain == 'Y':
            True
        if playagain == "N" :
            break    
