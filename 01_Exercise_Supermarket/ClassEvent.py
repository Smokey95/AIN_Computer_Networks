class Event:
    """
    ### Class consists of instance variables:
    timeStamp: Time stamp when a event occurs
    work: job to be done
    args: list of arguments for job to be done
    prio: used to give leaving, being served, and arrival different priorities
    """
    counter = 0

    def __init__(self, timeStamp, work, args=(), prio=255):
        self.t = timeStamp
        self.n = Event.counter
        self.work = work
        self.args = args
        self.prio = prio
        Event.counter += 1


    def process(self):
        self.work(*self.args)
