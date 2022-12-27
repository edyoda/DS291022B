from ticketbooking import movie_ticket

class Main:
    def execute(self,choice):
        if choice == 1:
            print("***************Show the seats****************")
            movie_ticket_obj.show_seats()
        if choice == 2:
            print("***************Buy a ticket****************")
            movie_ticket_obj.buy_ticket()
        if choice == 3:
            print("***************Statistics****************")
            movie_ticket_obj.statistics()
        if choice == 4:
            print("***************Show booked tickets user info****************")
            movie_ticket_obj.user_info()
        if choice == 0:
            print("***************Thank You for connecting with us! Good Day!****************")
            exit()

if __name__ == "__main__":
    rows = int(input("Enter the number of rows : "))
    columns = int(input("Enter the number of seats in each row : "))

    movie_ticket_obj = movie_ticket(rows,columns)
    obj = Main()

    while True:
        choice = int(input("Enter \n1.Show the seats \n2.Buy a ticket \n3.Statistics \n4.Show booked tickets user info \n0.Exit \n"))
        obj.execute(choice)






