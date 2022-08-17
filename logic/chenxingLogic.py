import time
from abstractLogic import AbstractLogic
from events import chenxingEvent, zhuchengEvent, fengyaorukouEvent
from events.chenxingChallengeEvent import ChenxingChallengeEvent
from ocrModel import OcrModel
import utils

class ChenxingLogic(AbstractLogic):
    def __init__(self, queue) -> None:
        super().__init__(queue)
        self.restCount = 5
    
    def initEvents(self):
        atChenxingPage = False
        r = utils.ocr()
        for lineInfo in r:
            m = OcrModel(lineInfo)
            idx = m.text.find("辰星商店")
            if idx != -1:
                atChenxingPage = True
        
        if not atChenxingPage:
            self.events = [zhuchengEvent.ZhuchengEvent(), fengyaorukouEvent.FengyaoRukouEvent(), chenxingEvent.ChenxingEvent()]

        self.events.append(ChenxingChallengeEvent(self, 240), ChenxingChallengeEvent(self, 230), ChenxingChallengeEvent(self, 220), ChenxingChallengeEvent(self, 215))

    # 时间区间&&剩余次数>0
    def valid(self):
        t = time.localtime()
        if t.tm_hour >= 2 and t.tm_hour < 8:
            return False
        if self.restCount == 0:
            return False
        return True

    def updateRestCount(self):
        r = utils.ocr()
        for lineInfo in r:
            m = OcrModel(lineInfo)
            idx = m.text.find("/5")
            if idx != -1:
                self.restCount = int(m.text[0:idx])
    
    def reset(self):
        self.restCount = 5

    
    def chenxingFailed(self):
        pass

    def chenxingDone(self):
        self.updateRestCount()