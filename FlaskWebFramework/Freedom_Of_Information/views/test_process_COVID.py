'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
#########################################################
# # File Name: test_process_COVIDdata.py
# # Purpose : perform unit testing for process_COVIDdata.py
#########################################################

import unittest

from Freedom_Of_Information.views import process_COVIDdata


class TestProcess_COVIDdata(unittest.TestCase):
    
    
    def test_get_force(self):
        
        # dates - start date later than end date 
        self.assertEqual(process_COVIDdata.process('2020-11-01', '2020-09-01', "['Hampshire','Rutland']"),"incorrect_input.html")
        
        # passing incorrect area name
        self.assertEqual(process_COVIDdata.process('2020-10-01', '2020-11-01', "['Hamp','Rutld']"),"error.html")
         
     
        
if __name__ == "__main__":    
    unittest.main()