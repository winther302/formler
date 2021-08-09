import math
import sys

def help():
    print("Du har følgende funktioner at bruge:")
    print("ki_andele, skriv \"formler ki_andele 0.89 129\" hvor første tal er andel og andet er stikprøve antal(n)\n")
    print("ki_avg skriv \"formler ki_avg 6.61 0.95 1400 \" hvor 1. tal er andel, 2. er standardafvigelse og 3. er N\n")
    print("n_endele skriv \"formler n_andele 0.043 1.96 0.022\" hvor 1. tal er gennemsnit, 2. tal er standardafviglese og 3. tal er N")

def ki_avg(u, q, n):
    print('ki gennemsnit udrenginger: ')
    print('Gennemsnit: ' + str(u))
    print('standardafvigelse: ' + str(q))
    print('Stik proveantel er: '+ str(n))
    print('Ovre K.I er:  ' + str(u + 1.96 * q/math.sqrt(n)))
    print('Nedre K.I er:  ' + str(u - 1.96 * q/math.sqrt(n)))

def n_andele(andel, interval, m):
    print('N ved andele:')
    print('Andel: ' + str(andel))
    print('Interval: ' + str(interval))
    print('M: ' + str(m))
    print('Resultat: ' + str(andel*(1-andel)*(interval/m)**2))

def ki_andele(andel, n):
    print('ki andele udrenginger: andele +/- * sqrt(andel*(1-andel)/n)')
    print('Andel er: '+str(andel))
    print('Stik proveantel er: '+ str(n))
    print('Ovre K.I er:  ' + str(andel + 1.96 * math.sqrt(andel*(1-andel)/n)))
    print('Nedre K.I er: ' + str(andel - 1.96 * math.sqrt(andel*(1-andel)/n)))

def choose_eq():
    if(len(sys.argv) == 1):
        help()
    elif(sys.argv[1] == "ki_andele"):
        ki_andele(float(sys.argv[2]),float(sys.argv[3]))
    elif(sys.argv[1] == "ki_avg"):
        ki_avg(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
    elif(sys.argv[1] == "n_andele"):
        n_andele(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))



choose_eq()
