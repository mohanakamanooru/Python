'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
####################################################################
# # File Name: app_error.py
# # Purpose : application error configuration (error handlers)
####################################################################

from flask import render_template
from Freedom_Of_Information.info_app import app


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

