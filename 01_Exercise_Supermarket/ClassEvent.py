# class consists of instance variables:
# t: time stamp
# work: job to be done
# args: list of arguments for job to be done
# prio: used to give leaving, being served, and arrival different priorities
class Event:
    counter = 0

    def __init__(self, t, work, args=(), prio=255):
        self.t = t
        self.n = Event.counter
        self.work = work
        self.args = args
        self.prio = prio
        Event.counter += 1
