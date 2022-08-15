from abstractEvent import AbstractEvent

class Yaowang130Event(AbstractEvent):
    def __init__(self):
        super().__init__(self, '<妖王130>')

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