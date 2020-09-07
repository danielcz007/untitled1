

class Person:
    name = 'daniel'
    age = 0
    gender = 'man'
    weight = 0
    hight = 0
    subject = ['math','Chinese','Chemistry','Physics','English']
    #构造方法，在类 实例化的时候被调用
    def __init__(self,name,age,gender,weight,hight,subject):
        print('init函数被调用')
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.hight = hight
        self.subject = subject
    @classmethod #类方法可以通过加装饰器，这样就可以用类直接访问该方法。一般来讲方法只能通过实例来访问，类本身不能访问。只有加了装饰器之后才可以访问
    def eat(self):
        # print('eatting：')
        print(f"{self.name},eatting someting")
    def play(self):
        print(f"{self.name} love playing games")
    def jump(self):
        print(f"{self.name} favourite sports is jumpping")
    def study(self):
        print(f"{self.name} need good good study,and day day up,because he's age is {self.age}")
student = Person('bertty',30,'man',70,178,'math')#（）里面要填什么值？是根据构造方法决定的。构造方法里面设定了具体值，那么在
                                                #进行实例化时，就必须要传入相应的值
student.eat()
student.jump()
student.play()
student.study()
print(f"张三的名称是：{student.name},年龄是：{student.age},学科是：{student.subject}")
Person.eat()