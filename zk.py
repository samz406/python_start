#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from kazoo.client import KazooClient
import logging

from kazoo.protocol.states import KazooState

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

v_path = "/my/favorite"
zk.ensure_path(v_path)


def exist(path):
    if zk.exists(path):
        print("/my/favorite exist")
    else:
        print("/my/favorite not exist")


exist(v_path)

zk.delete(v_path)

exist(v_path)


def my_listener(state):
    if state == KazooState.LOST:
        # Register somewhere that the session was lost
        print("zk lost")
    elif state == KazooState.SUSPENDED:
        # Handle being disconnected from Zookeeper
        print("zk SUSPENDED")
    else:
        # Handle being connected/reconnected to Zookeeper
        print("zk connected")


zk.add_listener(my_listener)
