#!/usr/bin/env
# -*- coding: utf-8 -*-

import socket
import json
from time import sleep
import Action
import NavikitConnector
from pygame import mixer

BUF_SIZE = 1024
# Address
HOST = '192.168.1.100'
PORT = 7700
with open('points.json', 'r') as f:
    points = json.load(f)

#mp3 init
mixer.init()
mixer.music.set_volume(1.0)
def play(audio):
	if not mixer.music.get_busy():
		mixer.music.load('audios/'+audio+'.mp3')
		mixer.music.play()

def hasArrived():
    status_msg = Action.GetStatusAction()
    status = kit.send_msg(status_msg.toJson())
    statusObj = json.loads(status.strip())
    print "robot status no:", statusObj["data"]["status"]
    return statusObj["data"]["status"]


#init navikit connector
kit = NavikitConnector.NavikitConnector()
for i in range(len(points)):
    posObj = Action.SetTargetPosAction(points[i]['robot_x'],  points[i]['robot_y'],
      points[i]['end_x'],  points[i]['end_y'])
    pos = posObj.toJson()

    kit.send_msg(pos)
    print "moving to point", i+1
    sleep(2)
    while hasArrived() > 0:
        sleep(1)
    print "------------ point arrived,", i+1 ," --------------"
    sleep(1)
    play('collect_dishes')
    print "stop for ",points[i]['delay'], "seconds"
    sleep(points[i]['delay'])
    