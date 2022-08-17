from abstractEvent import AbstractEvent
import utils

class ShengsijieEvent(AbstractEvent):
    def __init__(self, observer):
        super().__init__('<生死劫>')
        self.observer = observer

    def findChenxing(self):
        r = utils.find_and_click_text('生死劫')
        return bool(r)

    def _preCondition(self):
        loops = 0
        while(not self.findChenxing()):
            utils.swip(100, 815, 330, 815)
            loops = loops + 1
            if loops > 5:
                break
        return True
	
    def _do(self):
        p = utils.recg_img_and_click('TargetPic/shengsijie_start.png')
        return bool(p)
		
    def _completionCondition(self):
        p = utils.recg_img_and_click('TargetPic/shengsijie_complete.png', False)
        if not bool(p):
            self.observer.shengsijieFailed()
            return False
        else:
            self.observer.shengsijieDone()
            return True