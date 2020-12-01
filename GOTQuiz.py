from GOTQuestions import GOTQuestion

quizPrompts = [
    "At the beginning of the series, how many children do Ned and Catelyn Stark have?\n(a) 4\n(b) 3\n(c) 6\n(d) 3\n\n",
    "Who is the first character in the series to be called 'King in the North'?\n(a) Jon Snow\n(b) Ned Stark\n(c) Robb Stark\n(d) Edumure Tully\n\n",
    "What is the name of Arya's direwolf?\n(a) Nymeria\n(b) Lady\n(c) Grey Wind\n(d) Ghost\n\n"
]

questions = [
    GOTQuestion(quizPrompts[0], "b"),
    GOTQuestion(quizPrompts[1], "c"),
    GOTQuestion(quizPrompts[2], "a"),
]

def runQuiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("You got ", score , "/" , len(questions) , "correct!")

runQuiz(questions)