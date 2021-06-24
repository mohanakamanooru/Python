'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
########################################################
# # File Name: process_SSdata.py
# # Purpose : process Method (Data Capture)
#             get_dict Method (Data Processing)
#             generate_plots ( Data Visualization)
#########################################################

import logging
import requests

import matplotlib.pyplot as plt
import pandas as pd


class process_SSdata:
    
    ss_df = pd.DataFrame()
    
    def __init__(self, date, f_id_list):
        logging.info("process_SSdata -- __init__")
        self.date = date
        self.f_id_list = f_id_list

    def process(self):
        
        try:
            # for every selected area get the data from url and add .
            for force in self.f_id_list:
                url = 'https://data.police.uk/api/stops-force?force=' + force + '&date=' + self.date
                logging.info("process_SSdata -- The data is being fetched from  -- ", url)
                ss_req = requests.get(url)
                logging.info("process_SSdata -- process -- ss_req.status_code ", ss_req.status_code)  
        
                # if code is successful , then we generate the plots from fetched data 
                if ss_req.status_code == 200:
                    ss_data = ss_req.text
                    ss_force_df = pd.read_json(ss_data, orient='records')
                    if len(ss_data) < 1:
                        return [], 'no_records.html'
                    # adding force information to data frame in new column 
                    ss_force_df['force'] = force 
                    ss_force_df['force'] = ss_force_df['force'].astype(str)
                    self.ss_df = pd.concat([self.ss_df , ss_force_df]) 
                
                # if the server throws an error without providing any data
                elif ss_req.status_code == 500:
                    logging.info("Error Occurred from server side", ss_req.status_code)
                    return [], '500.html'
        
                # page not found error in unpredicted scenarios
                elif ss_req.status_code == 404:
                    logging.info("Error Occurred ", ss_req.status_code)
                    return [], '404.html'
                
            return self.ss_df , ''
        
        except Exception as e:
            logging.error("Exception raised ", e)
            return 'error.html'
        
    
class ssForce:
    
    force_df = pd.DataFrame()
    f_name_list = []
    url = ''
    
    def __init__(self):
        logging.info("ssForce --  __init__") 
        self.url = 'https://data.police.uk/api/forces'
        
    def get_forces_df(self):
        '''Returns forces data frame from API with two columns id and name 
        ''' 
        try: 
            force_req = requests.get(self.url)
            if(force_req.status_code == 200):
                force = force_req.text
                force_df = pd.read_json(force, orient='forces')        
            self.force_df = force_df
            # return self.force_df
        
        except Exception as e:
            logging.error(e)
            return 'error.html'
        
    def get_filtered_flist(self, f_id_list):
        '''Returns list of forces name for the user selected force id list
        '''
        logging.info("ssForce -- get_force_list")
        self.get_forces_df()
        # read the data frame from API
        result_df = self.force_df[self.force_df['id'].isin(f_id_list)]
        self.f_name_list = result_df['name']
        return self.f_name_list

    
class format_data:
    
    dframe = pd.DataFrame()
    
    def __init__(self, dframe):
        self.dframe = dframe
    
    def remove_none(self, dataframe):
        # remove none and null values 
        dataframe.mask(dataframe.astype(object).eq('None')).dropna()
        return dataframe


