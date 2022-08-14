#!/usr/bin/env python3
import threading
import os
from multiprocessing import Process
import random
import time
import cv2
import easyocr
from ocrModel import OcrModel
from pages import pages,pageType

android_path = "/storage/emulated/0/Pictures/Screenshots"
pc_path = r"C:\Users\ZONST\Nox_share\ImageShare\Screenshots"
screen_shot_path = r'C:\Users\ZONST\Nox_share\ImageShare\Screenshots\1.png'
emulator_ip = "127.0.0.1:62001"

def launch_app():
    s = f"adb -s {emulator_ip} shell am start -W com.netease.xyh5/com.netease.xyh5.Client"
    os.system(s)

def kill_app():
    s = f"adb -s {emulator_ip} shell am force-stop com.netease.xyh5"
    os.system(s)

def screen_shot():
    s = f"adb -s {emulator_ip} shell screencap -p {android_path}/1.png"
    os.system(s)

def tap(x,y):
    s = f"adb -s {emulator_ip} shell input tap {x} {y}"
    os.system(s)
    time.sleep(1)

def swip(startX, startY, toX, toY):
    s = f"adb -s {emulator_ip} shell input swipe {startX} {startY} {toX} {toY} 50"
    os.system(s)
    time.sleep(2)

# def cv2_show(name, img):
#     cv2.imshow(name, img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


def image_to_position(screen, template):
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("     prob:", max_val)
    if max_val > 0.9:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        return center
    else:
        return False


def recg_img_and_tap(path):
    screen_shot()
    time.sleep(2)
    screen = cv2.imread(screen_shot_path)
    template =  cv2.imread(path)
    print(path)
    p = image_to_position(screen, template)
    print(p)
    if bool(p):
        tap(p[0], p[1])
    return p

def ocr():
    screen_shot()
    reader = easyocr.Reader(['ch_sim'], download_enabled=False) # ch_sim是Chinese simplified简写
    result = reader.readtext(screen_shot_path)
    return result

def find_and_click_text(text):
    result = ocr()
    for i in result:
        m = OcrModel(i)
        if m.text.find(text) != -1:
            tap(m.center[0], m.center[1])
            return True
    return False

def get_page():
    result = ocr()
    for i in result:
        m = OcrModel(i)
        print(m.text)
        for p in pages:
            if m.text.find(p.pageFlag) != -1:
                return p
    return False

if __name__ == "__main__":
    #连接adb
    # os.system("adb connect 127.0.0.1:62001")
    # screen_shot()
    print(get_page().pageType)