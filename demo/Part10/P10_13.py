import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as fileobj:
        json.dump(username, fileobj)
    return username


def greeting():
    username = get_stored_username()
    if username:
        namecorrect = input("your name is " + username + "? : yes or no >>>")
        if namecorrect == 'yes':
            print("Welcome back, " + username + "!")
        elif namecorrect == 'no':
            username = get_new_username()
            print("We'll remember you! " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you! " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you! " + username + "!")


# greeting()

def test():
    filename = 'username1.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = '123'
        return username
    else:
        return username


print(test())
