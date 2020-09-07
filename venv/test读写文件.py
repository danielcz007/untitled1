#通常文件的操分为三部
    # 1.打开文件
    # 2.操作文件
    # 3.关闭文件
# print(open('data.txt'))
# f = open('data.txt')
# print(f.readable())
# print(f.readlines())
# #每次取一行
# print(f.readline())
# print(f.readline())
# f.close()
#print(f.read())
#with 代码块 ,可以将文件打开后自动关闭
with open('data.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    #print(f.readlines())