from abstractEvent import AbstractEvent
import utils

class LoginEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<登录>')

    def _preCondition(self):
        p = utils.recg_img_and_click("TargetPic/login_btn.png")
        return bool(p)
	
    def _do(self):
        return True
		
    def _completionCondition(self):
        return True