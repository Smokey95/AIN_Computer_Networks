from ClassCustomer import *
from ClassStation import *
from threading import Thread
from ClassUtility import *
import time

def startCustomers(einkaufsliste, name, sT, dT, mT):
    i = 1
    t = sT
    while t < mT:
        kunde = Customer(list(einkaufsliste), name + str(i), (t / utility.debug_factor))
        kunde.start()
        i += 1
        t += dT

def printHeader():
    #print("------ Simulation started -------")
    print("|-------------------------------------------------------------")
    print("| Element     |     Value | Action                            ")
    print("|-------------------------------------------------------------")
        
printHeader()


baecker = Station(10, 'Bäcker')
baecker.start()

metzger = Station(30, 'Metzger')
metzger.start()

kaese = Station(60, 'Käse')
kaese.start()

kasse = Station(5, 'Kasse')
kasse.start()

Customer.served['Bäcker'] = 0
Customer.served['Metzger'] = 0
Customer.served['Käse'] = 0
Customer.served['Kasse'] = 0
Customer.dropped['Bäcker'] = 0
Customer.dropped['Metzger'] = 0
Customer.dropped['Käse'] = 0
Customer.dropped['Kasse'] = 0

einkaufsliste1 = [(10, baecker, 10, 10), (30, metzger, 5, 10), (45, kaese, 3, 5), (60, kasse, 30, 20)]
einkaufsliste2 = [(30, metzger, 2, 5), (30, kasse, 3, 20), (20, baecker, 3, 20)]

#startCustomers(einkaufsliste1, 'A', 0, 200, 200)
startCustomers(einkaufsliste1, 'A', 0, 200, 30 * 60 + 1)
#+startCustomers(einkaufsliste2, 'B', 1, 60, 30 * 60 + 1)


utility.endSimulationEv.wait()
print("Simulation complete")

#evQ.start()
#print('Simulationsende')
#my_print('Anzahl Kunden: %i' % (Customer.count
#                                ))
#my_print('Anzahl vollständige Einkäufe %i' % Customer.complete)
#x = Customer.duration / Customer.count
#my_print(str('Mittlere Einkaufsdauer %.2fs' % x))
#x = Customer.duration_cond_complete / Customer.complete
#my_print('Mittlere Einkaufsdauer (vollständig): %.2fs' % x)
#S = ('Bäcker', 'Metzger', 'Käse', 'Kasse')
#for s in S:
#    x = Customer.dropped[s] / (Customer.served[s] + Customer.dropped[s]) * 100
#    my_print('Drop percentage at %s: %.2f' % (s, x))
#
#f.close()
#fc.close()
#fs.close()

