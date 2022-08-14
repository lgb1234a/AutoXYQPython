from sqlite3 import Date
import threading
import os
from multiprocessing import Process
import random
import time
import cv2
from pages import pageType
import utils
import navigator

def click_zhucheng():
    utils.tap(130, 900)
    if time.localtime().tm_hour == 0:
        p = utils.recg_img_and_tap("TargetPic/new_day_next.png")
        if bool(p):
            for i in range(1,10):
                utils.tap(p[0],p[1])
        utils.recg_img_and_tap("TargetPic/new_day_close.png")
    

def skip_others():
    utils.recg_img_and_tap("TargetPic/login_btn.png")
    utils.recg_img_and_tap("TargetPic/guaji_btn.png")
    

def c_yaowang(level):
    t = time.localtime()
    if t.tm_min >= 20 and t.tm_min < 30:
        return
    if t.tm_min >= 50:
        return
    
    while(1):
        p = utils.recg_img_and_tap(f"TargetPic/yaowang_{level}.png")
        if bool(p):
            utils.recg_img_and_tap(f"TargetPic/yaowang_click.png")
            return True
        
        utils.swip(120, 177, 170, 177)
        p = utils.recg_img_and_tap("TargetPic/yaowang_130_border.png")
        if bool(p):
            if level <= 130 and level >= 90:
                utils.swip(120, 177, 170, 177)
        p = utils.recg_img_and_tap("TargetPic/yaowang_50_border.png")
        if bool(p):
            if level > 90:
                utils.swip(170, 177, 120, 177)

def yao_wang():
    navigator.navigate_to(pageType.yaowang)
    time.sleep(2)
    for i in range(50, 140, 10):
        c_yaowang(i)


if __name__ == "__main__":
    #连接adb
    # os.system("adb connect 127.0.0.1:62001")
    #启动游戏
    # utils.launch_app()
    # time.sleep(10)
    # yao_wang()
    utils.kill_app()

