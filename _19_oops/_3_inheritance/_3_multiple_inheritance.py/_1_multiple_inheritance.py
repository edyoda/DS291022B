# Multiple Inheritance - mulitple parent classes and single child classes
class c_lang:
    def procedural_feature(self):
        print("Procedural Feature!")

    def language(self):
        print("C Language!")

class cpp_lang:
    def oops_feature(self):
        print("Object Oriented Feature!")

    def language(self):
        print("Cpp Language!")

class python_lang(cpp_lang,c_lang):
    def both(self):
        print("It has both procedural and oops feature")

    def language(self):
        print("Python Language")

obj = python_lang()
obj.oops_feature()
obj.procedural_feature()
obj.both()
obj.language()


print(python_lang.mro()) # Method Resolution Order
print(python_lang.__mro__)

