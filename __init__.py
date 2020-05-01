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
        try:
            if self.uid and self.gid:
                subprocess.Popen(['echo', 'test success'],
                                 preexec_fn=set_user(self.uid, self.gid))
            else:
                subprocess.Popen(['/home/pi/connected-devices/Lampi/lamp_cmd', '--hue', '0.5'])
        except Exception:
                self.speak_dialog("hello world")

    def stop(self):
        pass


def create_skill():
    return LampiSkill()
