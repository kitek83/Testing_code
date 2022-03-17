#checking if 3 responses are properly stored in class Survey
import unittest
from survey1 import Survey

class TestSurvey1(unittest.TestCase):
    def test_store_three_responses(self):
        question = 'What language did you speak first: '
        my_survey = Survey(question)
        responses = ['English','Spain','German']

        for response in responses:
            my_survey.save_response(response)

        for response in responses:
            self.assertIn(response,my_survey.responses)

if __name__ == '__main__':
    unittest.main()