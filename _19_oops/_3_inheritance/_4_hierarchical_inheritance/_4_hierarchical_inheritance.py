# Hierarchical Inheritance - single parent class and multiple child classes.

class country:
    def region(self):
        print("Country is a region")

class India(country):
    def language(self):
        print("Hindi")

    def game(self):
        print("Hockey")

class USA(country):
    def language(self):
        print("English")

    def game(self):
        print("Baseball")

india = India()
india.region()
india.language()
india.game()

usa = USA()
usa.region()
usa.language()
usa.game()



class A:
    def a():
        print("A Class")
