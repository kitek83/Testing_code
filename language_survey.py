from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)
#show the question
my_survey.show_question()
print("Enter 'q' any time to quit.")

while True:
    lang = input('Language: ')
    if lang == 'q':
        break
    else:
        my_survey.store_response(lang)
    my_survey.show_question()

print('Thank You!')
my_survey.show_results()