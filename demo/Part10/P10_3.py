promptMsg = 'please input your name (input \'quit\' to exit) : '
filename = 'guest_book.txt'
namelist = []
while True:
    guessname = input(promptMsg)
    if guessname != 'quit':
        namelist.append(guessname + '\n')
    else:
        with open(filename, 'w') as file_Obj:
            file_Obj.writelines(namelist)
        break

with open(filename) as fileToRead:
    content = fileToRead.read()
    print(content.strip())
