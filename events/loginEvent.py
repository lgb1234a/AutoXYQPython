from abstractEvent import AbstractEvent
import utils

class LoginEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<登录>')

    def preCondition(self):
        p = utils.recg_img_and_tap("TargetPic/login_btn.png")
        return bool(p)
	
    def do(self):
        return True
		
    def completionCondition(self):
        return True