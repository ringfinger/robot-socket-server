#!/usr/bin/env
# -*- coding: utf-8 -*-

import socket
import json
from time import sleep

BUF_SIZE = 1024
# Address
HOST = '192.168.1.58'
PORT = 7700

pos = '''{
  "Action": {
              "CallBackFunction" : {
                                     "name" : "setTargetPos",
                                     "data" : {
                        "robot_x": -8.5,
                        "robot_y": 2.0,
                        "end_x"  : -2.0,
                        "end_y"  : -1.0
                          }
                                   }
             }
}
'''
# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
# 1: maximum number of requests waiting
s.listen(1)
client, addr = s.accept()  #wait for connection from robot

client.sendall(pos)