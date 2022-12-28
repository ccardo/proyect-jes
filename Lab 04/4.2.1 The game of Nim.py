##
# NIM DEF in personal projects
from random import randint
from colorama import init
from colorama import Fore
init()

marbles = randint(10, 100)
print(Fore.LIGHTYELLOW_EX + '> Welcome to the game of NIM! You\'ll have a set number of starting marbles\n'
      '  from which YOU and your OPPONENT will subtract marbles in turn!\n'
      '> The max. number of marbles you can take in 1 turn is HALF the total.\n'
      '> The player who takes the last marble loses! HAVE FUN!')

print(Fore.CYAN + f'\nThere are {marbles} starting marbles!')
firstMove = randint(0, 1)
smart = randint(0, 1)
moves = 0
firstMove_flag = firstMove

# from here, the code bisects to define the smart and dumb mode
if smart == 0:
    print(Fore.LIGHTWHITE_EX + '\ngame started in ' + Fore.GREEN + 'DUMB' + Fore.LIGHTWHITE_EX + ' mode!')
    while marbles > 0:

        # if firstMove equals 0, the computer will play first.
        # this block of code will activate ONCE and be useless after the computer
        # has made the first move
        if firstMove_flag == 0:
            print('\nThe opponent has the first move!')
            computerMove = randint(1, marbles // 2)
            marbles = marbles - computerMove
            print('\nThe opponent has taken ' + Fore.CYAN + f'{computerMove} marbles!' + Fore.RESET)
            print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
            moves = moves + 1

        # sets the first move flag to 1 to prevent the previous part of the code
        # from keeping on repeating after every cycle;
        # while also keeping the original firstMove the same (we will need it later for the win/loss)
        firstMove_flag = 1

        # player's turn
        # first we want to check if the move is valid (up to marbles/2)
        # if it's not valid, the computer will keep asking for a valid move to be made
        playerMove = int(input('\nHow many marbles will you take? '))
        playerMove_flag = playerMove

        if playerMove_flag > marbles // 2 or playerMove_flag == 0:
            while playerMove > marbles // 2 or playerMove == 0:
                print(Fore.LIGHTRED_EX + 'You cannot take 0 or more than HALF the marbles. Try again.' + Fore.RESET)
                playerMove = int(input('How many marbles will you take? '))
                if playerMove <= marbles // 2 and playerMove != 0:
                    playerMove_flag = playerMove
                    break
        if playerMove_flag <= marbles // 2 and playerMove_flag != 0:
            marbles = marbles - playerMove
            print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
            moves = moves + 1

        # computer's turn;
        # the computer takes a random number for which the move is valid
        if marbles > 1:
            computerMove = randint(1, marbles // 2)
            marbles = marbles - computerMove
            print('\nThe opponent has taken ' + Fore.CYAN + f'{computerMove} marbles!' + Fore.RESET)
            print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
            moves = moves + 1

        # takes into account the number of total turns and the starting turn
        # if the n. of turns is even, the player who started
        # also has the last marble and thus loses
        if marbles == 1:
            print('\n')
            if (firstMove == 0 and moves % 2 == 0) or (firstMove == 1 and moves % 2 != 0):
                print(Fore.GREEN + f'You have WON after {moves} moves! Congratulations!')
            elif (firstMove == 1 and moves % 2 == 0) or (firstMove == 0 and moves != 0):
                print(Fore.RED + f'You managed to LOSE after {moves} moves against a DUMB opponent! You\'re so bad!')
            break


elif smart == 1:
    print(Fore.LIGHTWHITE_EX + '\ngame started in ' + Fore.RED + 'SMART' + Fore.LIGHTWHITE_EX + ' mode!')
    power2 = 6

    while marbles > 0:
        if firstMove_flag == 0:
            # if firstMove equals 0, the computer will play first.
            # this block of code will activate ONCE and be useless after the computer
            # has made the first move
            print('\nThe opponent has the first move!')

            noOptimalStartingMove = [3, 7, 15, 31, 63]
            for i in noOptimalStartingMove:
                if marbles == i:
                    computerMove = 1
                    marbles = marbles - computerMove
                    print('\nThe opponent has taken ' + Fore.CYAN + f'{computerMove} marbles!' + Fore.RESET)
                    print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
                    moves = moves + 1

            computerMoveSmart = 0
            while marbles <= (2**power2 - 1):
                power2 = power2 - 1
            while marbles > ((2**power2) - 1):
                marbles = marbles - 1
                computerMoveSmart = computerMoveSmart + 1
                if marbles == ((2**power2) - 1):
                    power2 = power2 - 1
                    moves = moves + 1
                    print('\nThe opponent has taken ' + Fore.CYAN + f'{computerMoveSmart} marbles!' + Fore.RESET)
                    print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
                    break

        # sets the first move flag to 1 to prevent the previous part of the code
        # from keeping on repeating after every cycle;
        # while also keeping the original firstMove the same (we will need it later for the win/loss)
        firstMove_flag = 1

        # player's turn
        # first we want to check if the move is valid (up to marbles/2)
        # if it's not valid, the computer will keep asking for a valid move to be made
        playerMove = int(input('\nHow many marbles will you take? '))
        playerMove_flag = playerMove

        if playerMove_flag > marbles // 2 or playerMove_flag == 0:
            while playerMove > marbles // 2 or playerMove == 0:
                print(Fore.LIGHTRED_EX + 'You cannot take 0 or more than HALF the marbles. Try again.' + Fore.RESET)
                playerMove = int(input('How many marbles will you take? '))
                if playerMove <= marbles // 2 and playerMove_flag != 0:
                    playerMove_flag = playerMove
                    break
        if playerMove_flag <= marbles // 2 and playerMove_flag != 0:
            marbles = marbles - playerMove
            print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
            moves = moves + 1

        # computer's turn;
        if marbles > 1:
            while marbles < (2**power2 - 1):
                power2 = power2 - 1

            # if there's no optimal move to be made, the computer takes only 1 marble
            noOptimalMove = [3, 7, 15, 31, 63]
            for i in noOptimalMove:
                if marbles == i:
                    computerMoveSmart = 1
                    marbles = marbles - computerMoveSmart
                    print('\nThe opponent has taken ' + Fore.CYAN + f'{computerMoveSmart} marbles!' + Fore.RESET)
                    print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
                    moves = moves + 1
            # decreases the number of marbles until it is equal to 2^x - 1
            computerMoveSmart = 0
            while marbles > ((2**power2) - 1):
                marbles = marbles - 1
                computerMoveSmart = computerMoveSmart + 1
                # if the marbles are equal to 2^x - 1,
                # the power is diminished by 1 to account for the next cycle
                if marbles == ((2**power2) - 1):
                    power2 = power2 - 1
                    moves = moves + 1
                    print('\nThe opponent has taken ' + Fore.CYAN + f'{computerMoveSmart} marbles!' + Fore.RESET)
                    print(Fore.CYAN + f'Marbles left: {marbles}' + Fore.LIGHTWHITE_EX)
                    break

        # takes into account the number of total turns and the starting turn
        # if the n. of turns is even, the player who started
        # also has the last marble and thus loses
        if marbles == 1:
            print('\n')
            if (firstMove == 0 and moves % 2 == 0) or (firstMove == 1 and moves % 2 != 0):
                print(Fore.GREEN + f'You have WON after {moves} moves against the perfect opponent.'
                                   f' This shouldn\'t be possible wtf.')
            elif (firstMove == 1 and moves % 2 == 0) or (firstMove == 0 and moves % 2 != 0):
                print(Fore.RED + f'You have LOST after {moves} moves! Try another time!')
            break
exit('Game Over')
