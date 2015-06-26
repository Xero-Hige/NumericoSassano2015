import csv

a1 = 0.4
a2 = 0.018
b1 = 0.8
b2 = 0.023

class Vector(object):

	def __init__(self, x_param = 0, y_param = 0):
		self.x = x_param
		self.y = y_param
		
	def dividir(self, numero):
		self.x = self.x / float(numero)
		self.y = self.y / float(numero)

	def __add__(self,other):
		return Vector(self.x + other.x, self.y + other.y)

	def __mul__(self, other):
		return Vector(self.x * other.x, self.y * other.y)
	
	def __str__(self):
		return "[%.5f , %.5f]" % (self.x, self.y)


def rk4(h, x, y):
	h_vector = Vector(h,h)
	k1 = h_vector * f(x, y)
	k2 = h_vector * f(x + (0.5 * k1.x), y + (0.5 * k1.y))
	k3 = h_vector * f(x + (0.5 * k2.x), y + (0.5 * k2.y))
	k4 = h_vector * f(x + k3.x, y + k3.y)
	sol = (k1 + k2 + k2 + k3 + k3 + k4)
	sol.dividir(6)
	return (sol + Vector(x,y))

 
def solver(t0, tf, h, inicial):
	n = int((tf - t0) / float(h) )
	vx = []
	vy = []
	x = inicial.x
	y = inicial.y
	vx.append(x)
	vy.append(y)

	for i in xrange(n):
		r = rk4(h,x,y)
		x = r.x
		y = r.y
		vx.append(x)
		vy.append(y)
	return vx, vy
 
def f(x, y):
	f1 = a1 * x - a2 * x * y
	f2 = -b1 * y + b2 * x * y
	return Vector(f1,f2)


def main():
	x0 = 30
	y0 = 4
	t0 = 0
	tf = 30
	h = 0.1
	condiciones_iniciales = Vector(x0, y0)

	vx, vy = solver(t0, tf,h, condiciones_iniciales)

	with open('out.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		ti = t0
		for i in xrange(len(vx)):
			st = "%.2f,%.10f,%.10f" % (ti, vx[i],vy[i])
			print st
			writer.writerow(st)
			ti += h

main()
