from abstractEvent import AbstractEvent
import utils

class LixianshouyiEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<离线收益弹窗>')

    def preCondition(self):
        p = utils.recg_img_and_tap("TargetPic/lixianshouyi_btn.png")
        return bool(p)
	
    def do(self):
        return True
		
    def completionCondition(self):
        return True