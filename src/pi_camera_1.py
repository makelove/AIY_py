# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 16:30
# @Author  : play4fun
# @File    : pi_camera_1.py
# @Software: PyCharm

"""
pi_camera_1.py:
https://www.youtube.com/watch?v=aV5bhkB8NWM
"""

from picamera import PiCamera

camera = PiCamera()
brightlevel = 50

if text == 'brighter':
    brightlevel = brightlevel + 10
    camera.brightness = brightlevel

elif text == 'dimmer':
    brightlevel = brightlevel - 10
    camera.brightness = brightlevel

elif text == 'preview':
    camera.start_preview()

elif text == 'capture':
    camera.capture('image.jpg')
    camera.stop_preview()
    print('picture taken')
    os.system('gpicview image.jpg')
