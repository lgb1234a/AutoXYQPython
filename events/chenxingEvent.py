from abstractEvent import AbstractEvent

class ChenxingEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<天降辰星>')

    def _preCondition(self):
        return True
	
    def _do(self):
        return True
		
    def _completionCondition(self):
        return True