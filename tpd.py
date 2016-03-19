#!/usr/bin/python3 

import zmq
import os
import multiprocessing 

def worker(cmd):
    print('start',cmd)
    os.system(cmd)
    print('finish',cmd)

def start_server(port,n_processes=4):
    pool = multiprocessing.Pool(processes=n_processes)
    ct = zmq.Context()
    socket = ct.socket(zmq.PULL)
    socket.bind("tcp://*:%d"%port)
    while True:
        msg = socket.recv_unicode()
        print('cmd: '+msg)
        pool.apply_async(worker, (msg,))


if __name__ == '__main__':
    start_server(5050)
