#!/usr/bin/python
# -*- coding: UTF-8 -*-


import thread
import time


def print_time(t, d):
    count = 0
    while count < 10:
        time.sleep(d)
        count = count + 1
        print "%s:%s" % (t, time.ctime(time.time()))


try:
    thread.start_new_thread(print_time("thead-1", 2))
    thread.start_new_thread(print_time("thread-2", 4))
except:
    print "Error:unable to start thread"
