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
import loginEvent
from yaowangLogic import YaowangLogic

eventQueue = Queue()
logics = [YaowangLogic(eventQueue)]
day = time.localtime().tm_mday

def refreshLogics():
    for logic in logics:
        logic.reset()


def restartApp():
    utils.kill_app()
    time.sleep(5)
    if not utils.is_app_running():
        utils.launch_app()
        time.sleep(10)
    eventQueue.put(loginEvent())


def start():
    if eventQueue.empty:
        for logic in logics:
            if logic.valid():
                logic.start()
    else:
        event = eventQueue.get(False)
        if not event.preCondition():
            restartApp()
        if not event.do():
            eventQueue.put(event)
        if not event.completionCondition():
            restartApp()

    if day != time.localtime().tm_mday:
        refreshLogics()
    day = time.localtime().tm_mday



if __name__ == "__main__":
    #连接adb
    os.system("adb connect 127.0.0.1:62001")
    #启动游戏
    if not utils.is_app_running():
        utils.launch_app()
        time.sleep(10)

    eventQueue.put(loginEvent.LoginEvent())
    scheduler = BlockingScheduler()
    trigger = TriggerManager.interval_trigger(conf={"timeInterval": 1, "timeUnit": 's'})
    scheduler.add_job(start, trigger)
    scheduler.start()
