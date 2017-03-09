#!/usr/bin/env
# -*- coding: utf-8 -*-

from Queue import Queue
import threading
from time import sleep

class ResponseHandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.buf = Queue()
        self.backCommand = ''
        self.daemon = True

    def run(self):
        while self.running:
            try:
                res = self.sock.recv(1024)
                self.buf.put(res)
            except:
                pass
            finally:
                sleep(0.2)

    def readBuf(self):
        while not self.buf.empty():
            self.backCommand += self.buf.get()
        cmdPos = self.backCommand.find('\n')
        if cmdPos >= 0:
            cmd = self.backCommand[:cmdPos].strip()
            self.backCommand = self.backCommand[cmdPos+1:]
            return cmd
        return ''

