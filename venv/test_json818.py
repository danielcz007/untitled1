import json
#json由字典和列表组成
#json的常用方法 ：
    # dumps() 将数据类型转化为字符串
    # loads() 将字符串转化为json
    # dump()  将数据类型转换成字符串并储存在文件中
    # load()  打开文件，并把里面的字符串转换成数据类型

data={
    "name":['daniel','chen','zheng'],
    "age":18,
    "gender":"female"
}
print(type(data))
print(data)
data1 = json.dumps(data)
print(type(data1))
print(data1)
data2 = json.loads(data1)
print(type(data2))
print(data2)