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

def ask_questions():
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

    score = 0

    for question, answer in zipList:
        print(zipList)
        guess = input(question + '> ')
        if guess == answer:
            print('Right!')
        else:
            print('Wrong!')
        print('You got {0} correct out of {1}\n'.format(score, number_of_questions))


ask_questions()