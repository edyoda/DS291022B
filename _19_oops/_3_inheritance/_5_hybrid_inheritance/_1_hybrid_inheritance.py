# Hybrid Inheritance - a program contains two or more inheritance is known as hybrid inheritance

class A:
	def a(self):
		print("A method")

class B(A):
	def b(self):
		print("B method")

class C(A):
	def c(self):
		print("C method")

class D(B):
	def d(self):
		print("D method")

class E(B):
	def e(self):
		print("E method")

class F(C):
	def f(self):
		print("F method")

class G(E,F):
	def g(self):
		print("G method")

b_obj = B()
b_obj.b()
b_obj.a()
print()

c_obj = C()
c_obj.c()
c_obj.a()
print()

d_obj = D()
d_obj.d()
d_obj.b()
d_obj.a()
print()

e_obj = E()
e_obj.e()
e_obj.b()
e_obj.a()
print()

f_obj = F()
f_obj.f()
f_obj.c()
f_obj.a()
print()

g_obj = G()
g_obj.a()
g_obj.b()
g_obj.c()
g_obj.e()
g_obj.f()
g_obj.g()
