from sqlite3 import Date
import threading
import os
from multiprocessing import Process
import random
import time
import cv2
from pytz import HOUR
from pages import pageType
import utils
from level import LevelModel
from apscheduler.schedulers.blocking import BlockingScheduler
from triggerManager import TriggerManager
from queue import Queue
from events.loginEvent import LoginEvent
from events.pendingEvent import PendingEvent
from events.lixianshouyiEvent import LixianshouyiEvent
from logic.yaowangLogic import YaowangLogic

eventQueue = Queue()
yl = YaowangLogic(eventQueue)
logics = [yl]
day = time.localtime().tm_mday

def resetLogics():
    for logic in logics:
        logic.reset()


def restartApp():
    utils.kill_app()
    time.sleep(5)
    if not utils.is_app_running():
        utils.launch_app()
        time.sleep(10)

    eventQueue.queue.clear()
    eventQueue.put(LoginEvent())
    eventQueue.put(PendingEvent(5))
    eventQueue.put(LixianshouyiEvent())


def start():
    if eventQueue.qsize() == 0:
        for logic in logics:
            if logic.valid():
                logic.start()
    else:
        event = eventQueue.get(True)
        if not event.preCondition():
            restartApp()
        if not event.do():
            #Todo:
            eventQueue.put(event)
        if not event.completionCondition():
            restartApp()
    d = time.localtime().tm_mday
    if day != d:
        resetLogics()
    day = d


#540x960分辨率
if __name__ == "__main__":
    #连接adb
    os.system("adb connect 127.0.0.1:62001")
    #启动游戏
    if not utils.is_app_running():
        utils.launch_app()
        time.sleep(10)
        eventQueue.put(LoginEvent())
        eventQueue.put(PendingEvent(5))
        eventQueue.put(LixianshouyiEvent())


    scheduler = BlockingScheduler()
    trigger = TriggerManager.interval_trigger(conf={"timeInterval": 1, "timeUnit": 's'})
    scheduler.add_job(start, trigger)
    scheduler.start()
