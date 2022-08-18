import input_func

class main_logic():

    def __init__(self):
        pass

    def score_scale(self, a, fcn):
        try:
            score = int(a)
            if score <= 8:
                return 1 , score #hangup_negative
            else:
                return 2 , score #hangup_positive
        except ValueError:
            return fcn

    def moods(self, a):
        if a == "Нет":
            return main_logic().recommend_score_negative()
        if a == "Возможно":
            return main_logic().recommend_score_neutral()
        if a == "Да":
            return main_logic().recommend_score_positive()
        else:
            return main_logic().recommend_default()

    def recommend_main(self):
        print("\nСкажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? Оцените, пожалуйста, по шкале от «0» до «10», где «0» - не буду рекомендовать, «10» - обязательно порекомендую.")
        a = input_func.input_func()
        if a == "null":
            return main_logic().recommend_null()
        if a == "Не знаю":
            return main_logic().recomend_repeat_2()
        if a == "Занят":
            return 4, None, None # hangup_wrong_time
        else:
            return main_logic().score_scale(a, main_logic().moods(a))


    def recomend_repeat(self):
        print("\nКак бы вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от 0 до 10, где 0 - точно не порекомендую, 10 - обязательно порекомендую.")
        a = input_func.input_func()
        return main_logic().score_scale(a, None), None

    def recomend_repeat_2(self):
        print("\nНу если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0».")
        a = input_func.input_func()
        return  main_logic().score_scale(a, None), None


    def recommend_score_negative(self):
        print("\nНу а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?")
        a = input_func.input_func()
        return main_logic().score_scale(a, None), "negative"

    def recommend_score_neutral(self):
        print("\nНу а от 0 до 10 как бы вы оценили ?")
        a = input_func.input_func()
        return main_logic().score_scale(a, None), "dont_know"

    def recommend_score_positive(self):
        print("\nХорошо, а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10?")
        a = input_func.input_func()
        return main_logic().score_scale(a, None), "positive"

    def recommend_null(self):
        print("\nИзвините вас совсем не слышно,  повторите пожалуйста?")
        a = input_func.input_func()
        if a == "null":
            return 5, None, None # hangup_null
        else:
            return main_logic().recomend_repeat()

    def recommend_default(self):
        print("\nПовторите пожалуйста")
        a = input_func.input_func()
        if a == "null":
            return 5, None, None  # hangup_null
        if a == "Вопрос":
            return 3, None, True # forward
        else:
            return main_logic().recomend_repeat()
