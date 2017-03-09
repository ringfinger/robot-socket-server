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

class GetRobotPosAction(Action):
    def __init__(self, name):
        Action.__init__(self, name)

class SetTargetPosAction(Action):
    def __init__(self, name, robot_x, robot_y, end_x, end_y):
        Action.__init__(self, name) 
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
