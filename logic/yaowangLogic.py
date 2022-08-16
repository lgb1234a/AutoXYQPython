from . import YaowangChallengeEvent
from abstractLogic import AbstractLogic
import time
from ocrModel import OcrModel
import utils
from events import yaowangEvent, zhuchengEvent, fengyaorukouEvent
from events.yaowangChallengeEvent import YaowangChallengeEvent

class YaowangLogic(AbstractLogic):
    def __init__(self, queue) -> None:
        super().__init__(queue)
        self.restCount = 100
        self.restTicket = 0
    
    def initEvents(self):
        self.events = [zhuchengEvent.ZhuchengEvent(), fengyaorukouEvent.FengyaoRukouEvent(), yaowangEvent.YaowangEvent()]

        if self.restCount < 9:
            for i in range(0, self.restCount):
                self.events.append(YaowangChallengeEvent(self, 130 - i*10))
        else:
            # 50~130
            for i in range(130, 40, -10):
                self.events.append(YaowangChallengeEvent(self, i))
            

    # 时间区间&&剩余次数>0
    def valid(self):
        t = time.localtime()
        if t.tm_min >= 20 and t.tm_min < 30:
            return False
        if t.tm_min >= 50:
            return False
        if self.restCount == 0:
            return False
        return True

    def updateRestCount(self):
        r = utils.ocr()
        for lineInfo in r:
            m = OcrModel(lineInfo)
            idx = m.text.find("/9")
            if idx != -1:
                self.restTicket = int(m.text[0:idx])
            idx = m.text.find("/100")
            if idx != -1:
                self.restCount = int(m.text[m.text.find("归属奖励次数：") : idx])
    
    def reset(self):
        self.restCount = 100

    def locateLevelAndChallenge(self, destLevel):
        result = utils.ocr()
        maxLevel = 0
        minLevel = 500
        gs = []
        for i in result:
            m = OcrModel(i)
            if m.text.find(f'{destLevel}级') != -1:
                utils.tap(m.center[0], m.center[1] - 30)
                utils.recg_img_and_click("TargetPic/yaowang_click.png")
                return True
            if len(m.text) < 5 and m.text.find('0级') != -1:
                level = int(m.text[0, m.text.find('0级') + 1])
                if level >= maxLevel:
                    maxLevel = level
                gs.append(level)

        for l in gs:
            if l < min and max - l < 100:
                min = l

        if destLevel < minLevel:
            #左滑
            utils.swip()
        if destLevel > maxLevel:
            utils.swip()
        return False

    def challengeFinished(self):
        r = utils.find_and_click_text("驻守者", False)
        return r

    def startYaowang(self, level):
        loops = 0
        while(not self.locateLevelAndChallenge(level)):
            loops = loops + 1
            if loops > 20:
                self.yaowangFailed(level)
                return False
        
        loops = 0
        while(not self.challengeFinished()):
            loops = loops + 1
            if loops > 20:
                self.yaowangFailed(level)
                return False

        self.yaowangDone(level)
        return True

    def yaowangDone(self, level):
        pass

    #未找到，重新加入事件队列
    def yaowangFailed(self, level):
        super().appendEvent(YaowangChallengeEvent(self, level))