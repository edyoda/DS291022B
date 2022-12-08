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

    def update_book():
        pass

    def delete_book():
        pass

    def search_book_by_ID():
        pass

    def search_book_by_name():
        pass

    def view_book():
        pass
