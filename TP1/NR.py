import math
import sys

#ERROR_LIMIT = 0.00000000002
ERROR_LIMIT = 0.001
MAX_ITERATIONS = 1000
PI = 3.1416

class Function(object):
	def eval(self, l):
		pass

class Original(Function):	
	def eval(self, l, L = 100):
		return (((1 / (64 * (PI**3))) * ((L - (4 * l)) ** 4)) + ((l ** 4) / 12))

class Derived(Function):
	def eval(self, l, L = 100):
		return ((((-1) / (4 * (PI **3))) * ((L - (4 * l)) ** 3)) + ((l ** 3) / 3))

class Second_Derived(Function):
	def eval(self, l, L = 100):
		return ((3 / (PI**3)) * ((L - (4 * l)) ** 2) + (l ** 2))

class Relation(Function):
	def eval(self, l, L):
		return L - l

def resolve_by_nr(f, ff, x0,L = 100):
	i = 0
	error = 1
	print "Xi+1    |    Xi    |    Error"

	while (error > ERROR_LIMIT) and (i < MAX_ITERATIONS):
		f0 = f.eval(x0, L)
		f1 = ff.eval(x0, L)

		x1 = x0 - (f0 / f1)
		i += 1
		error = abs((x1 - x0) / x1)

		print "%.4f    |    %.4f    |    %.4f" % (x1, x0, error)			

		x0 = x1

		if f.eval(x1) == 0:
			error = 0
			break
	return x0, i, error


def main(args):
	
	function = Original()
 	derived_function = Derived()
 	second_derived_function = Second_Derived()
 	relation = Relation()
 	
	
	#~ if (len(sys.argv) > 1):
		#~ x0 = int(args[1]) / 2.0
		#~ L = int(args[1])
	#~ else:
		#~ x0 = 50
		#~ L = 100
	L = float(raw_input("Ingresar la longitud del alambre (numero mayor a 0): "))
	x0 = L / 2.0

	print "Trabajando con x0 = %.4f, a partir de L = %.4f, hasta conseguir error menor a: %.4f" % (x0, L, ERROR_LIMIT)



	# Busco el 0 de la derivada, aka el punto critico
	root, iterations, error = resolve_by_nr(derived_function, second_derived_function, x0, L)



	# Punto del minimo hallado
	min_x = root

	#~ if (function.eval(min_x) > function.eval(0)):
		#~ min_x = 0  #Este extremo es seguro mejor que el punto encontrado
#~ 
	#~ if (function.eval(min_x) > function.eval(x0 * 2)):
		#~ min_x = x0 * 2  #Este es el minimo

	print 'Minimo en x = %.4f' % (min_x)
	print 'Valor del minimo: %.4f' % (function.eval(min_x, L))
	print 'l = %.4f' % (min_x)
	print 'r = %.4f' % (relation.eval(min_x, L))

main(sys.argv)
