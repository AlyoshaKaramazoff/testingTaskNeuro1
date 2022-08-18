import input_func

class hello_logic:

    """
        CТРУКТУРА ВОЗВРАЩАЕМГО ОТВЕТА
        afterStart[int], confirm, wrong_time, repeat [bool]
    """

    def __init__(self):
        pass


    def hello(self, name):
        print(name+", Вас беспокоит компания X, мы проводим опрос удовлетворенности нашими услугами. Подскажите, вам удобно сейчас говорить?")
        a = input_func.input_func()
        if a == "Null":
            return hello_logic().hello_null()
        if a == "Нет" or a == "Занят":
            return 2, False, False, False # hangup_wrong_time
        if a == "Ещё раз":
            return hello_logic().hello_repeat()
        else:
            return 1, True, False, False # recommend_main


    def hello_repeat(self):
        print("\nЭто компания X  Подскажите, вам удобно сейчас говорить?")
        a = input_func.input_func()
        if a == "Нет" or a == "Занят":
            return 2, False, True, True # hangup_wrong_time
        if a == "Null":
            return 3, False, False, True # hangup_null
        else:
            return 1, True, False, True # recommend_main


    def hello_null(self):
        print("\nИзвините, вас не слышно. Вы могли бы повторить.")
        a = input_func.input_func()
        if a == "Null":
            return 3, False, False, False # hangup_null
        if a == "Ещё раз":
            return hello_logic().hello_repeat()
        if a == "Нет" or a == "Занят":
            return 2, False, True, False # hangup_wrong_time
        else:
            return 1, True, False, False # recommend_main


