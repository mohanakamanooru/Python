'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
#########################################################
# # File Name: test_info_app.py
# # Purpose : perform unit testing for info_app.py
#########################################################

import unittest

from Freedom_Of_Information.info_app import app 




class TestInfoApp(unittest.TestCase):
    
    # Initial setup -executed before each test
    def setUp(self):
        self.app = app.test_client()

    # Initial setup - executed after each test
    def tearDown(self):
        pass

    # test cases 
    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    def test_stop_and_search(self):
        response = self.app.get('/stop_and_search/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_covid_search(self):
        response = self.app.get('/covid_search/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
         
        
        
if __name__ == "__main__":    
    unittest.main()

