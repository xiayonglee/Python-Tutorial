class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


dog = Dog()
dog.walk()  # 继承自Mammal的定义
dog.bark()  # 在Dog类中定义
