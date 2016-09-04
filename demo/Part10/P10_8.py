def readFile(filename):
    counts = 0
    try:
        with open(filename) as fileObj:
            lines = fileObj.readlines()
    except FileNotFoundError:
        pass
        # print('file '+filename+' not found ')
    else:
        print('content in file: ' + filename + ' is follow: \n')
        for line in lines:
            counts += line.count('cat')
            print(line.strip())
        print('there are ' + str(counts) + ' cats \n')


file1 = 'cats.txt'
file2 = "dogs.txt"

readFile(file1)
readFile(file2)
