from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class LampiSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')


    @intent_handler(IntentBuilder('SetHueIntent').require('SetHue'))
    def handle_set_hue_intent(self, message):
        self.speak_dialog(message)

    def stop(self):
        pass


def create_skill():
    return LampiSkill()
