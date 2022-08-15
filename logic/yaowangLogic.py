from abstractLogic import AbstractLogic
import zhuchengEvent, fengyaorukouEvent, fengyaoEvent, yaowangEvent, yaowang50Event, yaowang60Event, yaowang70Event, yaowang80Event, yaowang90Event, yaowang100Event, yaowang110Event, yaowang120Event, yaowang130Event

class YaowangLogic(AbstractLogic):
    def __init__(self, queue) -> None:
        super().__init__(self, queue)
        self.restCount = 0
        self.restTicket = 0
    
    def initEvents(self):
        self.events = [zhuchengEvent.ZhuchengEvent(), fengyaorukouEvent.FengyaoRukouEvent(), yaowangEvent.YaowangEvent(), yaowang130Event.Yaowang130Event(), yaowang120Event.Yaowang120Event(), yaowang110Event.Yaowang110Event(), yaowang100Event.Yaowang100Event(), yaowang90Event.Yaowang90Event(), yaowang80Event.Yaowang80Event(), yaowang70Event.Yaowang70Event(), yaowang60Event.Yaowang60Event(), yaowang50Event.Yaowang50Event()]


    