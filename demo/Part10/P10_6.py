def inputNumber():
    msg = 'please input a number : '
    error = 'input type error, please reinput'
    try:
        numbers = input(msg)
        if numbers == 'quit':
            return numbers
        else:
            value = int(numbers)
    except ValueError:
        print(error)
    else:
        print('you have input ' + str(value) + '\n input \'quit\' to exit')
        return value


# inputNumber()
while 1:
    returnvalue = inputNumber()
    if returnvalue == 'quit':
        break

