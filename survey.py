class AnonymousSurvey:
    #Collect anonymous answer to survey question.
    def __init__(self,question):
        #Store a question and prepare to store responses
        self.question = question
        self.responses = []

    #Show the question
    def show_question(self):
        print(self.question)

    def store_response(self,response):
        #store single response to the survey
        self.responses.append(response)
        self.responses.append('Spain')

    def show_results(self):
        for response in self.responses:
            print(f'-{response}')
