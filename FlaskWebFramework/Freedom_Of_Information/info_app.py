'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
####################################################################
# # File Name: info_app.py
# # Purpose : application configuration (Routing,attributes, main)
####################################################################

from flask import Flask, render_template , request
from Freedom_Of_Information.views import process_SSdata, process_COVIDdata, format_COVIDdata

import logging
import matplotlib
from Freedom_Of_Information.views.process_SSdata import ssForce

# creating a Flask object 
app = Flask(__name__)
app.config.from_object('config.DevConfig')

# Defining Global Constants
FLASK_ENV = app.config['FLASK_ENV']
DEBUG = app.config['DEBUG']
TESTING = app.config['TESTING']
TEMPLATES_AUTO_RELOAD = app.config["TEMPLATES_AUTO_RELOAD"]

####################################################################
# Routing details - URL routing seen on client browser
####################################################################


@app.route('/', methods=['POST', 'GET'])
def index():
    # routing for index => http://localhost:5000/
    logging.info('info_app -- executing index()')
    return render_template('index.html')


@app.route('/covid_search/', methods=['POST', 'GET'])
def covid_search():
    # routing for covid Search => http://localhost:5000/covid_search
    logging.info('info_app -- executing covid_search()')
    areaName_df = format_COVIDdata.get_area_list()
    return render_template('covid_search.html', areaName_df = areaName_df )


@app.route('/display_cases/' , methods=['POST', 'GET'])
def display_cases():
    # routing for displaying covid results => http://localhost:5000/display_cases
    logging.info('info_app -- executing display_cases()')
    
    logging.info('display_cases() Reading the month inputs from Form ')
    start = request.form['start']
    end = request.form['end']
    req_area = request.form.getlist('areas')
    
    logging.info('display_cases() -- calling the process function in process_COVIDdata')
    html_fname = process_COVIDdata.process(start , end, req_area)
    return render_template(html_fname, frm=start , to=end)


@app.route('/stop_and_search/', methods=['POST', 'GET'])
def stop_and_search():
    # routing for stop and search => http://localhost:5000/stop_and_search
    logging.info('info_app -- executing stop_and_search()')
    ssForce_obj = ssForce()
    ssForce_obj.get_forces_df()
    forces_df = ssForce_obj.force_df
    return render_template('stop_and_search.html',forces_df = forces_df)


@app.route('/display_plots/', methods=['POST', 'GET'])
def display_plots():
    # routing for displaying stop and search plots = http://localhost:5000/display_plots
    logging.info('info_app -- executing display_plots()')  
    
    logging.info('info_app -- Reading the date and force inputs from Form')
    date = request.form ["year"] + '-' + request.form ["month"]    
    selected_forces_idList = request.form.getlist("forces")
    
    logging.info('info_app -- Getting forces id and name details from API ')
    selected_forces_nameList = ssForce().get_filtered_flist(selected_forces_idList)
    #force = ssForce().get_force_list()
    
    logging.info('display_plots -- calling the process function in process_SSdata') 
    html_fname =process_SSdata.capture_process_data(date, selected_forces_idList)
    return render_template(html_fname , records_date=date , records_flist=selected_forces_nameList)


@app.after_request
def add_header(response):
    # clearing the cache after every request from the client browser before providing response
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'   
    response.headers['Expires'] = '0'
    logging.info('info_app() -- add_header() clearing the cache')
    return response

##############################################################################
# Main Application: Execution of FreedomOfSearch Application starts from here. 
##############################################################################


if(__name__ == "__main__"):
    
    # defining the log and application configurations 
    logging.basicConfig(filename='config/app.log', level=logging.INFO)
    logging.info('info_app -- executing main()')
    logging.info('info_app -- invoking server 127.0.0.1, port = 5000')
    matplotlib.use('Agg')
    app.run(debug=DEBUG)
    
