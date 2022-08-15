from abstractEvent import AbstractEvent

class Yaowang110Event(AbstractEvent):
    def __init__(self, observer):
        super().__init__(self, '<妖王110>')
        self.observer = observer

    def preCondition(self):
		# print('当前不在登录页')
		# super().preConditionFailed()
        print('当前在登录页')
        return True
	
    def do(self):
		# print('找不到登录按钮')
		# super().doFailed()
        print('点击了登录按钮')
        return True
		
    def completionCondition(self):
		# print('当前不在离线收益页')
		# super().completionConditionFailed()
        print('当前在离线收益页')
        return True