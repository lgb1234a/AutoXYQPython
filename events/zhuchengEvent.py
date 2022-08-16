from abstractEvent import AbstractEvent
import utils

class ZhuchengEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<主城>')

    def _preCondition(self):
        utils.tap()
        return True
	
    def _do(self):
        utils.tap()
        return True
		
    def _completionCondition(self):
        p = utils.recg_img_and_click('TargetPic/fengyao_rukou.png', False)
        return bool(p)