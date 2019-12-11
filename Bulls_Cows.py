import random
def generate_list():
    lst = [i for i in range(10)]
    lst = random.sample(lst, 4)
    return lst

def count_cows():
    pass

def count_bulls():
    pass

def user_parse():
        while True:
            try:
                user_try = list(input("Insert four number: "))
                if len(user_try) != 4:
                    raise Exception
                if len(user_try) == 4:
                    for i in user_try:
                        int(i)
                    return user_try
                else:
                    return user_try
            except:
                print('You have to insert four number, for instance 1234 ')
                continue

def comparison(target_list, user_try):
    target = target_list
    for_target = list(target)
    # print('Toto je target',target)
    user = user_try
    for_user = list(user)
    bulls = 0
    cows = 0
    for index in range(4):
        # print(index)
        # print(type(target_list[index]), type(user_try[index]))
        if target[index] == int(user[index]):
            bulls += 1
            # print(index, target_list[index])
            for_target.remove(target[index])

    for i in for_target:
        # print(for_target)
        if str(i) in user:
            # print(user)
            cows += 1
            for_user.remove(str(i))
    return bulls, cows


def main():

    target_list = generate_list()
    print(target_list)
    user_try = user_parse()
    print(comparison(target_list, user_try))

main()