
name = "daniel"
age = 30
likesm = [1,2,3]
dirc1 = {'name':'tom','gender':'male'}
#第二种字面量 利用 format()方法获取变量，然后用{} 对变量取值，可以重复使用，也有位置标识，无标识时按照位置顺序取值
print("My name is {},age is {}".format(name,age))
print("my name is {},dict is {}".format(likesm,dirc1))
print("my name is {1},age is {0}".format(likesm,dirc1))
print("my name is {1},age is {0}".format(*likesm))
print("my name is {name},age is {gender}".format(**dirc1))
#第三种字面量 (f"")
print(f"my name is {name},age is {age},my list is {likesm},my dirc is {dirc1}")
print(f"my name is \n{name},age is {age},my list is {likesm},my dirc is {dirc1}")

print(f'my name is {name.upper()},age is {age},my list is {likesm},my dirc is {dirc1}')
print(f"my name is {name.upper()},age is {age},my list is {likesm[0]},my dirc is {dirc1['name']}")

