import random

dic = {'1':' ', '2':' ', '3':' ',
       '4':' ', '5':' ', '6':' ',
       '7':' ', '8':' ', '9':' '
       }

def print_template():
    print('''===========================
Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
Let's start the game''')
    print('------')
    print(' | | ')
    print('------')
    print(' | | ')
    print('------')
    print(' | | ')
    print('------')
    print('='*27)

def first_player():
       lst = [0, 1]
       random.shuffle(lst)
       return lst


def choose_sign(player1, player2):
    while True:
        if player1 == 1:
            player = 'Player1'
            choices = ['x', 'o']
            sypher = input('Random choose {} as first player. {} please insert your sign: x or o \n'.format(player, player))
            if sypher != choices[0] and sypher != choices[1]:
                print('You have to insert x or o')
                continue
            else:
                if sypher == 'x':
                    return ['x', 'o']
                else:
                    return ['o', 'x']

        elif player2 == 1:
            player = 'Player2'
            choices = ['x', 'o']
            sypher = input('Random choose {} as first player. {} please insert your sign: x or o \n'.format(player, player))
            if sypher != choices[0] and sypher != choices[1]:
                print('You have to insert x or o ')
                continue
            else:
                if sypher == 'x':
                    return ['o', 'x']
                else:
                    return ['x', 'o']


def print_progress(dic):
    print('------')
    print('{}|{}|{}'.format(dic['1'], dic['2'], dic['3']))
    print('------')
    print('{}|{}|{}'.format(dic['4'], dic['5'], dic['6']))
    print('------')
    print('{}|{}|{}'.format(dic['7'], dic['8'], dic['9']))
    print('------')


def win(dic, sypher):

    if dic['1'] == dic['2'] == dic['3'] == sypher:
        return True
    if dic['4'] == dic['5'] == dic['6'] == sypher:
        return True
    if dic['7'] == dic['8'] == dic['9'] == sypher:
        return True

    if dic['1'] == dic['4'] == dic['7'] == sypher:
        return True
    if dic['2'] == dic['5'] == dic['8'] == sypher:
        return True
    if dic['3'] == dic['6'] == dic['9'] == sypher:
        return True

    if dic['1'] == dic['5'] == dic['9'] == sypher:
        return True
    if dic['3'] == dic['5'] == dic['7'] == sypher:
        return True

    return False

def exit_requests(player1, player2):
    for i in dic:
        dic[i] = ' '
    if player1 == 1:
        print('Player2 `s turn')
        return (0, 1)
    elif player2 == 1:
        print('Player1 `s turn')
        return (1, 0)

def main():
    while True:
        next_game = True
        while next_game:
            next_game = False
            print_template()
            player1, player2 = first_player()
            mark_player1, mark_player2 = choose_sign(player1, player2)
            score = {'Player1': 0, 'Player2': 0}
            count = 0
            while count < 3:
                count += 1
                while True:
                    if player1 == 1:
                        try:
                            inpt = input('Player1 please insert position: ')
                            if dic[inpt] == ' ':
                                dic[inpt] = mark_player1
                                print_progress(dic)
                                if win(dic, mark_player1):
                                    print('Player1 is winner')
                                    score['Player1'] += 1
                                    break
                            else:
                                print('Possition is occupied ')
                                continue
                        except :
                            print('You have to insert integer 1-9 !')
                            continue
                        player1, player2 = 0, 1

                    elif player2 == 1:
                        try:
                            inpt = input('Player2 please insert position: ')
                            if dic[inpt] == ' ':
                                dic[inpt] = mark_player2
                                print_progress(dic)
                                if win(dic, mark_player2):
                                    print('Player2 is winner')
                                    score['Player2'] += 1
                                    break
                            else:
                                print('Possition is occupied ')
                                continue
                        except :
                            print('You have to insert integer 1-9 !')
                            continue
                        player1, player2 = 1, 0
                print('Score is: Player1:{}   Player2:{} \n'.format(score['Player1'], score['Player2']))

                if count < 3:
                    exit_request = input('Do you want to play next round ? y=yes, anything for no  ')
                    player1, player2 = exit_requests(player1, player2)
                    if exit_request == 'y':
                        continue
                    else:
                        break

        try:
            game_input = input('Do you want to play next game ? y=yes, anything for no  ')
            if game_input == 'y':
                for i in dic:
                    dic[i] = ' '
                next_game = True
            else:
                return None

        except ValueError:
            print('You have to choose \'y\' or \'n\'')

main()