from abstractEvent import AbstractEvent
import utils

class LixianshouyiEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<离线收益弹窗>')

    def _preCondition(self):
        p = utils.recg_img_and_click("TargetPic/lixianshouyi_btn.png")
        return bool(p)
	
    def _do(self):
        return True
		
    def _completionCondition(self):
        return True