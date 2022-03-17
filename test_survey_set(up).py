#using setUp method to check if one response is properly stored
#and 3 responses are properly stored in class Survey

import unittest
from survey1 import Survey

class TestSurvey(unittest.TestCase):
    def setUp(self):
        question = 'What language did you speak firstly?'
        self.my_survey = Survey(question)
        self.responses = ['English','Spain','German']

    def test_one_response(self):
        self.my_survey.save_response(self.responses[2])
        self.assertIn(self.responses[2],self.my_survey.responses)

    def test_three_responses(self):
        for response in self.responses:
            self.my_survey.save_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()