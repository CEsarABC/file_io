
# function to show menu and ask for input
def show_menu():
    print("1. Ask questions")
    print("2. Add question")
    print("3. Exit game")

    option = input("Enter option: ")
    return option

# function to ask questions
def ask_questions():
    questions = []      # creating an array to fill up with questions
    answers = []        # creating an array to fill up with answers

    with open('questions.txt', 'r') as file:    # with opens and closes the document automatically
        lines = file.read().splitlines()        # creates a variable to store the splitlines after reading

    for i, text in enumerate(lines):    # creating a loop with 2 variables and uses the enumerate function to count
        if i % 2 == 0:                  # the number of lines, and if the line is even add the test to questions
            questions.append(text)      # if the line is odd add the text to answers
        else:
            answers.append(text)

    number_of_questions = len(questions)                # the variable is created to count the number of questions
    questions_and_answers = zip(questions, answers)     # creates tuples were question and answer are grouped together

    score = 0                       # crates a score variable to use later on

    for question, answer in questions_and_answers:      # compares if the question and the answer are in the tuple
        guess = input(question + '> ')                  # created previously
        if guess == answer:                         # if the match score will add 1 every time they match
            score += 1
            print('Right!')
        else:                                       # if they don't match it does not add
            print('Wrong!')
        # finally prints a message where brings the format to show the variables for score and  number_of_questions
        print('You got {0} correct out of {1}\n'.format(score, number_of_questions))


def add_question():
    print('')
    question = input('Enter a question\n ')     # question variable stores the string

    print('')
    print('Tell me the answer')
    answer = input('{0}\n> '.format(question))  # answer variable stores the answer

    file = open('questions.txt', 'a')           # we open the file to append the question with a line break to separate
    file.write(question + '\n')                 # the inputs as many times as we open the document
    file.write(answer + '\n')
    file.close()


def game_loop():                                # we create the game loop to use our functions
    while True:
        option = show_menu()                        # we create our option variable which is equal to the return
        if option == '1':
            print('You selected /ask questions')    # then cases follow and functions come to play
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


game_loop()             # plays the function containing the functions