import datetime
import typing
from enum import Enum

import dataclasses
from dataclasses_json import dataclass_json


@dataclass_json
@dataclasses.dataclass
class OncologyAlertnessQuestionnaire:
    """
    Это класс, определяющий актету онконастороженности.
    Сереализуется в валидный для https://surveyjs.io/ json,
    десериализуется из json, который позвращает эта анкета,
    сереализуется в этот же json,
    используется для скармливания ML модели для получения предсказаний.
    """

    class Q0(Enum):
        """Пол"""
        _0 = 'Женский'
        _1 = 'Мужской'

    q0: Q0

    class Q1(int):
        """Возраст:"""

        def value(this) -> int:
            return this

    q1: Q1

    class Q2(Enum):
        """Подвергались ли Вы воздействию вредных условий (различные виды излучения, вредное производство, токсичные вещества)?"""
        _1 = 'Да'
        _0 = 'Нет'

    q2: Q2

    class Q3(Enum):
        """Работали ли Вы на предприятиях с повышенной вредностью (горячий цех, химическое производство, нефтеперерабатывающее предприятие)?"""
        _0 = 'Да, есть или были в прошлом'
        _1 = 'Есть или были в прошлом'
        _2 = 'Нет'

    q3: Q3

    class Q4(Enum):
        """Болели ли Ваши кровные родственники злокачественными опухолевыми заболеваниями?"""
        _0 = 'Да'
        _1 = 'Нет'
        _2 = 'Не знаю'

    q4: Q4

    class Q5(Enum):
        """Вставали ли Вы ранее на учет к онкологу?"""
        _0 = 'Да'
        _1 = 'Нет'

    q5: Q5

    class Q6(Enum):
        """Вы курите?"""
        _0 = 'Да, больше 10 лет'
        _1 = 'Да, меньше 10 лет'
        _2 = 'Нет, никогда не курил'

    q6: Q6

    class Q7(Enum):
        """Какое количество сигарет в день Вы выкуриваете?"""
        _0 = 'Больше пачки'
        _1 = 'Меньше пачки'
        _2 = 'Не курю'

    q7: Q7

    class Q8(Enum):
        """В течение последних месяцев Вас беспокоил кашель?"""
        _0 = 'Да, бывает с примесью или прожилками крови'
        _1 = 'Да, с мокротой'
        _2 = 'Да, сухой'
        _3 = 'Нет'

    q8: Q8

    class Q9(Enum):
        """Являетесь ли Вы пассивным курильщиком (наличие активного курильщика дома, на работе)?"""
        _0 = 'Да'
        _1 = 'Нет'

    q9: Q9

    class Q10(Enum):
        """Как давно Вы в последний раз выполняли флюорографию, рентгенографию или КТ грудной клетки?"""
        _0 = 'В этом году'
        _1 = 'Больше года назад'
        _2 = 'Вообще не проходил'

    q10: Q10

    class Q11(Enum):
        """Замечали ли Вы изменение тембра голоса (осиплость, хрипоту)?"""
        _0 = 'Да, постоянно, дольше 1 месяца'
        _1 = 'Да, иногда в течение последнего месяца'
        _2 = 'Нет'

    q11: Q11

    class Q12(Enum):
        """Был ли у Вас дискомфорт во время глотания пищи или воды (застревание, ощущение инородного тела в горле или пищеводе)?"""
        _0 = 'Да, дольше 1 месяца, стабильно'
        _1 = 'Иногда, около месяца'
        _2 = 'Нет'

    q12: Q12

    class Q13(Enum):
        """Когда-либо Вам был установлен диагноз: язва (или полип) желудка?"""
        _0 = 'Да'
        _1 = 'Нет'
        _2 = 'Не помню'

    q13: Q13

    class Q14(Enum):
        """Была ли у Вас рвота после еды?"""
        _0 = 'Да, дольше 1 месяца, стабильно'
        _1 = 'Да, иногда, около месяца'
        _2 = 'Нет'

    q14: Q14

    class Q15(Enum):
        """Находили ли у Вас ранее заболевание толстого кишечника?"""
        _0 = 'Да, полипы толстой кишки'
        _1 = 'Да, геморрой'
        _2 = 'Да, трещину заднего прохода'
        _3 = 'Нет'

    q15: Q15

    class Q16(Enum):
        """Ощущали ли Вы дискомфорт (или боли) во время дефекации в прямой кишке, крестце или копчике?"""
        _0 = 'Да'
        _1 = 'Нет'

    q16: Q16

    class Q17(Enum):
        """Замечали ли Вы после дефекации кровь на туалетной бумаге или изменение цвета кала (черный или обесцвеченный)?"""
        _0 = 'Да'
        _1 = 'Нет'

    q17: Q17

    class Q18(Enum):
        """Бывают у Вас ложные позывы на стул?"""
        _0 = 'Да'
        _1 = 'Нет'

    q18: Q18

    class Q19(Enum):
        """Замечали ли Вы беспричинное повышенние температуры тела (кроме простудных/инфекционных заболеваний)?"""
        _0 = 'Постоянно, более 1 месяца'
        _1 = 'Да, периодически'
        _2 = 'Нет'

    q19: Q19

    class Q20(Enum):
        """Замечали ли Вы у себя усиленную потливость (без физической нагрузки)?"""
        _0 = 'Да, постоянно больше 1 месяца'
        _1 = 'Нет'

    q20: Q20

    class Q21(Enum):
        """Бывает ли у Вас отсутствие аппетита без причины или отвращение к еде?"""
        _1 = 'Да'
        _0 = 'Нет'

    q21: Q21

    class Q22(Enum):
        """Бывают ли у Вас необъяснимые(без причины) носовые кровотечения или подкожные кровоизлияния (синяки)?"""
        _0 = 'Да'
        _1 = 'Нет'

    q22: Q22

    class Q23(Enum):
        """Есть ли у Вас боли, требующие систематического приема анальгетиков?"""
        _0 = 'Да'
        _1 = 'Нет'

    q23: Q23

    class Q24(Enum):
        """Заметили ли Вы, что похудели за последние 3 месяца больше чем на 5 кг ненамеренно?"""
        _0 = 'Да, существенно'
        _1 = 'Нет'
        _2 = 'Не знаю'

    q24: Q24

    class Q25(Enum):
        """Находили ли Вы у себя увеличенные лимфоузлы?"""
        _0 = 'Да'
        _1 = 'Нет'

    q25: Q25

    class Q26(Enum):
        """Замечали ли Вы у себя на коже не исчезающие долгое время язвы или трещины?"""
        _0 = 'Да'
        _1 = 'Нет'

    q26: Q26

    class Q27(Enum):
        """Не было ли у Вас последнее время изменения формы и цвета родинок?"""
        _0 = 'Да, кровоточат'
        _1 = 'Да, цвет изменился'
        _2 = 'Да, увеличились и появились новые'
        _3 = 'Нет'

    q27: Q27

    class Q28(Enum):
        """Было ли у вас нарушения мочеиспускания?"""
        _0 = 'Да'
        _1 = 'Нет'

    q28: Q28

    class Q29(Enum):
        """Не замечали ли Вы последнее время примесь крови в моче?"""
        _0 = 'Да'
        _1 = 'Нет'

    q29: Q29

    class Q30(Enum):
        """Находите ли Вы у себя изменения в молочных железах?"""
        _0 = 'Да, выделения из соска кровянистого цвета'
        _1 = 'Появление уплотнений, узлов'
        _2 = 'Втяжение или уплощение соска'
        _3 = 'Нет'

    q30: Q30

    class Name(str):
        """Ваше имя"""

    name: Name

    class Surname(str):
        """фамилия"""

    surname: Surname

    class Q31(Enum):
        """Бывают ли у Вас сукровичные (или кровянистые) выделения из половых путей, не связанные с месячным?"""
        _0 = 'Да'
        _1 = 'Нет'

    q31: Q31 = Q31._1

    class Q32(Enum):
        """Замечали ли Вы у себя кровянистые выделения из половых путей после половых сношений, гинекологических осмотров или при запорах?"""
        _0 = 'Да'
        _1 = 'Нет'

    q32: Q32 = Q32._1

    class DoctorName(str):
        """фамилия вашего доктора"""

    doctor_name: DoctorName = None

    class ConsultationTime(datetime.datetime):
        """На какое время вы записаны к врачу"""

    consultation_time: typing.Optional[ConsultationTime] = None

    @classmethod
    def to_surveyjs_io_json(cls) -> dict:
        def first_page() -> dict:
            return {
                "name": f"Как с вами связаться?",
                "elements": [
                    {
                        "name": "name",
                        "type": "text",
                        "isRequired": True,
                        "title": cls.Name.__doc__,
                    }, {
                        "name": "surname",
                        "type": "text",
                        "isRequired": True,
                        "title": cls.Surname.__doc__,
                    }, {
                        "name": "doctor_name",
                        "type": "text",
                        "isRequired": False,
                        "title": cls.DoctorName.__doc__,
                    }, {
                        "name": "consultation_time",
                        "type": "text",  # нет выбора дат нормального?
                        "isRequired": False,
                        "title": cls.ConsultationTime.__doc__,
                        "placeHolder": "03.12.19 14:30",
                    },
                ]
            }

        # для всех вопросов с выбором ответов из нескольких вариантов
        def one_page_enum(field_name: str, question: str, ansvers: typing.List[str]) -> dict:
            return {
                "elements": [{
                    "type": "radiogroup",
                    "name": field_name,
                    "title": question,
                    "isRequired": True,
                    "choices": [{
                        "value": answer,
                        "text": answer
                    } for answer in ansvers]},
                ]
            }

        def one_page_int(field_name: str) -> dict:
            return {
                "elements": [{
                    "name": field_name,
                    "type": "text",
                    "title": question,
                    "isRequired": True,
                    "inputType": "number",
                }]
            }

        pages = list()
        pages.append(first_page())

        for field_name in [
            'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11',
            'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21',
            'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30'
        ]:
            type_of_field: type = cls.__dataclass_fields__[field_name].type
            question = type_of_field.__doc__
            if issubclass(type_of_field, Enum):
                answers = [field.value for _, field in type_of_field.__members__.items()]
                pages.append(one_page_enum(field_name, question, answers))
            elif issubclass(type_of_field, int):
                pages.append(one_page_int(field_name))
            else:
                raise TypeError(
                    f"It is not clear how to generate a questionnaire for the type {type_of_field.__repr__()}")

        for field_name in ['q31', 'q32']:
            type_of_field: type = cls.__dataclass_fields__[field_name].type
            question = type_of_field.__doc__
            answers = [field.value for _, field in type_of_field.__members__.items()]
            result = one_page_enum(field_name, question, answers)
            result['visibleIf'] = f'{{q0}} = "{cls.Q0._0.value}"'  # показывать только для женщин
            pages.append(result)

        all_survey = {
            "locale": "ru",
            "loadingHtml": "Загрузка",
            "completedHtml": {
                "ru": '''
                <span>
                    Спасибо, ваши ответы записаны. Ожидайте приёма врача.
                </span><script>
                    window.addEventListener('load', () => {
                        setTimeout( () => {
                            window.location.reload();  
                        }, 60000);
                    })
                </script>'''
            },

            "pages": pages,
            "showQuestionNumbers": "off",
            "showProgressBar": "top",
            "goNextPageAutomatic": True,
            "startSurveyText": "Начать анкету",
            "pagePrevText": "Вернуться",
            "pageNextText": "Далее",
            "completeText": "Завершить",
        }

        return all_survey


# on client Survey.Model(surveyjs_io_json); отрисовывает анкету
# https://surveyjs.io/Overview/Library/
surveyjs_io_json: dict = OncologyAlertnessQuestionnaire.to_surveyjs_io_json()
