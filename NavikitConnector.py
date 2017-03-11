#!/usr/bin/env
# -*- coding: utf-8 -*-

from time import sleep
import socket
import traceback

BUF_SIZE = 1024
# Address
HOST = '192.168.1.100'
PORT = 7700
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

class NavikitConnector():
    def __init__(self):
        self.running = True
        self._wait_connection()
        self.msg_to_send = None

    def _wait_connection(self):
        print "waiting for connction from robot ..."
        client, addr = s.accept()  # wait for connection from robot
        print "connection from ", addr
        self.sock = client

    # send message and wait for response
    def send_msg(self, msg):
        print "sending message: ", msg
        self.msg_to_send = msg

        flag = True
        while flag:
            res = self._get_response()
            if res is not None:
                print "Response :", res
                return res


    def _get_response(self):
        # if msg not None, send it
        if self.msg_to_send:
            self.sock.sendall(self.msg_to_send)
            try:
                res = self.sock.recv(BUF_SIZE)
                return res
            except:
                sleep(0.1)
        return None


    def stop(self):
        self.sock.close()
        self.running = False
