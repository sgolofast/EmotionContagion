from otree.api import *
from numpy import random
import numpy as np


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iDec = models.IntegerField()
    dRT = models.FloatField()
    iConf = models.IntegerField()
    sButtonsPressed = models.LongStringField()
    sTimesPressed = models.LongStringField()
    bRow = models.BooleanField()
    dDev = models.IntegerField()

# FUNCTIONS

def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            p, session = player.participant, subsession.session
            p.bRow = bool(random.randint(0,2))
    for player in subsession.get_players():
        player.bRow = player.participant.bRow
        player.dDev = random.randint(3, 11)



# PAGES
class Ready(Page):
    pass

class Main(Page):
    form_model = 'player'
    form_fields = [
        'iDec', 'dRT'
    ]

    @staticmethod
    def vars_for_template(player: Player):

        dDevV = player.dDev
        c12 = '0,' + str(dDevV)
        c21 = str(dDevV) + ',0'
        if player.bRow:
            role = 'Row'
            a = 'c'
            b = 'd'
        else: 
            role = 'Column'
            a = 'C'
            b = 'D'
        return dict(
            c11 = '2,2',
            c12 = c12,
            c21 = c21,
            c22 = '1,1',
            role = role,
            A = a,
            B = b
        )

class Confidence(Page):
    pass



page_sequence = [Ready, Main, Confidence]
