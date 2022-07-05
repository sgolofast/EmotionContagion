from otree.api import *
import itertools
       

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'MediaFeed'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.BooleanField()
    zoom = models.StringField(label="Пожалуйста, укажите свой ник в Zoom:")

# FUNCTIONS
def creating_session(subsession):
    treatments = itertools.cycle([True, True, False, False])
    for player in subsession.get_players():
        participant = player.participant
        participant.treatment = next(treatments)

# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['zoom']

class Instruction(Page):
    pass

class PositiveFeed(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.treatment == True
    
    timer_text = "Оставшееся время на просмотр ленты:"
    timeout_seconds = 180


class NegativeFeed(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.treatment == False
    
    timer_text = "Оставшееся время на просмотр ленты:"
    timeout_seconds = 180


class Results(Page):
    pass


page_sequence = [Introduction, Instruction, PositiveFeed, NegativeFeed]
