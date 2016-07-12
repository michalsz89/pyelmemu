#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import threading
import sys
import time

from debug import *
from config import bt_server_timeout

class RfcommServer(threading.Thread):
    server_status = str()
    server_errors = []
    msg_queue = []

    def __init__(self, threadID, name):
        debug_print_mtcall("RfcommServer", "__init__")
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name     = name

        self.client_sock = None
        self.serv_sock = None

        self.setDaemon(True)
        self.start()


    def run(self):
        debug_print_mtcall("RfcommServer", "run")
        self.job(self.name)

    def send(self, command):
        debug_print_mtcall("RfcommServer", "set_command")
        #self.lock.acquire(True)
        self.msg_queue.append(command)
        #self.lock.release()

    def stop(self):
        debug_print_mtcall("RfcommServer", "stop")
        #self.lock.acquire(True)
        self.msg_queue.append("exit")
        #self.lock.release()

    def close(self):
        debug_print_mtcall("RfcommServer", "close")
        if self.client_sock is not None:
            self.client_sock.close()
        if self.serv_sock is not None:
            self.serv_sock.close()

    def job(self, threadName):
        debug_print_mtcall("RfcommServer", "job")
        run = True
        currentThread = threading.currentThread()
        debug_print_log("RfCommServer",  "Server starting...")

        #Create socket and listen on any port.
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)

        self.serv_sock = server_sock

        port = server_sock.getsockname()[1]
        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        bluetooth.advertise_service(server_sock, "BTserver",
                service_id = uuid,
                service_classes = [uuid, bluetooth.SERIAL_PORT_CLASS],
                profiles = [bluetooth.SERIAL_PORT_PROFILE],)

        debug_print_log("RfCommServer", "Waiting for devices...")
        client_sock,addr = server_sock.accept()
        self.client_sock = client_sock
        debug_print_log("RfCommServer", "connected", str(addr))

        self.client_sock.settimeout(bt_server_timeout)
        #Data reading loop
        while run:
            try:
                cmd = str()
                if len(currentThread.msg_queue) > 0:
                    debug_print_log("SENDING")
                    cmd = currentThread.msg_queue[0];
                    del currentThread.msg_queue[0]
                    cmd = cmd + '\r'
                    client_sock.send(cmd)

                data = client_sock.recv(1024)
                if len(data) > 0:
                    debug_print_log("data received")

            except IOError:
                pass

        debug_print_log("RfCommServer", "Disconnecting...")
        client_sock.close()
        server_sock.close()
        debug_print_log("RfcommServer", "Finished...")
