#异常的处理流程：
# 检测到错误--引发异常--捕获异常
'''
异常通常可以有开发人员处理，但是错误就不能一般是系统级别的
实例：
num1 = int (input("输入一个除数"))
num2 = int (input("输入一个被除数"))
print(bum1/num2)
'''

# num1 = int (input("输入一个除数"))
# num2 = int (input("输入一个被除数"))
# print(num1/num2)
#但是由于被除数分母，不能为0，如果为0时就是出现异常,其中ZeroDivisionError为异常类型
'''
Traceback (most recent call last):
  File "D:/python3/untitled1/venv/错误与异常.py", line 12, in <module>
    print(num1/num2)
ZeroDivisionError: division by zero
'''
try:
    num1 = int(input("输入一个除数"))
    num2 = int(input("输入一个被除数"))
    print(num1 / num2)
except ZeroDivisionError:
    print('除数不能为0')
except:
    print("除数不能为非数字类型")
#没有异常
else:
    print('没有异常')
finally:
    print('无论有没有异常都会输出：计算结束')
