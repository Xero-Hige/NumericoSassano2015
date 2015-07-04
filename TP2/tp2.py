import matplotlib.pyplot as plt

A1 = 0.4
A2 = 0.018
B1 = 0.8
B2 = 0.023


class Vector(object):
    def __init__(self, x_param=0.0, y_param=0.0):
        self.x = x_param
        self.y = y_param

    def dividir(self, numero):
        self.x /= float(numero)
        self.y /= float(numero)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __str__(self):
        return "[%.5f , %.5f]" % (self.x, self.y)


def rk4(h, x, y):
    h_vector = Vector(h, h)
    k1 = h_vector * f(x, y)
    k2 = h_vector * f(x + (0.5 * k1.x), y + (0.5 * k1.y))
    k3 = h_vector * f(x + (0.5 * k2.x), y + (0.5 * k2.y))
    k4 = h_vector * f(x + k3.x, y + k3.y)
    sol = (k1 + k2 + k2 + k3 + k3 + k4)
    sol.dividir(6)
    return sol + Vector(x, y)


def solver(t0, tf, h, inicial):
    n = int((tf - t0) / float(h))
    vx = []
    vy = []
    x = inicial.x
    y = inicial.y
    vx.append(x)
    vy.append(y)

    for i in xrange(n):
        r = rk4(h, x, y)
        x = r.x
        y = r.y
        vx.append(x)
        vy.append(y)
    return vx, vy


def f(x, y):
    f1 = A1 * x - A2 * x * y
    f2 = -B1 * y + B2 * x * y
    return Vector(f1, f2)


def solutions_graph(time, vx, vy):
    plt.suptitle('Soluciones')

    plt.plot(time, vx, 'g-', )
    plt.annotate('x, presa', xy=(time[10], vx[10]), xytext=(time[10] + 3, vx[10] + 3),
                 arrowprops=dict(facecolor='green', shrink=0.05), )
    plt.plot(time, vy, 'r--')
    plt.annotate('y, depredador', xy=(time[-10], vy[-10]), xytext=(time[-10] + 3, vy[-10] + 3),
                 arrowprops=dict(facecolor='red', shrink=0.05), )
    plt.grid(True)
    plt.yticks(range(0, int(max(vx) + 2), 5))
    plt.xticks(range(int(time[-10] + 3) + 2))
    plt.show()


def space_graph(vx, vy):
    plt.suptitle("Estado - Espacio")

    plt.plot(vx, vy, 'b-o', )
    plt.grid(True)
    plt.xlabel('x presa')
    plt.ylabel('y predador')
    plt.yticks(range(0, int(max(vy) + 2), 5))
    plt.xticks(range(0, int(max(vx) + 2), 5))
    plt.show()


def main():
    try:
        x0 = float(raw_input("Ingrese el valor de x(0) siendo x las presas: (30 por defecto) "))
    except ValueError:
        x0 = 30.0
    try:
        y0 = float(raw_input("Ingrese el valor de y(0) siendo y los depredadores: (4 por defecto) "))
    except ValueError:
        y0 = 4.0
    t0 = 0
    tf = 30
    h = 0.1
    condiciones_iniciales = Vector(x0, y0)

    vx, vy = solver(t0, tf, h, condiciones_iniciales)

    """# ~ with open('out.csv', 'wb') as csvfile:
    #~ writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #~ ti = t0
    #~ for i in xrange(len(vx)):
    #~ l1 = "%.2f" % ti
    #~ l2 = "%.10f" % vx[i]
    #~ l3 = "%.10f" % vy[i]
    #~ writer.writerow([l1,l2,l3])
    #~ ti += h"""

    ti = t0
    time = []

    print "Para x(0)=%.4f y y(0)=%.4f" % (x0, y0)
    print "Con a1=%.4f, a2=%.4f, b1=%.4f y b2=%.4f" % (A1, A2, B1, B2)
    print "ti\t\t|\t\tx(ti)\t\t|\t\ty(ti)"
    for i in xrange(len(vx)):
        time.append(ti)
        print "%05.2f \t| %014.10f \t| %014.10f" % (ti, vx[i], vy[i])
        ti += h

    solutions_graph(time, vx, vy)
    space_graph(vx, vy)


main()
