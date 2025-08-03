#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import time
import logging
import traceback
import psutil #Specs Monitor Thing
import datetime 
import subprocess
import socket


picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V4
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)
logging.info("Started successfully") #log info      

try:

    epd = epd2in13_V4.EPD()
    logging.info("init and Clear") #log info
    epd.init()
    epd.Clear(0xFF)

    #font15 = ImageFont.load_default()
    font15 = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 15)

    while True:

        epd.init()
        image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(image)

        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

        cpu_percent = psutil.cpu_percent(interval=1) #CPU Text
        cpu_text = f"CPU: {cpu_percent:.1f}%"

        cpu_freq = psutil.cpu_freq() #CPU Freq
        freq_text = f"Freq: {cpu_freq.current:.0f} MHz"

        mem = psutil.virtual_memory() #RAM Text
        ram_text = f"RAM: {mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB ({mem.percent:.1f}%)"

        users = psutil.users() #Users
        user_text = f"Users: {len(users)}"

        addrs = psutil.net_if_addrs()
        ip_wlan0 = None
        if 'wlan0' in addrs:
            for snic in addrs['wlan0']:
                if snic.family == socket.AF_INET:  # IPv4 address
                    ip_wlan0 = snic.address
                    break

        ip_text = f"IP: {ip_wlan0}" if ip_wlan0 else "IP: Not connected"


        draw.text((0, 0), u'no', font = font15, fill = 0) # draw text
        draw.text((0, 12), cpu_text, font=font15, fill=0) # draw text
        draw.text((0, 24), current_time, font=font15, fill=0) # show time 
        draw.text((0, 36), freq_text, font=font15, fill=0)    # cpu freq its alright 
        draw.text((0, 48), ram_text, font=font15, fill=0)   # ram display its mehhh 
        draw.text((0, 60), user_text, font=font15, fill=0) # useless and broken user display text
        draw.text((0, 72), ip_text, font=font15, fill=0)        # WiFi IP address



        epd.display(epd.getbuffer(image))
        logging.info("Sleep 5s") #log info
        time.sleep(5)

except KeyboardInterrupt:
    logging.info("Clearing")
    epd.Clear(0xFF)
    logging.info("Interrupted by user, shutting down...")
    epd.sleep()

