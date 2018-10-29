import random
array = [1,2,3,4,5]
tuple = [(1,1),(2,2),(3,3)]

print(type(tuple))

tuple1 = ('banana', 'apple', 'pear', 'banana')

print(type(tuple1))
print(len(tuple1))
print(tuple1[2])
print(tuple1.index('banana'))
print(tuple1.count('banana'))
print(tuple1)

print(random.choice(tuple1))

foo = ['battery', 'correct', 'horse', 'staple']
secure_random = random.SystemRandom()
print(secure_random.choice(foo))
print(foo)
foo.pop(2)
print(foo)

questions = []
answers = []

with open('questions.txt', 'r') as file:
        lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        questions.append(text)
    else:
        answers.append(text)

number_of_questions = len(questions)
questions_and_answers = zip(questions, answers)
zipList = list(questions_and_answers)
random.shuffle(zipList)


def ask_questions():
    score = 0
    for question, answer in zipList:
        guess = input(question + '> ')
        if guess == answer:
            score += 1
            print('Right!')
        else:
            print('Wrong!')
        print('You got {0} correct out of {1}\n'.format(score, number_of_questions))


def delete_a_question():
    print(zipList)
    print('Which question would you like to erase??')
    print('from 0 to', + len(zipList)-1)
    option_delete = int(input('>'))
    if option_delete == 0:
        zipList.pop(0)
    elif option_delete == 1:
        zipList.pop(1)
    elif option_delete == 2:
        zipList.pop(2)
    else:
        print('not a choice')


    print(zipList)
    print(option_delete)


#ask_questions()
delete_a_question()

def deleting():
    zipList.pop(0)
    print(zipList)


#deleting()