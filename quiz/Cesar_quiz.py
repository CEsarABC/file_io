import random

def show_menu():
    print("1. Ask questions")
    print("2. Add question")
    print("3. Delete a question")
    print("4. Exit game")

    option = input("Enter option: ")
    return option


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


def add_question():
    print('')
    question = input('Enter a question\n ')

    print('')
    print('Tell me the answer')
    answer = input('{0}\n> '.format(question))

    file = open('questions.txt', 'a')
    file.write(question + '\n')
    file.write(answer + '\n')
    file.close()


def delete_a_question():
    print(questions)
    print('Which question would you like to erase??')
    print('from 0 to', + len(zipList)-1)
    option_delete = int(input('>'))
    if option_delete == 0:
        questions.pop(0)
        answers.pop(0)
    elif option_delete == 1:
        questions.pop(1)
        answers.pop(1)
    elif option_delete == 2:
        questions.pop(2)
        answers.pop(2)
    else:
        print('not a choice')
    print(questions)

def game_loop():
    while True:
        option = show_menu()
        if option == '1':
            print('You selected /ask questions')
            ask_questions()
        elif option == '2':
            print('You selected /add a question')
            add_question()
        elif option == '3':
            print('You selected /Delete a question')
            delete_a_question()
        elif option == '4':
            print('you selected /Exit game')
            break
        else:
            print('Invalid input')
        print('')


game_loop()

