# -*- coding: utf-8 -*-
# @Time    : 2017/11/19 23:04
# @Author  : play4fun
# @File    : assistant_deom1.py
# @Software: PyCharm

"""
assistant_deom1.py:
"""
import logging

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

def main():

    def on_button_press(_):
        assistant.start_converstation()

    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()

    button.on_press(on_button_press)

    for event in assistant.start():
        process_event(event)





if __name__ == '__main__':
    main()

