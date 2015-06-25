from math import sqrt

a1 = 0.4
a2 = 0.018
b1 = 0.8
b2 = 0.023

class Vector(object):

	def __init__(self, x_param = 0, y_param = 0):
		self.x = x_param
		self.y = y_param

	def __add__(self,other):
		return Vector(self.x + other.x, self.y + other.y)

	def __mul__(self, other):
		return Vector(self.x * other.x, self.y * other.y)
	
	def __str__(self):
		return "[%.2f , %.2f]" % (self.x, self.y)

def rk4(h, x, y):
	h_vector = Vector(h,h)
	k1 = h_vector * f(x, y)
	#print "K1: ", k1
	k2 = h_vector * f(x + (0.5 * k1.x), y + (0.5 * k1.y))
	#print "K2: ", k2
	k3 = h_vector * f(x + (0.5 * k2.x), y + (0.5 * k2.y))
	#print "K3: ", k3
	k4 = h_vector * f(x + k3.x, y + k3.y)
	#print "K4: ", k4
	k_final = (k1 + k2 + k2 + k3 + k3 + k4)
	sol = Vector(k_final.x / 6, k_final.y / 6)
	#print "KF: ", sol
	#print "Sol: ", (sol + Vector(x,y))
	return (sol + Vector(x,y))
 
def solver(t0, tf, h, inicial):
	n = int((tf - t0) / float(h) )
	vx = [0]*(n + 1)
	vy = [0]*(n + 1)
	vx[0] = x = inicial.x
	vy[0] = y = inicial.y
	for i in xrange(n):
		r = rk4(h,x,y)
		#print r
		vx[i] = x = r.x
		vy[i] = y = r.y
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
	print "[%.2f , %.2f]" % (x0 + r.x, y0 + r.y)

def main():
	x0 = 30
	y0 = 4
	t0 = 0
	tf = 30
	h = 0.1
	print f(x0,y0)
	condiciones_iniciales = Vector(x0, y0)

	vx, vy = solver(t0, tf,h, condiciones_iniciales)
	for x, y in list(zip(vx, vy))[::10]:
		r = f(x,y)
		print "%.2f\t%.2f\t%.2f\t%.2f" % (x, y, r.x,r.y)


main()
