
class AbstractLogic():
    def __init__(self, queue) -> None:
        self.events = []
        self.done = False
        self.queue = queue
        self.initEvents()

    def initEvents(self):
        pass

    def priority(self):
        return 0
    
    def valid(self):
        return True

    def reset(self):
        pass

    def start(self):
        for event in self.events:
            self.queue.put(event)