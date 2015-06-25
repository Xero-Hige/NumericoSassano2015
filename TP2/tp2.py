from math import sqrt

a1 = 0.4
a2 = 0.018
b1 = 0.8
b2 = 0.023

class Vector(object):

	def __init__(self, vec1 = 0, vec2 = 0):
		self.v1 = vec1
		self.v2 = vec2

	def __add__(self,other):
		return Vector(self.v1 + other.v1, self.v2 + other.v2)

	def __mul__(self, other):
		return Vector(self.v1 * other.v1, self.v2 * other.v2)
	
	def __str__(self):
		return "[%.2f , %.2f]" % (self.v1, self.v2)

def rk4(h, x, y):
	h_vector = Vector(h,h)
	k1 = h_vector * f(x, y)
	print k1
	k2 = h_vector * f(x + 0.5 * k1.v1, y + 0.5 * k1.v2)
	print k2
	k3 = h_vector * f(x + 0.5 * k2.v1, y + 0.5 * k2.v2)
	print k3
	k4 = h_vector * f(x + k3.v1, y + k3.v2)
	print k4
	k_final = (k1 + k2 + k2 + k3 + k3 + k4)
	print k_final
	return k_final.v1 / 6, k_final.v2 / 6
 
def solver(f, x0, y0, x1, h):
	vx = [0]*(n + 1)
	vy = [0]*(n + 1)
	n = (x1 - x0)/h
	vx[0] = x = x0
	vy[0] = y = y0
	for i in range(1, n + 1):
		vx[i] = x = x0 + i*h
		vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4)/6
	return vx, vy
 
def f(x, y):
	f1 = a1 * x - a2 * x * y
	f2 = -b1 * x + b2 * x * y
	return Vector(f1,f2)


def main():
	print "Hola"
	h = 0.1
	x0 = 10
	y0 = 5
	r = rk4(h, x0, y0)
	print r
	print "[%.2f , %.2f]" % (x0 + r[0], y0 + r[1])

"""
	vx, vy = rk4(f, 0, 1, 10, 0.1)
	for x, y in list(zip(vx, vy))[::10]:
		print(x, y, y - (4 + x*x)**2/16)
"""

main()

