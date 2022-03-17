#testing if the class AnonumouSurvey properly saves responses in the list
#usingg assertIn() function

import unittest
from survey import AnonymousSurvey

class TestAnonymous(unittest.TestCase):
    def test_store_sigle_response(self):
        question = 'What language did you speak first?'
        my_survey = AnonymousSurvey(question)

        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)

if __name__ == '__main__':
    unittest.main()