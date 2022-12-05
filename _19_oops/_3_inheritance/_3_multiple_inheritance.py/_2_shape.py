# class circle:
#     def circle_area(self, pi=3.14,):
#         area = pi**2
#         print("Area of circle:", area)

# class Square:
#     def squ_area(self, side):
#         area = side*side
#         print("Area of Square:", area)

# class Rectangle:
#     def rec_area(self,height,width):
#         area=height*width
#         print("Area of Rectangle:",area)
        
# class triangle:
#     def triangle_area(self, b,h):
#         area = b*h/2
#         print("Area of triangle:", area)


# class area(circle,Square,Rectangle,triangle):
#     def area(self):
#         print("Area of Square:", area)

# obj = area()
# obj.rec_area(20,20)
# obj.squ_area(12)
# obj.triangle_area(2,3)
# obj.circle_area(2)







# Keeping it, though it's incomplete (just for reference purpose)

# import math
# class circle:
#     def area_circle(self):
#         self.rad=int(input("Enter the radius:"))
#         self.cir_area=math.pi()*self.rad**2
#     def display_circle(self):
#         return self.cir_area

# class square:
#     def area_square(self):
#         self.size=int(input("Enter the side value for square:"))
#         self.squ_area=self.size**2
#     def display_square(self):
#         return self.squ_area

# class triangle:
#     def area_triangle(self):
#         self.base=int(input("Enter the base value:"))
#         self.height=int(input("Enter the height:"))
#         self.tri_area=1/2*(self.base*self.height)
#     def display_triangle(self):
#         return self.tri_area

# class rectangle:
#     def area_rectangle(self):
#         self.breadth=int(input("Enter the breadth:"))
#         self.length=int(input("Enter the length:"))
#         self.rect_area=self.breadth*self.length
#     def display_rectangle(self):
#         return self.rect_area










# class area_circle:
# 	def c_area(self):
# 		rad = int(input("Enter radius of the circle: "))
# 		self.area = 3.16*rad*rad
# 	def c_display(self):
# 		print("Area of the circle:", self.area)

# class area_square:
# 	def s_area(self):
# 		side = int(input("Enter length of side of the square: "))		
# 		self.area = side*side
# 	def s_display(self):
# 		print("Area of the square:", self.area)

# class area_rectangle:
# 	def s_area(self):
# 		len = int(input("Enter length of the rectangle: "))
# 		wide = int(input("Enter width of the rectangle: "))
# 		self.area = len*wide
# 	def r_display(self):
# 		print("Area of the rectangle:", self.area)

# class area_triangle:
# 	def t_area(self):
# 		height = int(input("Enter height of the triangle: "))
# 		base = int(input("Enter length of base of the triangle: "))
# 		self.area = 1/2*(base*height)
# 	def t_display(self):
# 		print("Area of the triangle:", self.area)

# class Area(area_circle,area_square,area_rectangle,area_triangle):
# 	def ques(self):
# 		shape = input("What do you want to find the Area for? ").lower()
# 		return shape


# obj = Area()
# shape = obj.ques()
# if 	shape == "circle":
# 	obj.c_area()
# 	obj.c_display()
# elif shape == "square":
# 	obj.s_area()
# 	obj.s_display()
# elif shape == "rectangle":
# 	obj.r_area()
# 	obj.r_display()
# elif shape == "triangle":
# 	obj.t_area()
# 	obj.t_display()

# else: 
# 	print("Invalid Input, try again!")