class generate_plots:
    
    df = pd.DataFrame()   
    # fig  = plt.figure(figsize=(10, 10))
    
    def __init__(self, df):
        self.df = df
        self.fig = plt.figure(figsize=(10, 10))
        # self.fig = plt.figure(constrained_layout=True, figsize=(10, 10))
        # self.spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=self.fig)
    
    def age_plot(self, dataframe , force_id_list):
        
        plt.close('all')
        age_fig = plt.figure(constrained_layout=True, figsize=(12, 5))
        age_fig.subplots_adjust(hspace=0.5)
        age_fig.tight_layout()
        age_fig.suptitle('Age Group')
        plt.axis('off')
        for i in range(0, len(force_id_list)):
            ax = 'age_ax' + str(i)
            pos = '1' + str(len(force_id_list)) + str(i + 1)
            
            # filter the data frame for specific force 
            age = {'age_range': dataframe['age_range'] , 'force': dataframe['force']}
            agedf = pd.DataFrame(age , columns=['age_range', 'force'])
            agedf = agedf[agedf['force'] == force_id_list[i]]
            agedf = agedf.dropna()
             
            agedf['search_count'] = 1
            agedf = agedf.groupby('age_range').sum()
            agedf.reset_index(inplace=True)
             
            ax = age_fig.add_subplot(pos) 
            ax.set_title(force_id_list[i])
            ax.pie(agedf['search_count'], labels=agedf['age_range'], autopct='%1.1f%%', shadow=False, startangle=90, pctdistance=0.85)
            ax = plt.gcf()
            ax.gca().add_artist(plt.Circle((0, 0), 0.70, fc='white'))
            
        plt.savefig('static/img/age_range.png')
    
    def gender_plot(self, dataframe, force_id_list):

        plt.close('all')
        gender_fig = plt.figure(constrained_layout=True, figsize=(12, 5))
        gender_fig.suptitle('Gender')
        gender_fig.tight_layout()
        gender_fig.subplots_adjust(hspace=0.5)
        plt.axis('off')
        
        for i in range(0, len(force_id_list)):
            ax = 'gender_ax' + str(i)
            pos = '1' + str(len(force_id_list)) + str(i + 1)
            
            # filter the data frame for specific force 
            gender = {'gender': dataframe['gender'] , 'force': dataframe['force']}
            genderdf = pd.DataFrame(gender , columns=['gender', 'force'])
            genderdf = genderdf[genderdf['force'] == force_id_list[i]]
            genderdf = genderdf.dropna()
             
            genderdf['search_count'] = 1
            genderdf = genderdf.groupby('gender').sum()
            genderdf.reset_index(inplace=True)
             
            ax = gender_fig.add_subplot(pos)
            ax.set_title(force_id_list[i]) 
            ax.pie(genderdf['search_count'], labels=genderdf['gender'], autopct='%1.1f%%', shadow=False, startangle=90, pctdistance=0.85)                                
            
        plt.savefig('static/img/gender.png')
    
    def ethnicity_plot(self, dataframe, force_id_list):
        
        plt.close('all')
        ethnicity_fig = plt.figure(constrained_layout=True, figsize=(12, 5))
        ethnicity_fig.suptitle('Ethnicity')
        ethnicity_fig.tight_layout()
        ethnicity_fig.subplots_adjust(hspace=0.5)
        plt.axis('off')
        
        for i in range(0, len(force_id_list)):
            ax = 'ethnicity_ax' + str(i)
            pos = '1' + str(len(force_id_list)) + str(i + 1)
            
            # filter the data frame for specific force 
            ethnicity = {'ethnicity': dataframe['officer_defined_ethnicity'] , 'force': dataframe['force']}
            ethnicitydf = pd.DataFrame(ethnicity , columns=['ethnicity', 'force'])
            ethnicitydf = ethnicitydf[ethnicitydf['force'] == force_id_list[i]]
            ethnicitydf = ethnicitydf.dropna()
             
            ethnicitydf['search_count'] = 1
            ethnicitydf = ethnicitydf.groupby('ethnicity').sum()
            ethnicitydf.reset_index(inplace=True)
            
            ax = ethnicity_fig.add_subplot(pos)
            ax.set_title(force_id_list[i]) 
            ax.bar(ethnicitydf['ethnicity'] , ethnicitydf['search_count'])
            plt.setp(ax.get_xticklabels(), rotation=45)
            
            total = sum(ethnicitydf['search_count'])
            for p in ax.patches: 
                x, y = p.get_xy() 
                ax.annotate('{:.0%}'.format(p.get_height() / total), (x, y + p.get_height() + 0.1))

        plt.savefig('static/img/ethnicity.png')
               
    def type_of_search_plot(self, dataframe, force_id_list):
        
        plt.close('all')
        type_fig = plt.figure(constrained_layout=True, figsize=(12, 5))
        type_fig.suptitle('Type Of Search')
        type_fig.subplots_adjust(hspace=0.5)
        type_fig.tight_layout()
        type_fig.tight_layout()
        plt.axis('off')
        
        for i in range(0, len(force_id_list)):
            ax = 'type_ax' + str(i)
            pos = '1' + str(len(force_id_list)) + str(i + 1)
            
            # filter the data frame for specific force 
            type_dict = {'type': dataframe['type'] , 'force': dataframe['force']}
            typedf = pd.DataFrame(type_dict , columns=['type', 'force'])
            typedf = typedf[typedf['force'] == force_id_list[i]]
            typedf = typedf.dropna()
             
            typedf['search_count'] = 1
            typedf = typedf.groupby('type').sum()
            typedf.reset_index(inplace=True)
            
            ax = type_fig.add_subplot(pos)
            ax.set_title(force_id_list[i]) 
            plt.setp(ax.get_xticklabels(), rotation=10 , fontsize=8)
            ax.bar(typedf['type'] , typedf['search_count'], color=['chocolate', 'limegreen', 'mediumslateblue'])
            
            total = sum(typedf['search_count'])
            for p in ax.patches: 
                x, y = p.get_xy() 
                ax.annotate('{:.0%}'.format(p.get_height() / total), (x, y + p.get_height() + 0.1))

        plt.savefig('static/img/type.png')
    
    def comparision_plot(self, dataframe, force_id_list):
        
        plt.close('all')
        dataframe['search_count'] = 1
        dataframe['date'] = dataframe['datetime'].dt.normalize()
        dataframe = dataframe.sort_values(['date'], ascending=True)
        
        cmp = { 'date': dataframe['date'] ,
                   'force': dataframe['force'],
                   'search_count': dataframe['search_count'] }
        all_forces_df = pd.DataFrame(cmp , columns=['date', 'force', 'search_count'])
        fig, ax = plt.subplots(figsize=(15, 5))
        fig.subplots_adjust(hspace=0.5)
        fig.suptitle('Daily Stop and Search cases recorded ')
        force_legend = []

        for force in force_id_list:
            cmp_df = all_forces_df[all_forces_df['force'] == force]
            cmp_df = cmp_df.groupby('date')['search_count'].count()
            if cmp_df.empty :
                continue
            cmp_df.plot(legend=True, ax=ax)
            force_legend.append(force)
        ax.legend(force_legend)
        plt.savefig('static/img/compare.png')
        

def capture_process_data(date, force_id_list):
    
    if(len(force_id_list) >=10):
        return 'incorrect_force.html'
    
    if not force_id_list:
        return 'incorrect_force.html' 
    
    ss_object = process_SSdata(date, force_id_list)
    dataframe , html_str = ss_object.process()
    
    if len(dataframe) < 1:
        if(html_str == 200):
            return 'no_records.html'
    
    if(html_str == ''):
        ss_plot_obj = generate_plots(dataframe)
        ss_plot_obj.age_plot(dataframe, force_id_list)
        ss_plot_obj.ethnicity_plot(dataframe, force_id_list)
        ss_plot_obj.gender_plot(dataframe, force_id_list)
        ss_plot_obj.type_of_search_plot(dataframe, force_id_list)
        ss_plot_obj.comparision_plot(dataframe, force_id_list)
        return 'display_plots.html'
    else:
        return html_str
