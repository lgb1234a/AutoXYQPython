
from asyncore import loop
from os import kill
from time import sleep
from pages import pages, pageType
from utils import get_page,tap,find_and_click_text,kill_app,launch_app,recg_img_and_tap

def navigate_to(destPageType):
    loopCount = 0
    crtPageType = False
    while(crtPageType != destPageType):
        p = get_page()
        if bool(p):
            crtPageType = p.pageType
            print(crtPageType)
            if crtPageType == destPageType:
                break

            elif crtPageType == pageType.denglu:
                tap(268,610)
                sleep(5)
                break

            elif crtPageType == pageType.zhucheng:
                if destPageType == pageType.wanfa or destPageType == pageType.guaji:
                    tap(38, 900)
                elif destPageType == pageType.yaowang or destPageType == pageType.chenxing:
                    recg_img_and_tap('TargetPic/fengyao_rukou.png')
                break

            elif crtPageType == pageType.guaji:
                if destPageType == pageType.wanfa or destPageType == pageType.guaji:
                    tap(30, 387)
                else:
                    tap(130, 900)
                break

            elif crtPageType == pageType.fengyao:
                if destPageType == pageType.chenxing:
                    find_and_click_text("天降辰星")
                if destPageType == pageType.yaowang:
                    find_and_click_text("封印妖王")
                break

            elif crtPageType == pageType.disha:
                if destPageType != pageType.disha:
                    tap(130, 900)
                break

            elif crtPageType == pageType.chenxing:
                if destPageType != pageType.chenxing:
                    tap(130, 900)
                break

            elif crtPageType == pageType.yaowang:
                if destPageType != pageType.yaowang:
                    tap(130, 900)
                break

            elif crtPageType == pageType.lixianshouyi:
                tap(367,605)
                break
            
            elif crtPageType == pageType.duanxianchonglian or crtPageType == pageType.dinghaodenglu:
                sleep(600)
            
            elif crtPageType == pageType.lianjieshibai or crtPageType == pageType.denglushibai:
                return

            elif crtPageType == pageType.huodong:
                tap(510, 912)
                break

            else:
                tap(130, 900)
                break

        loopCount = loopCount + 1
        if loopCount > 10:
            loopCount = 0
            kill_app()
            sleep(5)
            launch_app()
            sleep(5)