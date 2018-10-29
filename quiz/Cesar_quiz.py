def show_menu():
    print("1. Ask questions")
    print("2. Add question")
    print("3. Exit game")

    option = input("Enter option: ")
    return option


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

    score = 0

    print('this is the tuple {0}'.format(questions_and_answers))

    for question, answer in questions_and_answers:
        guess = input(question + '> ')
        if guess == answer:
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
            print('you selected /Exit game')
            break
        else:
            print('Invalid input')
        print('')


# game_loop()

ask_questions()