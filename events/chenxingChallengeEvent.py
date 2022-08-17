from ocrModel import OcrModel
import utils
from abstractEvent import AbstractEvent

class ChenxingChallengeEvent(AbstractEvent):
    def __init__(self, observer, level):
        super().__init__('<辰星{level}>')
        self.observer = observer
        self.level = level

    def _preCondition(self):
        # self.observer.updateRestCount()
        return True

    # 点击按钮+跳过
    def challengeFinished(self):
        pass

    def locateLevelAndChallenge(self, destLevel):
        result = utils.ocr()
        maxLevel = 0
        minLevel = 500
        gs = []
        for i in result:
            m = OcrModel(i)
            if m.text.find(f'{destLevel}级') == 0:
                utils.tap(m.center[0], m.center[1] - 30)
                # utils.recg_img_and_click("TargetPic/yaowang_click.png")
                return True
            if len(m.text) < 5 and m.text.find('0级') != -1:
                endIdx = m.text.find('0级') + 1
                _l = m.text[0: endIdx]
                level = int(_l)
                if level >= maxLevel:
                    maxLevel = level
                gs.append(level)

        for l in gs:
            if l < minLevel and maxLevel - l < 100:
                minLevel = l

        if destLevel < minLevel:
            #左滑
            utils.swip(100, 180, 200, 180)
        if destLevel > maxLevel:
            utils.swip(200, 180, 100, 180)
        return False
	
    def startChenxing(self, level):
        loops = 0
        while(not self.locateLevelAndChallenge(level)):
            loops = loops + 1
            if loops > 20:
                self.observer.chenxingFailed(level)
                return False
        
        loops = 0
        while(not self.challengeFinished()):
            loops = loops + 1
            if loops > 20:
                self.observer.chenxingFailed(level)
                return False

        self.observer.chenxingDone()
        return True


    def _do(self):
        self.startChenxing(self.level)
        return True
		
    def _completionCondition(self):
        return True