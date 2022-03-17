class Survey:
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def save_response(self,response):
        self.responses.append(response)
    
    def show_results(self):
        for response in self.responses:
            print(f'-{response}')