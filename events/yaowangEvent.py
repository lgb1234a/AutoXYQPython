from ctypes import util
from abstractEvent import AbstractEvent
import utils

class YaowangEvent(AbstractEvent):
    def __init__(self):
        super().__init__('<封印妖王>')

    def _preCondition(self):
        return True
	
    def _do(self):
        utils.find_and_click_text("封印妖王")
        return True
		
    def _completionCondition(self):
        r = utils.find_and_click_text("剩余获取归属", False)
        return r