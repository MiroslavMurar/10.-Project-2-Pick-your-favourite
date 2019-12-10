import random

player1 = None
player2 = None

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
    global player1
    global player2

    lst = [0,1]
    player1 = random.choice(lst)

    if player1 == 1:
        player2 = 0
        print('First player is Player1')
    else:
        player2 = 1
        print('First player is Player2')


def choose_sign():
    while True:
        sypher = input('Player insert x or o: ')
        if sypher != 'o' and sypher != 'x':
            print('You have to insert x or o')
            continue
        else:
            return sypher


def print_progress(dic):
    print('------')
    print('{}|{}|{}'.format(dic['1'], dic['2'], dic['3']))
    print('------')
    print('{}|{}|{}'.format(dic['4'], dic['5'], dic['6']))
    print('------')
    print('{}|{}|{}'.format(dic['7'], dic['8'], dic['9']))
    print('------')


def win(dic, sypher):

    if dic['1'] and dic['2'] and dic['3'] == sypher:
        return 'Winner !!!'
    if dic['4'] and dic['5'] and dic['6'] == sypher:
        return 'Winner !!!'
    if dic['7'] and dic['8'] and dic['9'] == sypher:
        return 'Winner !!!'

    if dic['1'] and dic['4'] and dic['7'] == sypher:
        return 'Winner !!!'
    if dic['2'] and dic['5'] and dic['8'] == sypher:
        return 'Winner !!!'
    if dic['3'] and dic['6'] and dic['9'] == sypher:
        return 'Winner !!!'

    if dic['1'] and dic['5'] and dic['9'] == sypher:
        return 'Winner !!!'
    if dic['3'] and dic['5'] and dic['7'] == sypher:
        return 'Winner !!!'

    return False

def flow(dic, sypher1):
    while True:
        try:
            inpt = input('Insert position: ')
            dic[inpt] = sypher1
            print_progress(dic)
            continue

        except ValueError as err:
            print('You have to insert integer !', err)
            continue




def main():
    print_template()
    first_player()

    flow(dic, choose_sign())

main()