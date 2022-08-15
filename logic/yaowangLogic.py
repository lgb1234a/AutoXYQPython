from abstractLogic import AbstractLogic
import time
import zhuchengEvent, fengyaorukouEvent, fengyaoEvent, yaowangEvent, yaowang50Event, yaowang60Event, yaowang70Event, yaowang80Event, yaowang90Event, yaowang100Event, yaowang110Event, yaowang120Event, yaowang130Event

class YaowangLogic(AbstractLogic):
    def __init__(self, queue) -> None:
        super().__init__(self, queue)
        self.restCount = 100
        self.restTicket = 0
    
    def initEvents(self):
        self.events = [zhuchengEvent.ZhuchengEvent(), fengyaorukouEvent.FengyaoRukouEvent(), yaowangEvent.YaowangEvent(), yaowang130Event.Yaowang130Event(self), yaowang120Event.Yaowang120Event(self), yaowang110Event.Yaowang110Event(self), yaowang100Event.Yaowang100Event(self), yaowang90Event.Yaowang90Event(self), yaowang80Event.Yaowang80Event(self), yaowang70Event.Yaowang70Event(self), yaowang60Event.Yaowang60Event(self), yaowang50Event.Yaowang50Event(self)]
            

    # 时间区间&&剩余次数>0
    def valid(self):
        t = time.localtime()
        if t.tm_min >= 20 and t.tm_min < 30:
            return False
        if t.tm_min >= 50:
            return False
        if self.restCount == 0:
            return False

    def updateRestCount(self, count, tickets):
        self.restCount = count
        self.restTicket = tickets
    
    def reset(self):
        self.restCount = 100