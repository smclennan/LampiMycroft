from pwd import getpwnam
import os
import subprocess

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class LampiSkill(MycroftSkill):
    def set_user(uid, gid):
        os.setgid(gid)
        os.setuid(uid)

    def get_config(self, key):
        return (self.settings.get(key) or
                self.config_core.get('LampiSkill', {}).get(key))

    def __init__(self):
        super().__init__()
        self.learning = True
        self.uid = None
        self.gid = None

    def initialize(self):
        my_setting = self.settings.get('my_setting')
        user = self.get_config('user')
        if user:
            pwnam = getpwnam(user)
            self.uid = pwnam.pw_uid
            self.gid = pwnam.pw_gid


    @intent_handler(IntentBuilder('SetHueIntent').require('SetHue'))
    def handle_set_hue_intent(self, message):
        utter = message.data.get('utterance').lower()
        utter = utter.split(' ')
        try:
            if self.uid and self.gid:
                subprocess.Popen(['echo', 'test success'],
                                 preexec_fn=set_user(self.uid, self.gid))
            else:
                subprocess.Popen(['/home/pi/connected-devices/Lampi/lamp_cmd', '--hue', utter[2]])
        except Exception:
                self.speak_dialog("Error")
                
    @intent_handler(IntentBuilder('SetSatIntent').require('SetSat'))
    def handle_set_sat_intent(self, message):
        utter = message.data.get('utterance').lower()
        utter = utter.split(' ')
        try:
            if self.uid and self.gid:
                subprocess.Popen(['echo', 'test success'],
                                 preexec_fn=set_user(self.uid, self.gid))
            else:
                subprocess.Popen(['/home/pi/connected-devices/Lampi/lamp_cmd', '--saturation', utter[2]])
        except Exception:
                self.speak_dialog("Error")             
     
    @intent_handler(IntentBuilder('SetBrightnessIntent').require('SetBrightness'))
    def handle_set_brightness_intent(self, message):
        utter = message.data.get('utterance').lower()
        utter = utter.split(' ')
        try:
            if self.uid and self.gid:
                subprocess.Popen(['echo', 'test success'],
                                 preexec_fn=set_user(self.uid, self.gid))
            else:
                subprocess.Popen(['/home/pi/connected-devices/Lampi/lamp_cmd', '--brightness', utter[2]])
        except Exception:
                self.speak_dialog("Error")
                
    @intent_handler(IntentBuilder('TurnOnIntent').require('TurnOn'))
    def handle_turn_on_intent(self, message):
        utter = message.data.get('utterance').lower()
        utter = utter.split(' ')
        try:
            if self.uid and self.gid:
                subprocess.Popen(['echo', 'test success'],
                                 preexec_fn=set_user(self.uid, self.gid))
            else:
                subprocess.Popen(['/home/pi/connected-devices/Lampi/lamp_cmd', '--on'])
        except Exception:
                self.speak_dialog("Error")
                                  
    @intent_handler(IntentBuilder('TurnOffIntent').require('TurnOff'))
    def handle_turn_off_intent(self, message):
        utter = message.data.get('utterance').lower()
        utter = utter.split(' ')
        try:
            if self.uid and self.gid:
                subprocess.Popen(['echo', 'test success'],
                                 preexec_fn=set_user(self.uid, self.gid))
            else:
                subprocess.Popen(['/home/pi/connected-devices/Lampi/lamp_cmd', '--off'])
        except Exception:
                self.speak_dialog("Error")

    def stop(self):
        pass


def create_skill():
    return LampiSkill()
