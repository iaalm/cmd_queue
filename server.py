#!/usr/bin/python3 

import zmq
import os

def start_server(port):
    ct = zmq.Context()
    socket = ct.socket(zmq.PULL)
    socket.bind("tcp://*:%d"%port)
    while True:
        msg = socket.recv_unicode()
        print('cmd: '+msg)
        os.system(msg)


if __name__ == '__main__':
    start_server(5050)
