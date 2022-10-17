# class consists of
# statistics variables
# and methods as described in the problem description
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

# please implement here