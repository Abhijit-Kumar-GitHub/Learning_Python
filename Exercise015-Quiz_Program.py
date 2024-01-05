questions = ("How many elements are there in the periodic table?: ",
             "Which mammal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?:",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?:")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0
q_n = 0

for question in questions:
    print("----------------------------------------------")
    print(question)
    for option in options[q_n]:
        print(option)

    guess= input("Enter your answer(A, B, C, D): ").upper()
    guesses.append(guess)

    print()
    if guess == answers[q_n]:
        print("CORRECT!")
        score += 1
    else: 
        print("INCORRECT!")
        print(f"The correct option is {answers[q_n]}")

    q_n += 1    

print("--------------------------------------------")
print("              The RESULTCARD                ")
print("--------------------------------------------")


print("Your  selected  answers: ", end="")                     # Using the end = "" to make the next line start right next to it .
for guess in guesses: 
    print(guess, end=" ")
print()                                             # To make the next line start from a new line.

print("The correct options are: ", end="")
for answer in answers: 
    print(answer, end=" ")
print()

marks = score/len(questions) * 100
print(f"you obtained {marks}%")




















