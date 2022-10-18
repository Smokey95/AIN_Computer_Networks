# class consists of
# statistics variables
# and methods as described in the problem description
import ClassEvent as Event

class Customer():
    
    served = dict()
    dropped = dict()
    complete = 0
    duration = 0
    duration_cond_complete = 0
    count = 0
    
    def __init__(self, einkaufsliste, name, start):
        self.einkaufsliste = einkaufsliste
        self.name = name
        self.start = start
        self.end = 0
        Customer.count += 1
        #my_print1(self.name, 'Ankunft', 'at')

    def run(self):
        #my_print1(self.name, 'Start', 'at')
        self.einkaufsliste[0][1].add(self)
        ev = Event(self.start + self.einkaufsliste[0][0], self.run2, args=(self.einkaufsliste[0][1],), prio=1)
        evQ.push(ev)
        #my_print1(self.name, 'Ende', 'at')