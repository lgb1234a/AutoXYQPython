from abstractEvent import AbstractEvent

class FengyaoEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<封妖>')

    def _preCondition(self):
        return True
	
    def _do(self):
        return True
		
    def _completionCondition(self):
        return True