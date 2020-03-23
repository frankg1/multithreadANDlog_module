#-*- coding: utf-8 -*-
from log import Log

from multiprocessing import cpu_count
from concurrent import futures

'''
author：from ljx  my bro, fixed by gaoxiang02
1 这个模块具有两种使用方式，
    1.1 作为class的全局变量，每个线程去调用之
    1.2 作为每个线程之中的局部变量（推荐使用，这样可以识别线程）
2 参数介绍
    2.1 默认参数，线程标识Log('线程参数')
'''

class Obj():
    # log=Log('这是什么意思？')   #传进去的这段文字  输出日志的时候，告诉你是哪个线程用的
    def __init__(self):
        pass
    def test(self,thread_index):
        log=Log(str(thread_index)+" thread")
        log.debug(str(thread_index)+' is debuging !')
        log.debug(str(thread_index)+' is erroring !')
    def run(self):
        lis=[i for i in range(20)]
        with  futures.ThreadPoolExecutor(max_workers=int(20)) as excutor:
              excutor.map(self.test,lis )



def run():
    obj=Obj()
    obj.run()
    pass

if __name__=="__main__":
    run()
    pass