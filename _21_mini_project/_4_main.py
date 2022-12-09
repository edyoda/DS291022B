from _3_funtionality import BookOperation

class Main:
    def execute(self,choice,book_operation):
        if choice == 1:
            book_operation.add_book()

        if choice == 2:
            book_operation.view_book()

        if choice == 3:
            book_ID = int(input("Enter Book ID : "))
            book_operation.search_book_by_ID(book_ID)

        if choice == 4:
            book_operation.delete_book()

        if choice == 5:
            book_operation.update_book()

        if choice == 6:
            book_operation.search_book_by_name()

if __name__ == "__main__":
    obj = Main()
    book_operation = BookOperation()
    
    while True:
        choice = int(input("Enter \n1.Add Book \n2.View Book \n3.Search Book by ID \n4.Delete Book \n5.Update Book \n6.Search Book by Book Name \n"))
        obj.execute(choice=choice,book_operation=book_operation)

    
