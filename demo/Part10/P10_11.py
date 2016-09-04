import json


def input_fav(filename):
    msg = 'please input your favorite number! : '
    try:
        favNumber = input(msg)
        favNumber = int(favNumber)
    except ValueError:
        print('input value error! please input a number: ')
        input_fav(filename)
    else:
        with open(filename, 'w') as fileobj:
            json.dump(favNumber, fileobj)


def get_fav(filename):
    errormsg = filename + ' not found in path >>' + 'please input your favorite number! : '
    try:
        with open(filename) as fileobj:
            favNumber = json.load(fileobj)
            if type(favNumber) == int:
                msg = 'I know your fav number is : ' + str(favNumber)
                print(msg)
            else:
                input_fav(filename)
                get_fav(filename)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(errormsg)
        input_fav(filename)
        get_fav(filename)


filename = 'favorite.txt'
# input_fav(filename)
get_fav(filename)
