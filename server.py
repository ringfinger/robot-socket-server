#!/usr/bin/env
# -*- coding: utf-8 -*-

import socket
import json
from time import sleep
import Action

BUF_SIZE = 1024
# Address
HOST = '192.168.1.100'
PORT = 7700

posObj = Action.SetTargetPosAction("setTargetPos", 5.8, -2.08, -2.0, -1.0)
pos = posObj.toJson()
print pos

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
# 1: maximum number of requests waiting
s.listen(1)
client, addr = s.accept()  #wait for connection from robot
sleep(1)
print "Sending target Pos ..."
client.sendall(pos)