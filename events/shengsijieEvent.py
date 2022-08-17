from abstractEvent import AbstractEvent
import utils

class ShengsijieEvent(AbstractEvent):
    def __init__(self, observer):
        super().__init__('<生死劫>')
        self.observer = observer

    def _preCondition(self):
        # find shengsijie
        return True
	
    def _do(self):
        p = utils.recg_img_and_click('TargetPic/.png')
        return bool(p)
		
    def _completionCondition(self):
        p = utils.recg_img_and_click('TargetPic/.png', False)
        if not bool(p):
            self.observer.shengsijieFailed()
        else:
            self.observer.shengsijieDone()
        return True