'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
################################################################
# # File Name: process_COVIDdata.py
# # Purpose(methods) : process         --- (Data Capture)
#                      get_cases_plot  --- (Data Visualization)
#################################################################

from datetime import datetime
import logging

from matplotlib import gridspec

from Freedom_Of_Information.views import format_COVIDdata
import matplotlib.pyplot as plt
import pandas as pd


def process(start , end, req_area):
    ''' Returns subset of dataframe between the mentioned months
    
    This method returns the filtered data frame . 
    Cases information only between the frm and to months
    '''
    logging.info("process_COVIDdata -- executing process()")
    
    try:
        # type casting start and end dates to datetime 
        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')
        
        # if the start date is after the end date then throws error.
        if (start_date < end_date):
            # get the data frame and filtering as per input dates
            df = format_COVIDdata.get_dataframe()
            filtered_df = df[df['date'] >= start_date]
            filtered_df = filtered_df[filtered_df['date'] <= end_date]
        else:
            logging.info("process_COVIDdata -- process() -- Incorrect input data")
            return 'incorrect_input.html'
        
        if (len(req_area) > 0):
            # if input requested areas are  selected then replace special chars
            for ind in range(0, len(req_area)):
                req_area[ind] = req_area[ind].replace("&nbsp;" , " ")
                req_area[ind] = req_area[ind].replace("&amp;", "&")
            print(req_area)
            filtered_df = filtered_df[filtered_df['areaName'].isin(req_area)]
            filtered_df.info(verbose=True)
                        
        logging.info("process_COVIDdata -- calling get_cases_plot()")
        get_cases_plot(filtered_df, req_area)
        return 'display_cases.html'
    
    except Exception as e:
        logging.info("process_COVIDdata -- process -- Error ", e)
        return 'error.html'


