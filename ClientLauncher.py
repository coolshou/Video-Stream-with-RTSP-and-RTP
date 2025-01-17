#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Tibbers'
import sys
if sys.version_info[0] < 3:
    from Tkinter import Tk
else:
    from tkinter import Tk
from Client import Client

if __name__ == "__main__":
    try:
        serverAddr = sys.argv[1]
        serverPort = sys.argv[2]
        rtpPort = sys.argv[3]
        fileName = sys.argv[4]
    except:
        print("[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file]")
        print("  eg: ClientLauncher.py 192.168.70.147 10250 5008 video.mjpeg")
        sys.exit()

    root = Tk()

    # Create a new client
    #app = Client(root, serverAddr, serverPort, rtpPort, fileName)
    app = Client(root,serverAddr,serverPort,rtpPort,fileName)
    app.master.title("RTPClient")
    root.mainloop()

