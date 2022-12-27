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
                    if self.is_seat_booked(i,j):
                        print("B",end=" ")
                    else:
                        print("S",end=" ")
            print()

    def buy_ticket(self):
        row = int(input("Enter the row number : "))
        column = int(input("Enter the column number : "))
        total_seat = self.rows * self.columns
        if total_seat <= 60:
            ticket_price = 10
        else:
            first_half = self.rows//2
            if row > first_half:
                ticket_price = 8
            else:
                ticket_price = 10
        seat_no = str(row) + str(column)
        option = int(input(f"Your opt row is {row} and column is {column}, so the price for your seat is Rs.{ticket_price}.If you still wish to book the ticket please enter \n1.Yes \n2.No \n"))
        if option == 1:
            name = input("Enter your name : ")
            gender = input("Enter your gender : ")
            age = int(input("Enter your age : "))
            phone_no = int(input("Enter your mobile no : "))
            self.user_details[seat_no]=[name,gender,age,phone_no,ticket_price]
            print(self.user_details)
            print("Booked Successfully")
        else:
            print("No Problem! Thank You for connecting with Book my Show!!!")

    def statistics(self):
        total_seat = self.rows * self.columns
        tickets_purchased = len(self.user_details)
        percentage_sold = (len(self.user_details) / total_seat) * 100
        price_list = []
        for k,v in self.user_details.items():
            price_list.append(v[4])
        current_income = sum(price_list)
        if total_seat <= 60:
            total_income = total_seat * 10
        else:
           front_price = 10
           back_price = 8
           front_seats = (self.rows//2)*self.columns
           back_seats = total_seat - front_seats
           total_income = front_seats * front_price + back_seats * back_price
        print(f"Number of tickets purchased: {tickets_purchased}")
        print(f"Percentage of seats sold: {percentage_sold}%")
        print(f"Current income from ticket sales: Rs.{current_income}")
        print(f"Total income from ticket sales: Rs.{total_income}")
        
    def user_info(self):
        while True:
            row = int(input("Enter the row number : "))
            column = int(input("Enter the column number : "))
            seat_no = str(row) + str(column)
            user_details = self.user_details.get(seat_no,None)
            if user_details:
                print(f"Name: {user_details[0]}")
                print(f"Gender: {user_details[1]}")
                print(f"Age: {user_details[2]}")
                print(f"Ticket price: {user_details[3]}")
                print(f"Phone number: {user_details[4]}")
            else:
                print("Seat is not booked.")
            cont = input("Enter 'y' to continue or any other key to exit: ")
            if cont.lower() != 'y':
                break

    def is_seat_booked(self,row,column):
        seat_no = str(row) + str(column)
        if seat_no in self.user_details.keys():
            return True
        return False
   