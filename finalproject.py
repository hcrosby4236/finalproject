import random
print('----------------------------------------------------------------------------------------------------')
print('Hello! Welcome to Helenas final project!')
print('----------------------------------------------------------------------------------------------------')
print('What type of game would you like to play?')
game = input('Scary Forest, Cat Simulator or Rock, Paper, Scissors? (1, 2 or 3) ')
print('----------------------------------------------------------------------------------------------------')
print('Okay! Game Starting!')
print('----------------------------------------------------------------------------------------------------')

if game == "2":
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
            print('----------')
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
            total = total - 2
            print('You decide to walk around and start knocking stuff over.')
            print('----------')
    while total <= 0:
        print('The day is over! Thank you for playing!')
        break
    input('Press any key to exit! ')


if game == "1":
    name = input('Before we begin, what is your name? ')
    print('Perfect. Lets begin.')
    print('----------------------------------------------------------------------------------------------------')
    answer = input('You start at a crossroad. You see two signs. The sign on your right has unicorns and rainbows on it. The sign on your left is black and has skulls on it. Do you go Right or Left? ')
    print('----------------------------------------------------------------------------------------------------')
    if answer =='Right':
        print("You go down the path that has the sign with unicorns and rainbows. You think to yourself, 'How bad could this really be?' You fall down into a bottomless hole and end up floating around for all eternity.")
        print("You lose.")
        print('----------------------------------------------------------------------------------------------------')
        input('Press any key to exit! ')
    elif answer == 'Left':
        print("You go down the path that has the sign with is black and has skulls. You feel uneasy. You can't see what's at the end of the path and it scares you. You see signs on the trees that say 'Turn back!' and 'Stay away!' and it makes you feel worse. ")
        print('----------------------------------------------------------------------------------------------------')
        answer = input("You come to an opening. There seems to be a table with chairs? Do you sit down? (Y/N) ")
        print('----------------------------------------------------------------------------------------------------')
        if answer == 'Y':
            answer = input("You sit down at the table. You feel like your not supposed to be here. A man approaches you, with a teacup in hand, he asks you for your name. Do you tell him? (Y/N) ")
            print('----------------------------------------------------------------------------------------------------')
            if answer == 'Y':
                print(f'"{name}! How splendid that you have come to join me today! We are about to have a tea party!" As hes pouring a cup of tea, you think he seems familar, but you cannot remember where from.')
                answer = input('He hands you a cup of tea. Do you drink it? (Y/N) ')
                print('----------------------------------------------------------------------------------------------------')
                if answer == 'Y':
                    print('You drink it and instantly pass out. You died. Dont take stuff from strangers.')
                    print('----------------------------------------------------------------------------------------------------')
                    input('Press any key to exit! ')
                elif answer == 'N':
                    answer = input('Thats good. You are smart." The strange looking man says. He asks how you got here and you told him you just woke up here. "Well, if you go down that path right there, the man dressed in orange can help you" He says, pointing to a path that looks oddly suspicious. Do you go? (Y/N) ')
                    print('----------------------------------------------------------------------------------------------------')
                    if answer == 'Y':
                        print('You go down the path. You see a man all dressed in orange. He says hello and approaches you. He puts his arm on your arm lovingly and stabs you. You die.')
                        print('----------------------------------------------------------------------------------------------------')
                        input('Press any key to exit! ')
                    elif answer == 'N':
                        print('"Fine If you dont want help, leave!" He pushes you away so you leave. You continue walking down the path until you see a clearing. You made it out! Congrats!')
                        print('----------------------------------------------------------------------------------------------------')
                        input('Press any key to exit! ')
            elif answer == 'N':
                answer = input('You simply blank stare at him and say nothing. "Hm. Not the talking type? That is aokay! Would you like some tea?" (Y/N) ')
                print('----------------------------------------------------------------------------------------------------')
                if answer == 'Y':
                    print('You drink it and instantly pass out. You died. Dont take stuff from strangers.')
                    print('----------------------------------------------------------------------------------------------------')
                    input('Press any key to exit! ')
                elif answer == 'N':
                    print('"Why dont you want anything to do with me? Why are you even here?" He pushes you out and back into the forest.')
                    print('You continue to walk through the forest, until a man in all purple comes up to you.')
                    answer = input('He says if you give him your soul, he can get you out of this forest. What do you say? (Y/N) ')
                    print('----------------------------------------------------------------------------------------------------')
                    if answer == 'Y':
                        print('All of a sudden your vision goes white and you appear in your house. Your cat comes up and starts meowing at you. You sigh in relief')
                        print('You made it out!')
                        print('----------------------------------------------------------------------------------------------------')
                        input('Press any key to exit! ')
                    elif answer == 'N': 
                        print('He kills you. Somehow. It was too quick for you to realize how. You were not supposed to say no.')
                        print('----------------------------------------------------------------------------------------------------')
                        input('Press any key to exit! ')
        elif answer == 'N':
            answer = input('You continue walking past the table and chairs. Walking through the forest, you see a man standing oddly at the end of the path. Do you call out to him? (Y/N) ')
            print('----------------------------------------------------------------------------------------------------')
            if answer == 'Y': 
                answer = input('You call out to him and he disappears quickly. Do you continue walking? (Y/N) ')
                print('----------------------------------------------------------------------------------------------------')
                if answer == 'Y': 
                    answer = input('You simply continue walking. Nothing happens until you come up to a large house. It seems empty. Do you go in? (Y/N) ')
                    if answer == 'Y': 
                        print('You go inside. It seems nice, and no one seems to be here. You go upstairs')
                        print('All of a sudden, you hear a noise from downstairs. You go to check it out and see that shady figure from earlier rummiging around the cabinet.')
                        print('"Aw, are you hungry"? You ask. The shadow nods. You find a pop tart and give it to the shadow. He bows and snaps his fingers and all of a sudden you are back in your house.')
                        print('----------------------------------------------------------------------------------------------------')
                        print('You won! He was just wanting a pop tart!')
                        print('------------------')
                        input('Press any key to exit! ')
                elif answer == 'N':
                    print('You freeze out of fear. That was a bad choice because the monster can smell fear and you die.')
                    print('----------------------------------------------------------------------------------------------------')
                    input('Press any key to exit! ')
            elif answer == 'N':
                print('You continue walking until you get up to him. He disapears the moment you approach him. You keep walking.')
                answer = input('You come to another crossroad, nothing on either side. Do you go Right or Left? ')
                print('----------------------------------------------------------------------------------------------------')
                if answer == 'Right':
                    print('You go down the path on the right. It starts to clear up above you and your beginning to see the sun. All of a sudden someone tackles you.')
                    print('They took your wallet. Whatever, you just wanna get out of here. You continue walking.')
                    print('You approach a brick wall. Dead end. You just give up.')
                    print('----------------------------------------------------------------------------------------------------')
                    print('You lose.')
                    input('Press any key to exit! ')
                elif answer == 'Left':
                    print('You go on the path to the left. You approach a very bright wall of light. Your scared but walk through it none the less.')
                    print('You walk through the wall, eyes closed and when you open your eyes, you are walking through your front door.')
                    print('You won!')
                    print('----------------------------------------------------------------------------------------------------')
                    input('Press any key to exit! ')
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
