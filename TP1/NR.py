import math
import sys

ERROR_LIMIT = 0.00000000002
MAX_ITERATIONS = 1000

class Function(object):
    
    def eval(self,l):
        pass

class Original(Function):

    def eval(self,l):
        return (l**2)-(8*l)+16

class Derived(Function):

    def eval(self,l):
        return (2*l)-8

def main(argv):

    x0=argv[1]/2.0
    i=0
    error=1

    f = Original()
    ff = Derived()

    while (error>ERROR_LIMIT) and (i<MAX_ITERATIONS):
        f0=f.eval(x0)
        f1=ff.eval(x0)

        x1=x0-(f0/f1)

        i+=1

        error=abs((x1-x0)/x1);
        
        x0 = x1

        if f.eval(x1) == 0:
            error = 0;
            break     
            
    print "Root: ", x0
    print "Iterations: ", i
    print "Error: ", error
    print "Value: ", f.eval(x0)

#main(sys.argv)
main(["",11])