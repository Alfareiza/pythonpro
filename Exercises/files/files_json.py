import json

numbers = list(range(1, 11))

filename = 'numbers.json'


def create_file():
    with open(f'files_of_exercises/{filename}', 'w') as fp:
        json.dump(numbers, fp)


def read_file():
    with open(f'files_of_exercises/{filename}') as fp:
        numbers = json.load(fp)
    print(numbers)


def interacting():
    username = input("What is your name?: ")
    filename = 'username.json'

    with open(f'files_of_exercises/{filename}', 'w') as fp:
        json.dump(username, fp)
        print('User created!')


def hello_from_file():
    filename = 'username.json'
    with open(f'files_of_exercises/{filename}') as fp:
        username = json.load(fp)
        print(f'Welcome Back {username.capitalize()} !')


if __name__ == '__main__':
    # create_file()
    # read_file()
    # interacting()
    hello_from_file()
