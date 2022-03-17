from survey1 import Survey
question = 'What language did you first learn to speak?'
my_survey = Survey(question)

my_survey.show_question()

print('Enter q any time to finish.')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    else:
        my_survey.save_response(response)
    my_survey.show_question()

print()
print('The answers are following: ')
my_survey.show_results()
