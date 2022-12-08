class Book:
	def __init__(self, book_ID, book_name, book_author_name, book_edition, book_publisher, book_price):
		self.book_name = book_name
		self.book_ID = book_ID
		self.book_author_name = book_author_name
		self.book_edition = book_edition
		self.book_publisher = book_publisher
		self.book_price = book_price

	def __str__(self):
		return f"Book details: \nBook name: {self.book_name} \nBook ID: {self.book_ID} \nBook Author name: {self.book_author_name} \nBook Publisher : {self.book_publisher} \nBook Edition: {self.book_edition} \nBook Price: {self.book_price}"

	def set_book_name(self, book_name):
		self.book_name = book_name

	def get_book_name(self):
		return self.book_name

	def set_book_ID(self, book_ID):
		self.book_ID = book_ID

	def get_book_ID(self):
		return self.book_ID

    # def set_book_edition(self,book_edition):
    #     self.book_edition = book_edition

    

    # def get_book_edition(self):
    #     return self.book_edition

    # def set_book_author_name(self,book_author_name):
    #     self.book_author_name = book_author_name

    # def get_book_author_name(self):
    #     return self.book_author_name
    
    # def set_book_publisher(self,book_publisher):
    #     self.book_publisher = book_publisher

    # def get_book_publisher(self):
    #     return self.book_publisher
    
    # def set_book_price(self,book_price):
    #     self.book_price = book_price

    # def get_book_price(self):
    #     return self.book_price

