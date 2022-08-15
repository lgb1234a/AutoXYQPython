from time import sleep
from abstractEvent import AbstractEvent
import utils

class PendingEvent(AbstractEvent):
    def __init__(self, interval):
        super().__init__(f'<暂停{interval}s>')
        self.interval = interval

    def preCondition(self):
        return True
	
    def do(self):
        sleep(self.interval)
        return True
		
    def completionCondition(self):
        return True