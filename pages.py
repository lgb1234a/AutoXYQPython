class pageType():
    denglu = 1
    zhucheng = 2
    guaji = 3
    fengyao = 4
    disha = 5
    chenxing = 6
    yaowang = 7
    lixianshouyi = 8
    duanxianchonglian = 9
    lianjieshibai = 10
    denglushibai = 11
    juqing = 12
    dinghaodenglu = 13
    huodong = 14
    wanfa = 15

class Page(object):
    def __init__(self, flag, type, btn='') -> None:
        self.pageFlag = flag
        self.pageType = type
        self.btn = btn

pages = [
    Page('基础收益', pageType.lixianshouyi, '领取'),
    Page('断线重连', pageType.duanxianchonglian),
    Page('连接失败', pageType.lianjieshibai),
    Page('登录认证失败', pageType.denglushibai),
    Page('别处登录', pageType.dinghaodenglu),
    Page('登录', pageType.denglu),
    Page('神兽乐园', pageType.zhucheng),
    Page('自动挑战', pageType.guaji),
    Page('妖怪刷新提醒', pageType.fengyao),
    Page('积分排行', pageType.disha),
    Page('归属次数', pageType.chenxing),
    Page('驻守者', pageType.yaowang),
    Page('挑战剧情', pageType.juqing),
    Page('跳过动画', pageType.huodong),
    Page('玩法', pageType.wanfa)
]