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
		return "[%.5f , %.5f]" % (self.v1, self.v2)

def rk4(h, x, y):
	h_vector = Vector(h,h)
	k1 = h_vector * f(x, y)
	#print k1
	k2 = h_vector * f(x + 0.5 * k1.v1, y + 0.5 * k1.v2)
	#print k2
	k3 = h_vector * f(x + 0.5 * k2.v1, y + 0.5 * k2.v2)
	#print k3
	k4 = h_vector * f(x + k3.v1, y + k3.v2)
	#print k4
	k_final = (k1 + k2 + k2 + k3 + k3 + k4)
	#print k_final
	sol = Vector(k_final.v1 / 6, k_final.v2 / 6)
	print sol + Vector(x,y)
	return sol + Vector(x,y)
 
def solver(t0, tf, h, inicial):
	n = int((tf - t0) / float(h) )
	vx = [0]*(n + 1)
	vy = [0]*(n + 1)
	vx[0] = x = inicial.v1
	vy[0] = y = inicial.v2
	for i in xrange(n):
		r = rk4(h,x,y)
		#print r
		vx[i] = x = r.v1
		vy[i] = y = r.v2
	return vx, vy
 
def f(x, y):
	f1 = a1 * x - a2 * x * y
	f2 = -b1 * x + b2 * x * y
	return Vector(f1,f2)
	
def prueba():
	h = 0.1
	x0 = 30
	y0 = 4
	r = rk4(h, x0, y0)
	print r
	print "[%.2f , %.2f]" % (x0 + r.v1, y0 + r.v2)

def main():
	x0 = 30
	y0 = 4
	t0 = 0
	tf = 30
	h = 0.1
	condiciones_iniciales = Vector(x0, y0)

	vx, vy = solver(t0, tf,h, condiciones_iniciales)
	"""for x, y in list(zip(vx, vy))[::10]:
		print(x, y, y - (4 + x*x)**2/16)"""


main()
