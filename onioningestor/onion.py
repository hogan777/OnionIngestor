from datetime import datetime as dt

class Onion(object):
    """Onion class"""
    def __init__(self, url, source, type, status, monitor, denylist):
        self.url = url
        self.source = source
        self.type = type
        self.status = status
        self.monitor = monitor
        self.denylist = denylist
        self.datetime = dt.now()
        self.operators = {}

    def set_operator(self, response):
        self.operators.update(response)

    def asdict(self):
        d  = {
                'hiddenService':self.url,
                'source':self.source,
                'type':self.type,
                'status':self.status,
                'monitor': self.monitor,
                'denylist': self.denylist,
                'dateFound': self.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")+"Z",
                'operators': self.operators,
                }
        return d

    def __lt__(self, other):
        return self.datetime < other.datetime

    def __str__(self):
        return self.url

    def __repr__(self):
        return self.url
