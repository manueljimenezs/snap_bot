#!/usr/bin/python2.7

import datetime
import telepot
import time
import requests
import os
import glob
import cv2
from telepot.loop import MessageLoop

TOKEN = 'TOKEN:TOKEN'
def webcontrol(chat_id, type, cmd):
    req = 'http://localhost:8080/0/'+type+'/'+cmd
    res = requests.get(req)
    bot.sendMessage(chat_id, res.text )

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #FIXME does not work
    #if chat_id != 00000008:
    #    bot.sendMessage(chat_id, "Sorry this is a personal bot. Access Denied!")
    #    continue

    print 'Got command: %s' % command

    if command == '/snapshot':
        requests.get('http://localhost:8080/0/action/snapshot')
    elif command == '/snap':
        cap = cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        ret, img = cap.read() # lectura de un frame de video
        #img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cv2.imwrite('a.jpg', img)
        bot.sendPhoto(4192650, photo=open('a.jpg','rb'), caption='Nueva captura')

    else:
        bot.sendMessage(chat_id, "Unknown Command "+command)
        
bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()


print 'I am listening ...'


while 1:
    time.sleep(10)
