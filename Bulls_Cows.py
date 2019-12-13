import random

def generate_list():
    lst = [i for i in range(10)]
    lst = random.sample(lst, 4)
    return lst

def user_parse():
        while True:
            try:
                user_try = list(input("Enter four number: "))
                if len(user_try) != 4:
                    raise Exception
                if len(user_try) == 4:
                    for i in user_try:
                        int(i)
                    return user_try
                else:
                    return user_try
            except:
                print('You have to enter four number, for instance 1234 ')
                continue

def comparison(target_list, user_try):
    for_target = list(target_list)
    bulls = 0
    cows = 0
    for index in range(4):
        if target_list[index] == int(user_try[index]):
            bulls += 1
            for_target.remove(target_list[index])

    for i in for_target:
        if str(i) in user_try:
            cows += 1
    return bulls, cows

def score():
    with open('score.txt') as file:
        result = int(file.readline())
        for i in file:
            if int(i) < result:
                result = int(i)
        return result

def repeat():
    while True:
        repeat = input('Do you want to repeat game ? y/n \n')
        if repeat not in 'yn':
            print('You have to enter \'y\' or \'n')
            continue
        elif repeat == 'y':
            return True
        elif repeat == 'n':
            return False

def main():
    while True:
        counter = 1
        target_list = generate_list()
        # print(target_list)
        while True :
            user_try = user_parse()
            print(comparison(target_list, user_try))
            bulls, cows = comparison(target_list, user_try)
            if bulls == 4:
                break
            counter += 1

        print('Correct, you\'ve guessed the right number in {} guesses! \n'
              'Best score without considered your game is {}' .format(counter, score()))

        with open('score.txt', 'a') as file:
            file.write(str(counter) + '\n')

        if not repeat():
            break
main()