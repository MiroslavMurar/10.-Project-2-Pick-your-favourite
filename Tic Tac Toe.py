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
    # print(player1)
    if player1 == 1:
        player2 = 0
    else:
        player2 = 1

def choose_sign(player1, player2):
    if player1 > player2:
        while True:
            inpt = input('Insert x or o: ')
            if inpt != 'o' and inpt != 'x':
                print('You have to insert x or o')
                continue
            else:
                return inpt


def print_progress(dic):
    print('------')
    print('{}|{}|{}'.format(dic['1'], dic['2'], dic['3']))
    print('------')
    print('{}|{}|{}'.format(dic['4'], dic['5'], dic['6']))
    print('------')
    print('{}|{}|{}'.format(dic['7'], dic['8'], dic['9']))
    print('------')


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
    # print_progress(dic)
    # flow(dic, 'o')
    first_player()
    # print(player1)
    choose_sign(player1, player2)
    print(player1)


main()