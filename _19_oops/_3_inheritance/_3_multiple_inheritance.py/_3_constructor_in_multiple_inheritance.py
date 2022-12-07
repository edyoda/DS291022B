class mom:
    def __init__(self,name):
        self.name = name
        print("Mom Constructor")

    def property(self):
        print("Jewellery")

class dad:
    def __init__(self,address):
        self.address = address
        print("Dad Constructor")

    def property(self):
        print("Flat")

class son(dad,mom):
    def __init__(self,age):
        mom.__init__(self,"abc")
        dad.__init__(self,"xyz")
        self.age = age

    def property(self):
        mom.property(self)
        dad.property(self)
        print("Mobile")

obj = son(15)
obj.property()
    