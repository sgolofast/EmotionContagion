from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Questionnaire'
    PLAYERS_PER_GROUP = 20
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

# FUNCTIONS
def likertexp(label):
    return models.IntegerField(initial=0, choices=[[1, ''], [2, ''], [3, ''], [4, ''],
    [5, '']], label=label,widget=widgets.RadioSelect)

class Player(BasePlayer):
    FearRate = likertexp("Страх")
    AngerRate = likertexp("Злость")
    JoyRate = likertexp("Радость")
    SadRate = likertexp("Грусть")
    DisgustRate = likertexp("Отвращение")
    SurpriseRate = likertexp("Удивление")
    age = models.IntegerField(label='Укажите год своего рождения:', min=1960)
    gender = models.StringField(choices=[['female', 'Женщина'], ['male', 'Мужчина'],
                                         ],
                                label='Ваш пол:', widget=widgets.RadioSelect)
    country = models.StringField(
        label='В каком регионе (например, Кемеровская область) Вы прожили большую часть своей жизни? Если не в России - '
              'укажите название страны.')
    education = models.StringField(
        choices=[['Основное общее образование (9 классов)', 'Основное общее образование (9 классов)'],
                 ['Среднее общее образование', 'Среднее общее образование (11 классов)'],
                 ['Среднее профессиональное образование (техникум, колледж)',
                  'Среднее профессиональное образование (техникум, колледж)'],
                 ['Незаконченное высшее образование - бакалавриат', 'Незаконченное высшее образование - бакалавриат'],
                 ['Высшее образование - бакалавриат', 'Высшее образование - бакалавриат'],
                 ['Высшее образование - специалитет, магистратура', 'Высшее образование - специалитет, магистратура'],
                 ['Высшее образование - подготовка кадров высшей квалификаци',
                  'Высшее образование - подготовка кадров высшей квалификаци']],
        label='Ваш наивысший уровень образования:', widget=widgets.RadioSelect)
    study_field = models.StringField(choices=[['Экономика', 'Экономика и управление'],
                                              ['Математические и естественные науки',
                                               'Математические и естественные науки'],
                                              ['Инженерное дело, технологии и технические науки',
                                               'Инженерное дело, технологии и технические науки'],
                                              ['Здравоохранение и медицинские науки',
                                               'Здравоохранение и медицинские науки'],
                                              ['Образование и педагогические науки',
                                               'Образование и педагогические науки'],
                                              ['Искусство и культура', 'Искусство и культура'],
                                              ['Социология, писхология и философия',
                                               'Социология, писхология и философия'],
                                              ['Юриспруденция', 'Юриспруденция'],
                                              ['Политические науки и регионоведение',
                                               'Политические науки и регионоведение'],
                                              ['Языкознание и литературоведение', 'Языкознание и литературоведение'],
                                              ['История и археология', 'История и археология'],
                                              ['Другая область', 'Другая область']],
                                     label='В какой области Вы специализируетесь?', widget=widgets.RadioSelect)
    wealth = models.IntegerField(
        label="Представьте шкалу дохода, где 1 означает принадлежность к группе с самым низким доходом, 10 - к группе "
              "с самым высоким доходом в стране. Укажите, к какой группе принадлежит ваше домохозяйство. Пожалуйста, учтите "
              "все зарплаты, пенсионные выплаты и другие доходы",
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"], [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10"]]
    )
# PAGES
class Questionnaire1(Page):
    form_model = 'player'
    form_fields = ['FearRate', 'AngerRate', 'JoyRate', 'SadRate', 'DisgustRate', 'SurpriseRate']

class Questionnaire2(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'country', 'education', 'study_field', 'wealth']

class EndPage(Page):
    pass


page_sequence = [Questionnaire1, Questionnaire2, EndPage]
