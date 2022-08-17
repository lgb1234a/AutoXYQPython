import time
from abstractLogic import AbstractLogic
from events import zhuchengEvent, lilianEvent, shengsijieEvent

class ShengsijieLogic(AbstractLogic):
    def __init__(self, queue) -> None:
        super().__init__(queue)
        self.failedCount = 0

    def valid(self):
        return not self.complete

    def initEvents(self):
        self.events.append(zhuchengEvent.ZhuchengEvent(), lilianEvent.LilianEvent(), shengsijieEvent.ShengsijieEvent(self))

    def shengsijieFailed(self):
        self.failedCount = self.failedCount + 1
        if self.failedCount < 10:
            self.queue.put(shengsijieEvent.ShengsijieEvent(self))
    
    def shengsijieDone(self):
        self.complete = True