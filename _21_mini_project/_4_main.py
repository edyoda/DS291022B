from _3_funtionality import BookOperation

class Main:
    def execute(self,choice,book_operation):
        if choice == 1:
            book_operation.add_book()

        if choice == 2:
            book_operation.view_book()

        if choice == 3:
            pass
        if choice == 4:
            pass
        if choice == 5:
            pass
        if choice == 6:
            pass

if __name__ == "__main__":
    obj = Main()
    book_operation = BookOperation()
    while True:
        choice = int(input("Enter \n1.Add Book \n2.View Book \n3.Search Book by ID \n4.Delete Book \n5.Update Book \n6.Search Book by Book Name \n"))
        
        obj.execute(choice=choice,book_operation=book_operation)

    
