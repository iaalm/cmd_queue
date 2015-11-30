#!/usr/bin/python3 

import zmq

def send_task(endpoint,cmd):
    ct = zmq.Context()
    socket = ct.socket(zmq.REQ)
    socket.connect(endpoint)
    socket.send_unicode(cmd)
    return socket.recv_unicode()

if __name__ == '__main__':
    print(send_task('tcp://localhost:5050','ls'))
