class demo:
    def divison(self,no1,no2):
        div = no1/no2
        print("Division : ",div)

    def div(self):
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        try:
            self.divison(no1,no2)
        except:
            print("Error")

obj = demo()
obj.div()