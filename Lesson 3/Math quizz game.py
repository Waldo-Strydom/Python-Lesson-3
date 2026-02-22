import random
score = 0
def create_question(q_count):
    current_question = 1
    
    

    while current_question<=q_count:
      get_q_type()
      current_question+=1  



def get_q_type():
    ran = random.randint(1,2)
    symbol = ""
    if ran ==1:
        symbol = "+"
    else:
        symbol = "-"


    get_question(symbol)


def get_question(symbol):
    global score
    ans = 0
    question_print = ""
    num_1 = random.randint(1,12) 
    num_2 = random.randint(1,12) 

    if symbol == "+":
        question_print = f"{num_1} + {num_2} = ???"
        print(question_print)
        user_ans =float(input(""))
        ans = float(num_1+num_2)
    else:
        question_print = f"{num_1} - {num_2} = ???"
        print(question_print)
        user_ans =float(input(""))
        ans = float(num_1-num_2)

    res = result(user_ans,ans)
    
    if res:
        print("Correct ",num_1 ,symbol, num_2, "=", ans )
        
        score+=1
        print("Score ", score)
    else:
        print("Incorrect ",num_1 ,symbol, num_2, "=", ans )
        print("Score ", score)

def result(user_ans,ans):
    if user_ans==ans:
        return True
    else: 
        return False

print("Welcome to the math game.")

quizz_count = int(input("How many questions do you want?\n"))

if type(quizz_count)==int:
    create_question(quizz_count)
