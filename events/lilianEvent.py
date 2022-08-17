from abstractEvent import AbstractEvent
import utils

class LilianEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<历练入口>')

    def _preCondition(self):
        return True
	
    def _do(self):
        p = utils.recg_img_and_click('TargetPic/.png')
        return bool(p)
		
    def _completionCondition(self):
        r = utils.find_and_click_text('决战华山', False)
        return r