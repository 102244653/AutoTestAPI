import time


def read_local_time():
    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))