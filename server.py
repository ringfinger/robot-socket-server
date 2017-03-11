#!/usr/bin/env
# -*- coding: utf-8 -*-

import socket
import json
from time import sleep
import Action
import NavikitConnector

BUF_SIZE = 1024
# Address
HOST = '192.168.1.100'
PORT = 7700
with open('points.json', 'r') as f:
    points = json.load(f)

#init navikit connector
kit = NavikitConnector.NavikitConnector()
for i in range(len(points)):
    posObj = Action.SetTargetPosAction(points[i]['robot_x'],  points[i]['robot_y'],
      points[i]['end_x'],  points[i]['end_y'])
    pos = posObj.toJson()

    kit.send_msg(pos)
    sleep(20)
# # Configure socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# # 1: maximum number of requests waiting
# s.listen(1)
# client, addr = s.accept()  #wait for connection from robot
# sleep(1)
# print "Sending target Pos ..."
# client.sendall(pos)