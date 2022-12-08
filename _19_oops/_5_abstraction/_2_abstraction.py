from abc import ABC,abstractmethod

class college(ABC):
    @abstractmethod
    def hall_ticket(self):
        pass
    
    def timing(self):
        return "Timing : 10am - 1pm"

class classroomA(college): # 12th science
    def hall_ticket(self):
        return "Science Hall Ticket"

class classroomB(college): # 12th commerce
    def hall_ticket(self):
        return "Commerce Hall Ticket"

class classroomC(college): # 12th arts
    def hall_ticket(self):
        return "Arts Hall Ticket"

class_a = classroomA()
print(class_a.hall_ticket())
print(class_a.timing())

class_b = classroomB()
print(class_b.hall_ticket())
print(class_b.timing())

class_c = classroomC()
print(class_c.hall_ticket())
print(class_c.timing())

