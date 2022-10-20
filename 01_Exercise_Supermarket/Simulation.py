
import os

from ClassEventQueue import EventQueue
from ClassStation import Station
from ClassCustomer import Customer
from ClassEvent import Event

#--------------------------------------------------------------------------------------------------- File handling
directory_path = os.getcwd()
f = open(directory_path + "\\01_Exercise_Supermarket\data\supermarkt.txt", "w")
fc = open(directory_path + "\\01_Exercise_Supermarket\data\supermarkt_customer.txt", "w")
fs = open(directory_path + "\\01_Exercise_Supermarket\data\supermarkt_station.txt", "w")

# print on console and into supermarket log
def my_print(msg):
    print(msg)
    f.write(msg + '\n')


# print on console and into customer log
# k: customer name
# s: station name
def my_print1(k, s, msg):
    t = EventQueue.time
    print(str(round(t, 4)) + ':' + k + ' ' + msg + ' at ' + s)
    fc.write(str(round(t, 4)) + ':' + k + ' ' + msg + ' at ' + s + '\n')


# print on console and into station log
# s: station name
# name: customer name
def my_print2(s, msg, name):
    t = EventQueue.time
    print(str(round(t,4))+':'+s+' '+msg)
    fs.write(str(round(t, 4)) + ':' + s + ' ' + msg + ' ' + name + '\n')


# einkaufsliste: 
# name: Customer type
# start time: time when first customer arrives at supermarket
# delta time: Time between two customers
# maxSimulationTime: max time
def startCustomers(einkaufsliste, name, startTime, deltaTime, maxSimulationTime):
    i = 1
    t = startTime
    while t < maxSimulationTime:
        kunde = Customer(list(einkaufsliste), name + str(i), t)
        event = Event(t, kunde.begin, prio=1, args=(kunde.name))
        eventQueue.push(event)
        i += 1
        t += deltaTime


eventQueue = EventQueue()

#--------------------------------------------------------------------------------------------------- Create Stations
baecker = Station(10, 'Bäcker')
metzger = Station(30, 'Metzger')
kaese = Station(60, 'Käse')
kasse = Station(5, 'Kasse')
#--------------------------------------------------------------------------------------------------- Init Customer log
Customer.served['Bäcker'] = 0
Customer.served['Metzger'] = 0
Customer.served['Käse'] = 0
Customer.served['Kasse'] = 0
Customer.dropped['Bäcker'] = 0
Customer.dropped['Metzger'] = 0
Customer.dropped['Käse'] = 0
Customer.dropped['Kasse'] = 0

# List =          (Time Way, Name Station, Amount, max. customer)
einkaufsliste1 = [(10, baecker, 10, 10), 
                  (30, metzger, 5, 10), 
                  (45, kaese, 3, 5), 
                  (60, kasse, 30, 20)]
einkaufsliste2 = [(30, metzger, 2, 5),
                  (30, kasse, 3, 20),
                  (20, baecker, 3, 20)]

#startCustomers(einkaufsliste1, 'A', 0, 200, 30 * 60 + 1)
#startCustomers(einkaufsliste2, 'B', 1, 60, 30 * 60 + 1)
startCustomers(einkaufsliste1, 'A', 0, 200, 30)
startCustomers(einkaufsliste2, 'B', 1, 60, 30)



#print(eventQueue)

eventQueue.start()

#--------------------------------------------------------------------------------------------------- Print Customer log
my_print('| Simulationsende: %is' % EventQueue.time)
my_print('| Anzahl Kunden: %i' % (Customer.count))
my_print('| Anzahl vollständige Einkäufe %i' % Customer.complete)
x = Customer.duration / Customer.count
my_print(str('| Mittlere Einkaufsdauer %.2fs' % x))
x = Customer.duration_cond_complete / Customer.complete
my_print('| Mittlere Einkaufsdauer (vollständig): %.2fs' % x)
S = ('Bäcker', 'Metzger', 'Käse', 'Kasse')
for s in S:
    x = Customer.dropped[s] / (Customer.served[s] + Customer.dropped[s]) * 100
    my_print('| Drop percentage at %s: %.2f' % (s, x))

#--------------------------------------------------------------------------------------------------- Close files
f.close()
fc.close()
fs.close()

eventQueue.printEnd()