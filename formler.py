import math
import sys

def ki_andele(andel, n):
    print('ki andele udrenginger:')
    print('Andel er: '+str(andel))
    print('Stik proveantel er: '+ str(n))
    print('Ovre graenese er:  ' + str(andel + 1.96 * math.sqrt(andel*(1-andel)/n)))
    print('Nedre graenese er: ' + str(andel - 1.96 * math.sqrt(andel*(1-andel)/n)))

def choose_eq():
    if(sys.argv[1] == "ki_andel"):
        ki_andele(float(sys.argv[2]),float(sys.argv[3]))

choose_eq()
