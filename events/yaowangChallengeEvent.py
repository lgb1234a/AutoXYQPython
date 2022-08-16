from abstractEvent import AbstractEvent

class YaowangChallengeEvent(AbstractEvent):
    def __init__(self, observer, level):
        super().__init__('<妖王{level}>')
        self.observer = observer
        self.level = level

    def _preCondition(self):
        return True
	
    def _do(self):
        r = self.observer.startYaowang(self.level)
        return True
		
    def _completionCondition(self):
        return True