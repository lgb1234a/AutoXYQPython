from ctypes import util
from abstractEvent import AbstractEvent
from ocrModel import OcrModel
import utils

class Yaowang130Event(AbstractEvent):
    def __init__(self, observer):
        super().__init__('<妖王130>')
        self.observer = observer
        self.ocrResult = []

    def _preCondition(self):
        self.ocrResult = utils.ocr()
        restTicket = 0
        restCount = 100
        for lineInfo in self.ocrResult:
            m = OcrModel(lineInfo)
            idx = m.text.find("/9")
            if idx != -1:
                restTicket = m.text[0:idx]
            idx = m.text.find("/100")
            if idx != -1:
                restCount = m.text[m.text.find("归属奖励次数：") : idx]
        self.observer.updateRestCount(restCount, restTicket)
        return True
	
    def _do(self):
        self.observer.findYaowang(130)
        return True
		
    def _completionCondition(self):
        self.observer.yaowangDone(130)
        return True