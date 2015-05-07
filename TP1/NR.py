import math
import sys

ERROR_LIMIT = 0.00000000002
MAX_ITERATIONS = 1000


class Function(object):
    def eval(self, l):
        pass


class Original(Function):
    def eval(self, l):
        return (l ** 2) - (8 * l) + 16


class Derived(Function):
    def eval(self, l):
        return (2 * l) - 8


class Second_Derived(Function):
    def eval(self, l):
        return 2


def resolve_by_nr(f, ff, x0):
    i = 0
    error = 1

    while (error > ERROR_LIMIT) and (i < MAX_ITERATIONS):
        f0 = f.eval(x0)
        f1 = ff.eval(x0)

        x1 = x0 - (f0 / f1)

        i += 1

        error = abs((x1 - x0) / x1)

        x0 = x1

        if f.eval(x1) == 0:
            error = 0
            break

    return x0, i, error


def main(args):
    function = Original()
    derived_function = Derived()
    second_derived_function = Second_Derived()

    x0 = args[1] / 2.0

    # Busco el 0 de la derivada, aka el punto critico
    root, iterations, error = resolve_by_nr(derived_function, second_derived_function, x0)

    # TODO: Ver por si tiene varias raices (no raices multiples)

    # Punto del minimo hallado
    min_x = root

    if (second_derived_function.eval(min_x) > 0):
        min_x = 0  #Tiene que estar en un extremo

    if (function.eval(min_x) > function.eval(0)):
        min_x = 0  #Este extremo es seguro mejor que el punto encontrado

    if (function.eval(min_x) > function.eval(x0 * 2)):
        min_x = x0 * 2  #Este es el minimo

    print 'Min at:', min_x
    print 'Min value:', function.eval(min_x)

# main(sys.argv)
main(["", 11])