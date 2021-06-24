'''
Module : Software for Digital Innovation 
Assessment : ICA-2 (Freedom Of Information)
Project Name : Freedom Of Information

@author: Mohana Kamanooru
email : A0223038@live.tees.ac.uk
'''
########################################################################
# # File Name: format_data.py
# # Purpose  : format_data(class)  --- (Data Capture/pre-processing)
#              get_dataframe, get_area_list  --- (Data processing)
#########################################################################
import pandas as pd


class format_data:
    
    df = ""
    
    def __init__(self):
        df = pd.read_csv("source/data/covid/specimenDate_ageDemographic-unstacked.csv")
        # df = pd.read_csv("../source/data/covid/modified.csv")
        # df.info(verbose=True)
        self.df = df
        
    def get_dataframe(self):
        # self.df.info(verbose=True)
        return self.df
    
    def add_total_column(self):
        self.df['total-cases'] = self.df['Age-below60'] + self.df['Age-above60'] + self.df['Age-above90'] + self.df['Age-unassigned']
        return self.df
        
    def rename_cols(self):
        self.df.rename(columns={"newCasesBySpecimenDate-0_4": "Age0-4",
                        "newCasesBySpecimenDate-0_59": "Age-below60",
                        "newCasesBySpecimenDate-10_14": "Age10-14",
                        "newCasesBySpecimenDate-15_19": "Age15-19",
                        "newCasesBySpecimenDate-20_24": "Age20-24",
                        "newCasesBySpecimenDate-25_29": "Age25-29",
                        "newCasesBySpecimenDate-30_34": "Age30-34",
                        "newCasesBySpecimenDate-35_39": "Age35-39",
                        "newCasesBySpecimenDate-40_44": "Age40-44",
                        "newCasesBySpecimenDate-45_49": "Age45-49",
                        "newCasesBySpecimenDate-50_54": "Age50-54",
                        "newCasesBySpecimenDate-55_59": "Age55-59",
                        "newCasesBySpecimenDate-5_9": "Age05-09",
                        "newCasesBySpecimenDate-60+": "Age-above60",
                        "newCasesBySpecimenDate-60_64": "Age60-64",
                        "newCasesBySpecimenDate-65_69": "Age65-69",
                        "newCasesBySpecimenDate-70_74": "Age70-74",
                        "newCasesBySpecimenDate-75_79": "Age75-79",
                        "newCasesBySpecimenDate-80_84": "Age80-84",
                        "newCasesBySpecimenDate-85_89": "Age85-89",
                        "newCasesBySpecimenDate-90+": "Age-above90",
                        "newCasesBySpecimenDate-unassigned": "Age-unassigned",
                        
                        "newCasesBySpecimenDateRollingSum-0_4": "Sum0-4",
                        "newCasesBySpecimenDateRollingSum-0_59": "Sum-below60",
                        "newCasesBySpecimenDateRollingSum-10_14": "Sum10-14",
                        "newCasesBySpecimenDateRollingSum-15_19": "Sum15-19",
                        "newCasesBySpecimenDateRollingSum-20_24": "Sum20-24",
                        "newCasesBySpecimenDateRollingSum-25_29": "Sum25-29",
                        "newCasesBySpecimenDateRollingSum-30_34": "Sum30-34",
                        "newCasesBySpecimenDateRollingSum-35_39": "Sum35-39",
                        "newCasesBySpecimenDateRollingSum-40_44": "Sum40-44",
                        "newCasesBySpecimenDateRollingSum-45_49": "Sum45-49",
                        "newCasesBySpecimenDateRollingSum-50_54": "Sum50-54",
                        "newCasesBySpecimenDateRollingSum-55_59": "Sum55-59",
                        "newCasesBySpecimenDateRollingSum-5_9": "Sum05-09",
                        "newCasesBySpecimenDateRollingSum-60+": "Sum-above60",
                        "newCasesBySpecimenDateRollingSum-60_64": "Sum60-64",
                        "newCasesBySpecimenDateRollingSum-65_69": "Sum65-69",
                        "newCasesBySpecimenDateRollingSum-70_74": "Sum70-74",
                        "newCasesBySpecimenDateRollingSum-75_79": "Sum75-79",
                        "newCasesBySpecimenDateRollingSum-80_84": "Sum80-84",
                        "newCasesBySpecimenDateRollingSum-85_89": "Sum85-89",
                        "newCasesBySpecimenDateRollingSum-90+": "Sum-above90",
                        "newCasesBySpecimenDateRollingSum-unassigned": "Sum-unassigned" ,
                        
                        "newCasesBySpecimenDateRollingRate-0_4": "Rate0-4",
                        "newCasesBySpecimenDateRollingRate-0_59": "Rate-below60",
                        "newCasesBySpecimenDateRollingRate-10_14": "Rate10-14",
                        "newCasesBySpecimenDateRollingRate-15_19": "Rate15-19",
                        "newCasesBySpecimenDateRollingRate-20_24": "Rate20-24",
                        "newCasesBySpecimenDateRollingRate-25_29": "Rate25-29",
                        "newCasesBySpecimenDateRollingRate-30_34": "Rate30-34",
                        "newCasesBySpecimenDateRollingRate-35_39": "Rate35-39",
                        "newCasesBySpecimenDateRollingRate-40_44": "Rate40-44",
                        "newCasesBySpecimenDateRollingRate-45_49": "Rate45-49",
                        "newCasesBySpecimenDateRollingRate-50_54": "Rate50-54",
                        "newCasesBySpecimenDateRollingRate-55_59": "Rate55-59",
                        "newCasesBySpecimenDateRollingRate-5_9": "Rate05-09",
                        "newCasesBySpecimenDateRollingRate-60+": "Rate-above60",
                        "newCasesBySpecimenDateRollingRate-60_64": "Rate60-64",
                        "newCasesBySpecimenDateRollingRate-65_69": "Rate65-69",
                        "newCasesBySpecimenDateRollingRate-70_74": "Rate70-74",
                        "newCasesBySpecimenDateRollingRate-75_79": "Rate75-79",
                        "newCasesBySpecimenDateRollingRate-80_84": "Rate80-84",
                        "newCasesBySpecimenDateRollingRate-85_89": "Rate85-89",
                        "newCasesBySpecimenDateRollingRate-90+": "Rate-above90",
                        "newCasesBySpecimenDateRollingRate-unassigned": "Rate-unassigned"}, inplace=True)
    
    def format_date(self):
        # Converting datatype  of date field to datetime64[ns]
        # self.df['date'] = DatetimeIndex(self.df['date'], dtype='datetime64[ns]', freq=None)
        self.df['date'] = pd.to_datetime(self.df['date'])
        

def get_dataframe():
    fmt = format_data()
    fmt.format_date()
    fmt.rename_cols()
    fmt.add_total_column()
    return fmt.get_dataframe()


def get_area_list():
    ''' Returns data frame with two columns id and name 
    
    This method gets the data frame  and return the areaName data frame
    with columns 'id, and 'name'
    
    '''
    df = get_dataframe() 
    
    area = df['areaName'].unique()
    
    areaName = { 'id': area , 'name': area}
    areaName_df = pd.DataFrame(areaName , columns=['id', 'name'])
    areaName_df['id'] = areaName_df['id'].str.replace('&' , '&amp;')
    areaName_df['id'] = areaName_df['id'].str.replace(' ' , '&nbsp;')
    areaName_df = areaName_df.sort_values('name')
    
    return areaName_df

