import datetime
import utils
class AbstractEvent():
    def __init__(self, name) -> None:
        self.name = name
    
    def preCondition(self):
        self.logger("-------开始-------")
        r = self._preCondition()
        return r
	
    def do(self):
        r = self._do()
        return r
	
    def completionCondition(self):
        r = self._completionCondition()
        if not r:
            self.logger("  执行结果不匹配")
            d = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            utils.screen_shot(f'{utils.android_path}/debug/{d}.png')
        else:
            self.logger("       完成")
        return True

    
    def logger(self, msg):
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f'{d}:{self.name} {msg}\n'
        with open('log.txt', 'a') as f:
            f.write(log)


# ab = AbstractEvent('<测试>')
# ab.logger("-------开始-------")
# ab.logger("  执行结果不匹配")
# ab.logger("       完成")

		
	