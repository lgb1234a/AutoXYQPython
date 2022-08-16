from abstractEvent import AbstractEvent
import utils

class FengyaoRukouEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<封妖入口>')

    def _preCondition(self):
        return True
	
    def _do(self):
        p = utils.recg_img_and_click('TargetPic/fengyao_rukou.png')
        return bool(p)
		
    def _completionCondition(self):
        #展示封妖页
        r = utils.find_and_click_text('天降辰星', False)
        return r