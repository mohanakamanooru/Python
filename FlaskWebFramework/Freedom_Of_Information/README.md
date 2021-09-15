# Project Name : Freedom Of Information

	Assessment 		:Software for Digital Innovation ICA-2 
	Author			:Mohana Kamanooru 
	Email			:A0223038@live.tees.ac.uk
	Purpose 		:Application Overview , 
							Requirements ,
							Project folder structure, 
							File names and purpose,
							Instructions to Run application , 
							Testing Instructions, 
							Visualisation Plots and details
	


# Application Overview: 
-----------------------
	The project Freedom Of Information is developed using Flask web framework . As per the given requirements mentioned in ICA2 specification document,
	application enables user to access information quicker from two different APIs and aids to visualise BIG Data graphically.
	Hence, improves the user's ability to draw information form the hugely available data. 
	
	1. Covid Search 	- processes the covid cases information from given csv file and provides different plots to visualise.
	 						Capture Data 		: process_COVIDdata.py (reads data from csv and generates plots using aggregations and other libraries)
	 						Pre-process Data 	: format_COVIDdata.py	( Formats the data types,columns and returns data ready to be visualised)
	 						Visualise the Data	: display_cases.html ( displays the respective plots for the user given inputs )
	2. Stop and Search- processes the stop and search by force information from API and presents graphical data using various python libraries
	 						Capture Data 		: process_SSdata.py (gets the data as json object from API and processes it to provide Plots to user.)
	 						Pre-process Data 	: process_SSdata.py	( Formats the data types,columns , matplotlib, pandas and other libraries)
	 						Visualise the Data	: display_plots.html ( displays the respective plots for the user given inputs )
	
# Requirements :
----------------
	Installation details
	Packages/Libraries
	1. Python version 3.8.3 
		https://www.python.org/downloads/release/python-383/
	2. Flask 1.1.2
		https://pypi.org/project/Flask/
	3. Jinja2
		https://pypi.org/project/Jinja2/
	4. Pandas 1.1.4
		https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
	5. Matlplotlib 3.3.3
		https://pypi.org/project/matplotlib/
	6. Unittest 2 1.1.0
		https://pypi.org/project/unittest2/
		
		pip install Flask
		pip install Jinja2
		pip install pandas
		pip install matplotlib
		pip install requests
		

	IDE 
	1. Eclipse IDE for Eclipse Committers (includes Incubating components)
		Version: 2020-09 (4.17.0)
		Build id: 20200910-1200 
		https://www.eclipse.org/downloads/packages/release/2020-03/r/eclipse-ide-eclipse-committers
		


# Project Folder Structure :
----------------------------

	Application folder structure is provided in the structure.txt document under Folder Structure Section.



# File Names and Purpose 
-------------------------

	1. info_app.py		:	Application starts execution form this file. main method is mentioned and it defines application configuration (Routing, attributes, main)
	2. app_error.py		:	Application error configuration (error handlers 404,500 )
	3. config.py		:	Configuration details - Development , testing and Production environment Environment
	4. requirements.txt	:	Provides steps for Installation of modules and libraries.  Source Folder structure Details.
	5. app.log		:	Application log file. Auto saves the application log for debugging and monitoring purposes.
	6. specimenDate_ageDemographic-unstacked.csv Raw :	Data file from gov website with COVID cases details 
	7. main.css		:	Contains the style code for all the application html files.
	8. static/images	:	All the app images are stored in this location.		
									1. error.png
									2. norecords.png
									3. server_error.jpg
									4. uni_logo.jpg
	9. HTML Files		:	Application html files which serves as UI for the entire application.
									1.index.html 		-- main web page from where user can access the entire application.
									2. covid_search.html 	-- Pages allowing user to select covid cases to analyse
									3. display_cases.html 	-- web page with covid case plots and results
									4. stop_and_search.html -- web page allowing user to provide inputs to initiate the stop and search by force.
									5. display_plots.html 	-- web page with plots and results for selected stop and search force
									6. base.html 		-- contains the header and footers of the application front end.
									7. error.html 		-- shows up when exception or unknown error occurs
									8. incorrect_input.html -- Web page shown when user input is incorrect
									9. no_records.html 	-- when the HTTP request is successful but there is no information in database.
									10. 404.html 		-- shows up during page not found error
									11. 500.html 		-- shows up when server error.
									12. incorrect_force.html -- informs user that force filed is mandatory and cannot be balnk.
	10.format_COVIDdata.py	:	Pre-processes the data add/rename columns and returns a dtaframe
	11.process_COVIDdata.py	:	Process the data and calls appropriate methods to plot graphs
	12.process_SSdata.py	:	Processes the stop and search by force data and generates the plots.
	13.test_process_COVID.py:	Provides various unit test cases for process_COVIDdata.py
	14.test_process_SSdata.py:	Provides unit test cases for stop and search data by force
	15.test_info_app.py		: Contains the test cases for info_app.py file , it imports unittest from python unittest framework. 
	
# Instructions to run Application
		After the successful installations mentioned earlier , follow the below steps. 
		1. Import the provided source code into the eclipse workspace . Please refer to the folder structure mentioned in requirements.txt file.
		2. Run info_app.py as Python Run Config under the root folder of the imported project. When this is completed , flask server will be up and running in local environment. 
		3. Open the browser and enter the url - http://localhost:5000/ , it displays the home/index page of the application.  

# Testing :
	To test the application, run the test cases provided in test_info_app.py,test_process_COVID.py and test_process_SSdata.py files. 
	1. Open the mentioned test file and run as python unit test configuration.
	2. Console provides the test results in eclipse IDE .

# Visualization : 

	COVID Cases - Plots :
			1.Daily Covid Cases - bar plot between input date range and total cases in the period
			2.Weekly Covid Cases - line graph between weekly data (daily data agg by mean) and the total number of cases.  
			3.Monthly Covid Cases - line plot showing trend of total covid cases for selected months (blank is selected period is less than a month )
			4.Age group Covid Cases - pie plot showing percentage of people below60 and above tested positive for COVID
			5.Covid Cases in Selected Areas - This plot is line graph between date range and different selected areas. 
				(plotted if user has chosen areas to analyse , if not data is analysed for all areas "Covid Cases By Region".) 
			6.Covid Cases Highly Affected Areas - shows the top 10 highly affected areas (i.e. with highest number of cases)
			7.Covid Cases by Age - Bar chart showing the number of cases from each age group(for every 5 years)
			
	Stop and Search - Plots:
			1.Daily Search data - Shows line graph to compare the daily stop and search across different areas.
			2.Age Group - donut chart showing the Age group and respective percentages of people searched.
			3.Ethnicity - Bar plot showing the ethnicity of people who were searched by police.
			4.Type of Search - Bar graph showing the figures for category of search, vehicle/person search or both.
			5.Gender - pie plot showing percentage of men,women and other searched by the force.
			































