question1 = "what is the name of the longest river in the world ?"
question2 = "what is the name of the highest mountain in the world ?"
question3 = "what is number of axes of symmetry of triangle ?"
question4 = "what is the sum of measures of angles in any triangle ?"
question5 = "what is newton's third law ?"
question6 = "measure of inscribed angle subtended by arc of measure 80 ?"
question7 = "from what spieces is lion ?"
question8 = "who founded the principles of the law of gravity ?"
question9 = "what is the total measures of angles serrounding one point ?"
question10 = "what is the number of medians in any triangle ?"
game = True
score = 0
while game:
    if score < 0 :
        print("\n" +"YOU LOSE")
        game = False
    if score == 0:
        print(question1)
        print('\n')
        input1=input('the answer is: ')
        if input1 == "the nile":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question2)
            print('\n')
            input2=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question2)
            print('\n')
            input2=input('the answer is: ')
            if score < 0 :
                game = False

        if input2 == "everest":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question3)
            print('\n')
            input3=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question3)
            print('\n')
            input3=input('the answer is: ')
            if score < 0 :
                game = False
        
        if input3 == "3" or input3 == "three":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question4)
            print('\n')
            input4=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question4)
            print('\n')
            input4=input('the answer is: ')
            if score < 0 :
                game = False

        if input4 == "180" or input4 == "hundred and eighty" or input4 == "one hundred and eighty" or input4 == "180 degree":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question5)
            print('\n')
            input5=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question5)
            print('\n')
            input5=input('the answer is: ')
            if score < 0 :
                game = False

        if input5 == "every action has a reaction" or input5 == "reaction law":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question6)
            print('\n')
            input6=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question6)
            print('\n')
            input6=input('the answer is: ')
            if score < 0 :
                game = False

        if input6 == "40" or input6 == "40 degree":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question7)
            print('\n')
            input7=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question7)
            print('\n')
            input7=input('the answer is: ')
            if score < 0 :
                game = False

        if input7 == "cats" or input7 == "cat species":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question8)
            print('\n')
            input8=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question8)
            print('\n')
            input8=input('the answer is: ')
            if score < 0 :
                game = False

        if input8 == "newton" or input8 == "isaac newton":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question9)
            print('\n')
            input9=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question9)
            print('\n')
            input9=input('the answer is: ')
            if score < 0 :
                game = False

        if input9 == "360" or input9 == "360 degree" or input9 == "three hundred and sixty degree" or input9 == "three hundred and sixty":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print(question10)
            print('\n')
            input10=input('the answer is: ')
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            print(question10)
            print('\n')
            input10=input('the answer is: ')
            if score < 0 :
                game = False

        if input10 == "3" or input10 == "three":
            print('true')
            score += 1
            print('your score is '+ str(score))
            print('\n' + "YOU WIN")
            game = False
        else:
            print('false')
            score -= 1
            print("\n"+"your score is " + str(score))
            game = False
            







    


