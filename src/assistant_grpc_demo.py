#!/usr/bin/env python3
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

import logging

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat


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

    #button.on_press(callback=on_button_press)

    with aiy.audio.get_recorder():
        while True:
            status_ui.status('ready')
            print('Press the button and speak')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')

            try:
                text, audio = assistant.recognize()
            except aiy._apis._speech.Error as e:
                print('Exception in speech request')
                aiy.audio.say('Exception in speech request,proxy timeout')
                continue
            except :
                print('other Error')
                continue

            if text is not None:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
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

                aiy.audio.say('I heard you said  '+text)

            if audio is not None:
                aiy.audio.play_audio(audio)


if __name__ == '__main__':
    main()
