questionsarray=[
    {
        "question": "What is the longest ocean in the world?\n1) Pacific Ocean\n2) Indian Ocean\n3) Arctic Ocean\n4) Southern Ocean",
        "ansoption": "1",
        "ans": "Pacific Ocean"
    },
    {
        "question": "Which planet is known as the Red Planet?\n1) Mars\n2) Venus\n3) Jupiter\n4) Mercury",
        "ansoption": "1",
        "ans": "Mars"
    },
    {
        "question": "What is the capital city of France?\n1) Berlin\n2) Madrid\n3) Rome\n4) Paris",
        "ansoption": "4",
        "ans": "Paris"
    },
    {
        "question": "What is the chemical symbol for water?\n1) H2O\n2) CO2\n3) O2\n4) NaCl",
        "ansoption": "1",
        "ans": "H2O"
    }
]

score=0
i=0
def generate_quiz(displayquestion):
  global score
  global i

  print(displayquestion["question"])
  try:
    user=input("enter your option")
    if user in "1234":
      if user==displayquestion["ansoption"]:
        print("your answer is correct ")
        score+=2
        print(f"your current score is {score}")
      else:
        print("you selected incorrect option")
        print("correct option is {}".format(displayquestion["ans"]))
        score-=1
        print(f"your current score is {score}")
      if i!=len(questionsarray)-1:
        i+=1
        generate_quiz(questionsarray[i])
      else:
        return
    else:
      print("select valid option")
      generate_quiz(displayquestion)
  except Exception as e:
    print(e)
    print("error occured restarting current session")
    generate_quiz(displayquestion)
print("welcome to quiz ")
print("for correct answer you will be awarded 2 points")
print("for wrong answer you will be deducted 1 point")

generate_quiz(questionsarray[i])
