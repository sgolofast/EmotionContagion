from otree.api import *


doc = """
This app is a standard trust game.
"""


class C(BaseConstants):
    NAME_IN_URL = 'TrustGame'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(500)
    BASELINE = cu(0)
    EXAMPLE_1_SENT = cu(100)
    EXAMPLE_1_TRIPLE = cu(300)
    EXAMPLE_1_BACK = cu(150)
    EXAMPLE_1_A = cu(550)
    EXAMPLE_1_B = cu(650)
    MULTIPLIER = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        label="Укажите сумму, которую вы хотите отправить участнику Б:",
        min=cu(0),
        max=cu(500)
    )
    sent_back_amount = models.CurrencyField(min=cu(0),
    label="Укажите сумму, которую вы хотите отправить участнику А:")


class Player(BasePlayer):
    pass


# FUNCTIONS
def sent_back_amount_max(group: Group):
    return group.sent_amount * C.MULTIPLIER


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if group.sent_amount > 0:
        p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
        p2.payoff = C.ENDOWMENT + group.sent_amount * C.MULTIPLIER - group.sent_back_amount
    else:
        p1.payoff = C.ENDOWMENT 
        p2.payoff = C.ENDOWMENT



# PAGES
class Introduction(Page):
    pass

class Send(Page):

    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

class SendBackWaitPage(WaitPage):
    pass

class SendBack(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group == 2 and group.sent_amount > 0

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        tripled_amount = group.sent_amount * C.MULTIPLIER
        return dict(tripled_amount=tripled_amount)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
