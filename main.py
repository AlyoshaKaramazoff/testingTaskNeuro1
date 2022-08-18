import hello_logic
import main_logic
import hangup_logic


# Начальные данные для отчета
confirm = None
wrong_time = None
repeat = None
recommendation_score = None
recommendation = None
question = None


# НАЧАЛО ДИАЛОГА
afterStart = hello_logic.hello_logic().hello("Герман")
confirm = afterStart[1]
wrong_time = afterStart[2]
repeat = afterStart[3]
# afterStart = 1 / 2 / 3
# 1 - recommend_main
# 2 - hangup_wrong_time
# 3 - hangup_null

if afterStart[0] == 1:
    bodyAlg = main_logic.main_logic().recommend_main()
if afterStart[0] == 2:
    hangup_logic.hangup_logic().hangup_wrong_time()
    bodyAlg = (None, None, None)
if afterStart[0] == 3:
    hangup_logic.hangup_logic().hangup_null()
    bodyAlg = (None, None, None)

# afterBody
# 1 - hangup_negative
# 2 - hangup_negative
# 3 - forward
# 4 - hangup_wrong_time
# 5 - hangup_null

try:
    recommendation_score = bodyAlg[0][1]
    if bodyAlg[0][0] == 1:
        hangup_logic.hangup_logic().hangup_negative()
        recommendation = bodyAlg[1]
        if bodyAlg[1] == None:
            recommendation = 'negative'
    if bodyAlg[0][0] == 2:
        hangup_logic.hangup_logic().hangup_positive()
        if bodyAlg[1] == None:
            recommendation = 'positive'
        else:
            recommendation = bodyAlg[1]

# исключение возможных ошибок
except TypeError:
    recommendation_score = bodyAlg[1]
    if bodyAlg[0] == 1:
        hangup_logic.hangup_logic().hangup_negative()
        recommendation = "negative"
    if bodyAlg[0] == 2:
        hangup_logic.hangup_logic().hangup_positive()
        recommendation = "positive"
    if bodyAlg[0] == 3:
        hangup_logic.hangup_logic().forward()
        question = True
    if bodyAlg[0] == 4:
        hangup_logic.hangup_logic().hangup_wrong_time()
        wrong_time = True
    if bodyAlg[0] == 5:
        hangup_logic.hangup_logic().hangup_null()

# Формирование ответа
final_answer = [
    confirm,
    wrong_time,
    repeat,
    recommendation_score,
    recommendation,
    question]

# Вывод ответа
print("\n**************************************")
print(
    "Confirm: "+str(final_answer[0]) +
    "\nWrong_time: "+str(final_answer[1]) +
    "\nRepeat: "+str(final_answer[2]) +
    "\nRecommendation score: "+str(final_answer[3]) +
    "\nRecommendation: "+str(final_answer[4]) +
    "\nQuestion: "+str(final_answer[5]))
print("**************************************")