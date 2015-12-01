#!/usr/bin/python3 

import zmq
import os
import sys
import re

def send_task(endpoint,cmd):
    ct = zmq.Context()
    socket = ct.socket(zmq.PUSH)
    socket.connect(endpoint)
    socket.send_unicode(cmd)

if __name__ == '__main__':
    msg = sys.argv if len(sys.argv) > 1 else ['dummy','auto']
    msg.pop(0)
    msg = ' '.join(msg)
    os.system("svn up ~/ComputerVision-2.0")
    print("svn ci ~/ComputerVision-2.0 -m '%s'" % msg)
    output = os.popen("svn ci ~/ComputerVision-2.0 -m '%s'" % msg).read()
    print(output)
    reversion = re.search('revision (\d*)',output).groups(1)[0]
    print(reversion)
    send_task('tcp://192.168.1.101:5050','~/xks/bin/ir-oxford -m 25 -r %s' % reversion)
