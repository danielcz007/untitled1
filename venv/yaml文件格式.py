import yaml
#YAML "-" 后面需要添加空格！！！！
print(yaml.load("""
    - chen
    - zheng
    - daniel
    - c
    - a
    - 
        - 1
        - 2
    - a: 10  #冒号后也需要空格  ！！！！
""",Loader=yaml.FullLoader))
#dump（）方法生成一个yaml文件
#def dump(data, stream=None, Dumper=Dumper, **kwds):

    # Serialize a Python object into a YAML stream.
    # If stream is None, return the produced string instead.
    #
    # return dump_all([data], stream, Dumper=Dumper, **kwds)
#print(yaml.dump({'a':[1,2,3]}))
#生成了一个demo.yml文件
with open("demo.yml","w") as f:
    yaml.dump(data={'a':[1,2,3,4]},stream = f)