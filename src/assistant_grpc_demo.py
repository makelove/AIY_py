#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google Assistant GRPC recognizer."""

import os

#不生效
# os.environ['http_proxy'] = 'http://192.168.0.159:50493'
# os.environ['https_proxy'] = 'http://192.168.0.159:50493'
# alias xy="export http_proxy='http://192.168.0.159:50493';export https_proxy='http://192.168.0.159:50493'"

import logging

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import subprocess

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()

    def on_button_press(_):
        assistant.start_converstation()

    # button.on_press(callback=on_button_press)

    with aiy.audio.get_recorder():
        aiy.audio.say('system is online.')
        while True:
            status_ui.status('ready')
            speak = 'Press the button and speak'
            print(speak)
            aiy.audio.say(speak)
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
            # aiy.audio.say('ding')

            try:
                text, audio = assistant.recognize()
            except aiy._apis._speech.Error as e:
                print('Exception in speech request')
                aiy.audio.say('Exception in speech request,proxy timeout')
                continue
            except:
                print('other Error')
                continue

            if text is not None:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    aiy.audio.say('Time to say goodbye,see you soon,my love')
                    break
                print('You said "', text, '"')

                if 'turn on' in text:
                    led.set_state(aiy.voicehat.LED.ON)
                    print('LED on ')
                elif 'turn off the light' in text:
                    led.set_state(aiy.voicehat.LED.OFF)
                    print('LED off')
                elif 'blink' in text:
                    led.set_state(aiy.voicehat.LED.BLINK)
                    print('LED blink')


                if 'shut down' in text and 'computer' in text:
                    aiy.audio.say('I will shutdown this computer,please stand by')
                    # subprocess.call(['sudo', 'shutdown', '-h', 'now'])
                if 'reboot' in text and 'computer' in text:
                    aiy.audio.say('I will shutdown this computer,please stand by')
                    # subprocess.call(['sudo', 'reboot'])
                    break
                else:
                    aiy.audio.say('you said  ' + text)

            if audio is not None:
                aiy.audio.play_audio(audio)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
