from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'TrustGamePunishment'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(500)
    MULTIPLIER = 3
    MULTIPLIER_PUNISHMENT = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=cu(0),
        max=cu(500),
        label="Укажите сумму, которую вы хотите отправить участнику Б:",
    )
    sent_back_amount = models.CurrencyField(min=cu(0),
    label="Укажите сумму, которую вы хотите отправить участнику А:")
    punishment = models.BooleanField(choices=[[True, "Да"], [False, "Нет"]],
    label="Если вас не устраивает сумма, которую вам отправил участник Б, хотите ли вы его наказать?")
    punishment_display = models.BooleanField(default=False)
    punishment_amount = models.CurrencyField(
        min=cu(5),
        max=cu(500),
        label="Выберите сумму наказания:"
    )
    



class Player(BasePlayer):
    pass

# FUNCTIONS
def sent_back_amount_max(group: Group):
    return group.sent_amount * C.MULTIPLIER


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount

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
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        tripled_amount = group.sent_amount * C.MULTIPLIER
        return dict(tripled_amount=tripled_amount)

class Punishment(Page):
    form_model = 'group'
    form_fields = ['punishment']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1
    

class PunishmentAmount(Page):
    form_model = 'group'
    form_fields = ['punishment_amount']

    @staticmethod
    def is_displayed(player: Player, group: Group):
        return (player.id_in_group == 1 and group.punishment_display == True)

class PunishmentWaitPage(WaitPage):
    pass

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class ResultsNew(Page):
    pass

class Results(Page):

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


page_sequence = [
    Punishment, 
    PunishmentAmount,
    PunishmentWaitPage,
    ResultsNew
]
