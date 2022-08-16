import datetime
class AbstractEvent():
    def __init__(self, name) -> None:
        self.name = name
    
    def preCondition(self):
        r = self._preCondition()
        return r
	
    def do(self):
        r = self._do()
        return r
	
    def completionCondition(self):
        r = self._completionCondition()
        if not r:
            self.logger("执行结果不匹配")
        return r

    
    def logger(self, msg):
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f'{d}:{self.name} {msg}'
        with open('log.txt', 'a') as f:
            f.write(log)

		
	