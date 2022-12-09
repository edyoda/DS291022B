from _2_book import Book

class BookOperation:
    booklist = []
    def add_book(self):
        print("*****************Add Book*********************")
        book_Id = int(input("Enter Book ID : "))
        book_name = input("Enter Book Name : ")
        book_author_name = input("Enter Book Author Name : ")
        book_edition = int(input("Enter Book Edition : "))
        book_publisher = input("Enter Book Publisher : ")
        book_price = float(input("Enter Book Price : "))
        book = Book(book_ID=book_Id,book_name=book_name,book_author_name=book_author_name,book_edition=book_edition,book_publisher=book_publisher,book_price=book_price)
        self.booklist.append(book)
        print("Book Added Successfully!!!")

    def update_book(self):
        print("*****************Update Book*********************")
        book_ID = int(input("\nEnter the Book Id to update the Book: "))
        book = self.search_book_by_ID(book_ID)
        if book:
            book.set_book_name(input("Enter the book name:"))
            book.set_book_edition(int(input("Enter the book edition year:")))
            book.set_book_author_name(input("Enter the author name of the book:"))
            book.set_book_publisher(input("Enter the publisher name:"))
            book.set_book_price(float(input("Enter the price of the book:")))
            print("Book is updated successfully")
            

    def delete_book(self):
        print("*****************Delete Book*********************")
        book_ID = int(input("\nEnter the Book Id to delete the Book: "))
        book = self.search_book_by_ID(book_ID)
        if book:
            self.booklist.remove(book)
            # del book
            print("Book deleted successfully!")
            
    # def delete_book(self):
    #     book_ID = int(input("\nEnter the Book Id to delete the Book: "))
    #     for book in self.booklist:
    #         if book.get_book_ID() == book_ID:
    #             self.booklist.remove(book)
    #             # del book
    #             print("Book deleted successfully!")
    #             break
    #     else:
    #         print("\nBook not found!\n")

    # def search_book_by_ID(self):
    #     book_ID = int(input("Enter Book ID : "))
    #     for book in self.booklist:
    #         if book.get_book_ID() == book_ID:
    #             print(f"Book Details : \n{book}")
    #             break
    #     else:
    #         print(f"Book with {book_ID} book ID not found!!!!")

    def search_book_by_ID(self,book_ID):
        print("*****************Search Book by ID*********************")
        for book in self.booklist:
            if book.get_book_ID() == book_ID:
                print(f"Book Details : \n{book}")
                return book
        else:
            print(f"Book with {book_ID} book ID not found!!!!")
            return None


    def search_book_by_name(self):
        print("*****************Search Book by Name*********************")
        book_name = input("\nEnter the Book Name: ")
        for book in self.booklist:
            if book.get_book_name() == book_name:
                print(f"\nDetails of the Book: \n{book}\n")
                break
        else:
            print("\nBook not found!\n")


    def view_book(self):
        print("*****************View Book*********************")
        count = 0
        for i in self.booklist:
            count += 1
            print(f"Details of {count} book \n{i}\n")

