from transitions import Machine
import random


class NarcolepticSuperhero(object):

    states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']

    def __init__(self, name):
        self.name = name
        self.kittens_rescued = 0
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states, initial='asleep')
        self.machine.add_transition(trigger='wake_up', source='asleep', dest='hanging out')
        self.machine.add_transition(trigger='work_out', source='hanging out', dest='hungry')
        self.machine.add_transition(trigger='eat', source='hungry', dest='hanging out')
        self.machine.add_transition(trigger='distress_call', source="*", dest="saving the world",
                                    before="change_into_super_secret_costume")
        self.machine.add_transition(trigger='complete_mission', source='saving the world', dest='sweaty',
                                    after='update_journal')
        self.machine.add_transition(trigger='clean_up', source='sweaty', dest='asleep', conditions=['is_exhausted'])
        self.machine.add_transition(trigger='clean_up', source='sweaty', dest='hanging out')
        self.machine.add_transition(trigger='nap', source='*', dest='asleep')

    def update_journal(self):
        self.kittens_rescued += 1

    def is_exhausted(self):
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print("Beauty, eh?")