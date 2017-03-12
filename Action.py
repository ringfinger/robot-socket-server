#!/usr/bin/env
# -*- coding: utf-8 -*-

import json

class Action():
    def __init__(self, name):
        self._name = name

    def toJson(self):
        return json.dumps({
            "Action": {
                "CallBackFunction":{
                    "name": self._name
                }
            }
        })

    # @staticmethod
    # def getObjectFromJson(jsonObj):
    #     try:
    #         obj = json.loads(jsonObj)
    #         action = Action(obj["Action"]["CallBackFunction"]["name"], obj["Action"]["CallBackFunction"]["data"])
    #         return action
    #     except e:
    #         print e
    #         raise
class GetStatusAction(Action):
    def __init__(self):
        Action.__init__(self, "getStatus")

class GetRobotPosAction(Action):
    def __init__(self):
        Action.__init__(self, "getRobotPos")

class SetTargetPosAction(Action):
    def __init__(self, robot_x, robot_y, end_x, end_y):
        Action.__init__(self, "setTargetPos") 
        self.data = {
            "robot_x": robot_x,
            "robot_y": robot_y,
            "end_x"  : end_x,
            "end_y"  : end_y
                }

    def toJson(self):
        return json.dumps({
            "Action": {
                "CallBackFunction":{
                    "name": self._name,
                    "data": self.data
                }
            }
        })

if __name__ == "__main__":
    getpos = GetRobotPosAction()
    print getpos.toJson()