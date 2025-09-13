print("Welcome to the Quiz Game User")

play_choice = input("Would you like to continue (Y/N)? ")

if play_choice != "Y":
    quit()

print("\nOkay lets play! 😁, Here are the rules:\n\n1)There will be 5 questions on various topics under general knowledge\n2)Only write the answer and not the option number(Spelling errors)\n3)Score will be given after the quiz\n\n\n\nLets start!")

o_1 = ["1) 1917","2) 1923","3) 1914", "4) 1920"]
o_2 = ["1) Venus","2) Earth","3) Mars","4) Jupiter"]
o_3 = ["1) Beijing","2) Tokyo","3) Seoul","4) Bangkok"]
o_4 = ["1) Amazon","2) Mississippi","3) Nile","4) Yangtze"]
o_5 = ["1) 1896","2) 1900","3) 1912","4) 1924"]

q_1 = int(input(f"In what year did the Great October Socialist Revolution take place? \n{o_1} \nAnswer: ")) #correct answer is 1.
q_2 = int(input(f"Which planet in the solar system is known as the “Red Planet”? \n{o_2} \nAnswer: ")) #correct answer is 3.
q_3 = int(input(f"What is the capital of Japan? \n{o_3} \nAnswer: ")) #correct answer is 2.
q_4 = int(input(f"Which river is the longest in the world?\n{o_4} \nAnswer: ")) #correct answer is 3.
q_5 = int(input(f"In what year was the first international modern Olympiad held?\n{o_5} \nAnswer: ")) #correct answer is 1.

score = 0
if q_1 == 1:
    score += 1
if q_2 == 3:
    score += 1 
if q_3 == 2:
    score += 1 
if q_4 == 3:
    score += 1 
if q_5 == 1:
    score += 1

if score == 0:
    print(f"You got {score}/5!\nYou got work to do! 😓")
elif score >= 1 and score <= 2:
    print(f"You got {score}/5!\nPractice some more and you can do it! 🫡")
elif score == 3:
    print(f"You got {score}/5!\nYou did well! 😊")
elif score >= 4 and score <= 5:
    print(f"You got {score}/5!\nDamn near perfect! 🤩")

print("Thanks for playing the game with me!")