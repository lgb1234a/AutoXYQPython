import datetime
class AbstractEvent():
    def __init__(self, name) -> None:
        self.name = name
    
    def preCondition(self):
       return False
	
    def do(self):
       return False
	
    def completionCondition(self):
       return False

    
    def logger(self, msg):
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f'{d}:{self.name} {msg}'
        with open('log.txt', 'a') as f:
            f.write(log)

		
	