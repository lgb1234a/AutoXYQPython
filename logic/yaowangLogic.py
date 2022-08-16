from abstractLogic import AbstractLogic
import time
from events import yaowangEvent, zhuchengEvent, fengyaorukouEvent, fengyaoEvent
from events.yaowang import yaowang50Event, yaowang60Event, yaowang70Event, yaowang80Event, yaowang90Event, yaowang100Event, yaowang110Event, yaowang120Event, yaowang130Event

class YaowangLogic(AbstractLogic):
    def __init__(self, queue) -> None:
        super().__init__(queue)
        self.restCount = 100
        self.restTicket = 0
        self.undoLevels = []
        self.levelMapEvent = {
            130:yaowang130Event.Yaowang130Event(self),
            120:yaowang120Event.Yaowang120Event(self),
            110:yaowang110Event.Yaowang110Event(self),
            100:yaowang100Event.Yaowang100Event(self),
            90:yaowang90Event.Yaowang90Event(self),
            80:yaowang80Event.Yaowang80Event(self),
            70:yaowang70Event.Yaowang70Event(self),
            60:yaowang60Event.Yaowang60Event(self),
            50:yaowang50Event.Yaowang50Event(self)
        }
    
    def initEvents(self):
        self.events = [zhuchengEvent.ZhuchengEvent(), fengyaorukouEvent.FengyaoRukouEvent(), yaowangEvent.YaowangEvent()]

        self.undoLevels = []
        if self.restCount < 9:
            for i in range(0, self.restCount):
                self.undoLevels.append(130 - i*10)
        else:
            self.undoLevels = [130, 120, 110, 100, 90, 80, 70, 60, 50]
        for level in self.undoLevels:
            self.events.append(self.levelMapEvent[level])
            

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

    def updateRestCount(self, count, tickets):
        self.restCount = count
        self.restTicket = tickets
    
    def reset(self):
        self.restCount = 100

    def findYaowang(self, level):
        pass

    def yaowangDone(self, level):
        self.undoLevels.remove(level)

    #未找到，重新加入事件队列
    def yaowangFailed(self, level):
        super().appendEvent(self.levelMapEvent[level])