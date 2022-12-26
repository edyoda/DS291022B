class movie_ticket:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.user_details = {}

    def show_seats(self):
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if i == 0:
                    if j == 0:
                        print(" ",end=" ")
                    else:
                        print(j,end=" ")
                elif j == 0:
                    print(i, end=" ")
                else:
                    print("S",end=" ")
            print()

    def buy_ticket(self):
        row = int(input("Enter the row number : "))
        column = int(input("Enter the column number : "))

        ticket_price = 10
        seat_no = str(row) + str(column) #24

        option = int(input(f"Your opt row is {row} and column is {column}, so the price for your seat is Rs.{ticket_price}.If you still wish to book the ticket please enter \n1.Yes \n2.No \n"))

        if option == 1:
            name = input("Enter your name : ")
            gender = input("Enter your gender : ")
            age = int(input("Enter your age : "))
            phone_no = int(input("Enter your mobile no : "))
            self.user_details[seat_no]=[name,gender,age,phone_no]
            print(self.user_details)
            print("Booked Successfully")
        else:
            print("No Problem! Thank You for connecting with Book my Show!!!")

    def statistics(self):
        ticket_price = 10
        total_seat = self.rows * self.columns
        tickets_purchased = len(self.user_details)
        percentage_sold = (len(self.user_details) / total_seat) * 100
        current_income = len(self.user_details) * ticket_price
        total_income = ticket_price * total_seat
       
        print(f"Number of tickets purchased: {tickets_purchased}")
        print(f"Percentage of seats sold: {percentage_sold}%")
        print(f"Current income from ticket sales: Rs.{current_income}")
        print(f"Total income from ticket sales: Rs.{total_income}")
        
        


    