def get_cases_plot(df, req_area):
    
    logging.info("process_COVIDdata -- executing get_cases_plot(df) ")
    
    # cases by date - date and total cases
    cases_date = { 'date': df['date'] , 'cases': df['total-cases']}
    cases_date_df = pd.DataFrame(cases_date , columns=['date', 'cases']) 
    
    cases_mean = { 'date': df['date'] , 'cases': df['total-cases']}
    cases_mean_df = pd.DataFrame(cases_mean , columns=['date', 'cases'])
    cases_mean_df['cases'] = cases_mean_df['cases'].rolling(7).mean()
    cases_mean_df.reset_index(inplace=True)
    
    # Weekly Cases Average  
    weekly_df = cases_date_df.resample('W', on='date').mean()
    weekly_df.reset_index(inplace=True)
    weekly_df.info(verbose=True)
    
    # Monthly Cases Average 
    monthly_df = cases_date_df.resample('M', on='date').mean()
    monthly_df.reset_index(inplace=True)
    monthly_df.info(verbose=True)
    
    # Cases by Region
    region_df = df[df['areaType'] == 'region']    
    cases_region = {'areaName': region_df['areaName'], 'cases': region_df['total-cases'] }
    cases_region_df = pd.DataFrame(cases_region , columns=['areaName', 'cases'])
    cases_region_df['areaName'] = cases_region_df['areaName'].astype(str)
    cases_region_df = cases_region_df.groupby(['areaName']).sum()
    cases_region_df.reset_index(inplace=True)
    
    # Cases in Nation
    nation_df = df[df['areaType'] == 'nation']    
    cases_nation = {'areaName': nation_df['areaName'], 'cases': nation_df['total-cases'] }
    cases_nation_df = pd.DataFrame(cases_nation , columns=['areaName', 'cases'])
    cases_nation_df['areaName'] = cases_nation_df['areaName'].astype(str)
    
    # Cases in UnitedKingdom
    unitedK_df = df[df['areaType'] == 'overview']    
    cases_unitedK = {'areaName': unitedK_df['areaName'], 'cases': unitedK_df['total-cases'] }
    cases_unitedK_df = pd.DataFrame(cases_unitedK , columns=['areaName', 'cases'])
    cases_unitedK_df['areaName'] = cases_unitedK_df['areaName'].astype(str)
    
    # Cases By areaName
    area_df = df[df['areaType'] == 'ltla'] 
    areaName = { 'areaName': area_df['areaName'] , 'cases': area_df['total-cases']}    
    areaName_df = pd.DataFrame(areaName , columns=['areaName', 'cases'])
    areaName_df['areaName'] = areaName_df['areaName'].astype(str)    
    areaName_df = areaName_df.groupby('areaName').sum()
    areaName_df.reset_index(inplace=True)
    areaName_df_highest10 = areaName_df.sort_values('cases', ascending=False).head(10)
    
    # cases by age group
    ageGroup = { 'below60': df['Age-below60'].sum() ,
                'above60':df['Age-above60'].sum() }  # ,'above90' :df['Age-above90'].sum() ,'unassigned' :df['Age-unassigned'].sum()}    
    ageblock = {"Age0_4": df["Age0-4"].sum(),
               "Age5_9": df["Age05-09"].sum(),
               'Age10_14': df["Age10-14"].sum(),
               'Age15_19': df["Age15-19"].sum(),
               "Age20_24": df["Age20-24"].sum(),
               "Age25_29": df["Age25-29"].sum(),
               "Age30_34": df["Age30-34"].sum(),
               "Age35_39": df["Age35-39"].sum(),
               "Age40_44": df["Age40-44"].sum(),
               "Age45_49": df["Age45-49"].sum(),
               "Age50_54": df["Age50-54"].sum(),
               "Age55_59": df["Age55-59"].sum(),
               "Age60_64": df["Age60-64"].sum(),
               "Age65_69": df["Age65-69"].sum(),
               "Age70_74": df["Age70-74"].sum(),
               "Age75_79": df["Age75-79"].sum(),
               "Age80_84": df["Age80-84"].sum(),
               "Age85_89": df["Age85-89"].sum(),
                }  # "unassigned" : df["Age-unassigned"].sum(),}

    # Plotting the graphs
    logging.info("process_COVIDdata -- get_cases_plot - plotting the graphs") 
    fig1 = plt.figure(constrained_layout=True, figsize=(10, 10))
    fig1.tight_layout()
    fig1.subplots_adjust(hspace=0.5)
    spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig1)
     
    fig1_ax1 = fig1.add_subplot(spec2[0, 0])
    fig1_ax1.bar(cases_date_df['date'], cases_date_df['cases'])
    plt.setp(fig1_ax1.get_xticklabels(), rotation=90)
    fig1_ax1.set_title("Daily Covid Cases")        
     
    fig1_ax2 = fig1.add_subplot(spec2[0, 1])
    fig1_ax2.plot(weekly_df['date'] , weekly_df['cases'])
    plt.setp(fig1_ax2.get_xticklabels(), rotation=90)
    fig1_ax2.set_title("Weekly Covid Cases")
     
    fig1_ax3 = fig1.add_subplot(spec2[1, 0])
    fig1_ax3.plot(monthly_df['date'] , monthly_df['cases'])
    plt.setp(fig1_ax3.get_xticklabels(), rotation=90)
    fig1_ax3.set_title("Monthly Covid Cases")

    fig1_ax4 = fig1.add_subplot(spec2[1, 1])
    fig1_ax4.set_title("Age group Covid Cases")
    fig1_ax4.pie(ageGroup.values() , labels=ageGroup.keys() , autopct='%1.1f%%', startangle=90)
    fig1_ax4 = plt.gcf()
    fig1_ax4.gca().add_artist(plt.Circle((0, 0), 0.70, fc='white'))
    
    plt.savefig('static/img/covid_date.png')    
    plt.cla()
    plt.clf()
    plt.close()
    
    fig2 = plt.figure(constrained_layout=True, figsize=(10, 20))
    fig2.subplots_adjust(hspace=0.5)
    fig2.tight_layout()
    spec = gridspec.GridSpec(ncols=1, nrows=3, figure=fig2)
    
    fig2_ax1 = fig2.add_subplot(spec[0, 0])
    plt.setp(fig2_ax1.get_xticklabels(), rotation=45)
    
    if(len(req_area) > 1):
        fig2_ax1.set_title(" Covid Cases in Selected Areas")
        df = df.sort_values(['date'], ascending=True)
        df.set_index('date', inplace=True)
        newdf = df.groupby('areaName')['total-cases']
        newdf.plot(legend=True)
                
    else: 
        fig2_ax1.bar(cases_region_df['areaName'], cases_region_df['cases'])
        fig2_ax1.set_title(" Covid Cases By Region")
    
    fig2_ax2 = fig2.add_subplot(spec[1, 0])
    fig2_ax2.bar(areaName_df_highest10['areaName'] , areaName_df_highest10['cases'])
    plt.setp(fig2_ax2.get_xticklabels(), rotation=45)
    fig2_ax2.set_title("Covid Cases Highly Affected Areas")
    
    fig2_ax3 = fig2.add_subplot(spec[2, 0])
    fig2_ax3.bar(ageblock.keys() , ageblock.values())
    plt.setp(fig2_ax3.get_xticklabels(), rotation=45)
    fig2_ax3.set_title("Covid Cases by Age")   
    
    plt.savefig('static/img/covid_region.png')
    plt.cla()
    plt.clf()
    plt.close()   
    
    logging.info("process_COVIDdata -- exiting get_cases_plot()")
    return
    
