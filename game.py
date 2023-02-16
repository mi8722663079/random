#!/bin/python
questions = ["what is the name of the longest river in the world ?",
             "what is the name of the highest mountain in the world ?",
             "what is number of axes of symmetry of triangle ?",
             "what is the sum of measures of angles in any triangle ?",
             "what is newton's third law ?",
             "measure of inscribed angle subtended by arc of measure 80 ?",
             "from what spieces is lion ?",
             "who founded the principles of the law of gravity ?",
             "what is the total measures of angles serrounding one point ?",
             "what is the number of medians in any triangle ?"]
game = True
score = 0
currentQuestion = 0
while game:
    print("your score is :", score)
    if score < 0:
        print("\n" + "YOU LOSE")
        game = False
    if currentQuestion >= 10:
        print("Game Finished")
        game = False
    elif score >= 0:
        print(questions[currentQuestion] + '\n')
        answers = ["a", "b", "c", "d", "e", "f", "g", "h" "i", "j"]
        inputfromUser = input("The answer is :")
        if inputfromUser == answers[currentQuestion]:
            score += 1
        else:
            score -= 1
        currentQuestion += 1
# good Youtubers to watch :
# liveoverflow, theprimagen, codeAeshtitics, fireshipio
