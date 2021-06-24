'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
#########################################################
# # File Name: test_process_SSdata.py
# # Purpose : perform unit testing for process_SSdata.py
#########################################################

import unittest

from Freedom_Of_Information.views import process_SSdata
from Freedom_Of_Information.views.process_SSdata import ssForce


class TestProcess_SSdata(unittest.TestCase):
    
    def test_get_filtered_flist(self):
        ssForce_obj = ssForce()
        ssForce_obj.get_forces_df()         
        fdict = ssForce_obj.get_filtered_flist(["cleveland"])
        self.assertEqual(fdict.values[0], "Cleveland Police")
    
    def test_process(self):
        process_obj = process_SSdata.process_SSdata('2020-11', ['cleveland'])
        process_obj.process()
        self.assertEqual(len(process_obj.ss_df), 592)
        process_obj = process_SSdata.process_SSdata('2020-09', ['cleveland'])
        process_obj.process()
        self.assertEqual(len(process_obj.ss_df), 416)
        process_obj = process_SSdata.process_SSdata('2020-12', ['cleveland'])
        process_obj.process()
        self.assertEqual(len(process_obj.ss_df), 0)


    def test_get_forces_df(self):
        ssForce_obj = ssForce()
        ssForce_obj.get_forces_df()
        self.assertEqual(ssForce_obj.force_df.size, 88)
            
        
if __name__ == "__main__": 
    unittest.main()
    
