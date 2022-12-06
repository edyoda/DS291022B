class Grandpa:
    pass

class Dad(Grandpa):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_dad_info(self):
        print(f"Dad's Name : {self.name} \nDad's Age : {self.age}")


class Son(Dad):
    def __init__(self ,name, age, occupation):
        super().__init__(name,age)
        self.occupation = occupation

    def display_son_info(self):
        print(f"Son's Occupation : {self.occupation}")

son = Son("Ram",78,"Developer")
son.display_son_info()
son.display_dad_info()

# self - represents current class object
# super - represents immediate parent class object
