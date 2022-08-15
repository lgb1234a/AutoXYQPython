import time
import threading
class AbstractEvent():
	def __init__(self, name):
		self.name = name
	
	def logger(self):
		print(time.localtime()+':'+self.name)
		
	def preCondition(self):
		return False
	
	def do(self):
		return False
	
	def completionCondition(self):
		return False
	
	def preConditionFailed(self):
		#前置条件不满足
		#大退重进
		print('大退重进')
		
	def doFailed(self):
		#执行出错
		#将事件重新入栈
		print('将事件重新入栈')
		
	def completionConditionFailed(self):
		#前置条件不满足
		#大退重进
		print('大退重进')