'''
    要多次打开文件读取,个人理解是文件指针到末尾了,
    需要重新打开才能把指针重置回到文件头
'''
filename = 'learning_python.txt'

'''读取整个文件'''
with open(filename) as fileObj:
    content = fileObj.read()
    print('整个文件=' + content)

'''逐行遍历'''
with open(filename) as fileObj:
    line_number = 1
    for line in fileObj:
        print('第' + str(line_number) + '行:' + line.strip())
        line_number += 1

'''存储在列表中'''
with open(filename) as fileObj:
    linelist = fileObj.readlines()

print('存储在列表中的数据是:')
for line in linelist:
    newtxt = line.replace('Python', 'JavaScript')
    print(newtxt.strip())
