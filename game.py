print("WELCOME TO QUIZ GAME ")
response= input("Do You Want To Play The Game: ")
if response.lower() !="yes":
    quit()
print("LETS START THE GAME ")   
print("""game details: 
      This game contains of total 3 levels 
      level 1: contains 4 questions, for each correct answer you score 1 point and there are no negative marking
      level 2: contains 4 questions, for each correct answer 2 points and for incorrect answer -1 
      level 3: contains 4 questions, for each correct answer 4 points and or incorrect answers -2
      """)
score =0
total_score=0
#level 1 questions
print("Level -1")
question1= input("What is the full form of HR? ")
answer1= "human resource"
if question1.lower() == answer1:
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT")
question2= input("What is the full form of JD (in job recruitment)? ")

if question2.lower() == "job description":
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT")

question3= input("What is the full form of HRM? ")
if question3.lower() == "human resource management":
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT")

question4= input("What is the full form of PAN (used in Indian employee verification)? ")
if question4.lower() == "permanent account number":
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT")
print("you have completed level-1 questions")
print("you have  score " +str(score) +" in the  level-1")
total_score+=score

# this is level 2 
print("\nlevel- 2")
score1=0
question5= input("What is the full form of L&D in HR? ")
answer5="learning and development"
if question5.lower() == answer5:
    print("CORRECT!")
    score1 +=2
else:
    print("INCORRECT")
    score1-=1
 
question6= input("What is the full form of HCM? ")
answer6="human capital management"
if question6.lower() == answer6:
    print("CORRECT!")
    score1 +=2
else:
    print("INCORRECT")
    score1-=1

question7= input("What is the full form of HRIS? ")
answer7="human resource information system"
if question7.lower() == answer7:
    print("CORRECT!")
    score1 +=2
else:
    print("INCORRECT")
    score1-=1

question8= input("What is the full form of T&D in HR? ")
answer8="training and development"
if question8.lower() == answer8:
    print("CORRECT!")
    score1 +=2
else:
    print("INCORRECT")
    score1-=1
print("you have completed level 2 questions ")
print("you have scored "+str(score1)+" in level-2")
total_score+=score1

#level-3
print("\nLevel-3")
score2=0
question9= input("What is the full form of ESOP? ")
answer9="employee stock ownership plan"
if question9.lower() == answer9:
    print("CORRECT!")
    score2 +=4
else:
    print("INCORRECT")
    score2-=2
 
question10= input("What is the full form of PF (in employee financial benefits)?")
answer10=" provident fund"
if question10.lower() == answer10:
    print("CORRECT!")
    score2 +=4
else:
    print("INCORRECT")
    score2-=2

question11= input("What is the full form of ESOP?")
answer11= "employee stock ownership plan"
if question11.lower() == answer11:
    print("CORRECT!")
    score2 +=4
else:
    print("INCORRECT")
    score2-=2

question12= input("What is the full form of ER in HR context? ")
answer12="employee relations"
if question12.lower() == answer12:
    print("CORRECT!")
    score2 +=4
else:
    print("INCORRECT")
    score2-=2
print("you have completed level 2 questions ")
print("you have scored "+str(score2)+" in level-3")
total_score+=score2
print(total_score)