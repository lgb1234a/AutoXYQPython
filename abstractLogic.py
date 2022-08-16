
class AbstractLogic():
    def __init__(self, queue) -> None:
        self.events = []
        self.done = False
        self.queue = queue

    def initEvents(self):
        pass

    def priority(self):
        return 0
    
    def valid(self):
        return True

    def reset(self):
        pass

    def start(self):
        self.initEvents()
        for event in self.events:
            self.queue.put(event)

    def appendEvent(self, event):
        self.queue.put(event)