# Student Marks Administration
# Pete Dwyer 01/11/17
# Saul Johnson 20/06/2019
        
from my_functions import datafile
from my_functions import score_criteria

        
# Initialise variables.
# Define functions.
def show_raw_data(dat):
    for ind in range(0, len(datafile.data), 2):
        print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4)) 


def show_pass_list(dat):
    for ind in range(0, len(datafile.data), 2):
        grade = score_criteria.get_grade(dat[ind + 1])
        if(not grade == "Fail"):
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), str(grade).rjust(4))

  
def show_fail_list(dat):
    
    for ind in range(0, len(datafile.data), 2):               
        if(dat[ind + 1] >= 30 and dat[ind + 1] <= 39):
            grade = "re-submission" 
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), str(grade).rjust(4))       
        elif(dat[ind + 1] < 30):
            grade = "Fail" 
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), str(grade).rjust(4))
  

def show_high_low_avg(dat):
    
    low_score = score_criteria.get_low_score(dat, 1)
    high_score = score_criteria.get_high_score(dat, 1)
    average = score_criteria.get_average(dat)
      
    print("Low Score        :  ", low_score[0], str(low_score[1]))     
    print("High Score       :  ", high_score[0], str(high_score[1]))
    print("Average Score    :  ", format(average,".2f"))
    

def show_stats_list(dat):
    count_abv_avg=score_criteria.get_above_avgcount(dat)
    count_blw_avg=score_criteria.get_below_avgcount(dat)
    
    print("Students Scored Above Avg:    ",count_abv_avg)
    print("Students Scored Below Avg:    ",count_blw_avg)

# Main body of program.
show_raw_data(datafile.data)
print("*********************************************")
show_pass_list(datafile.data)
print("*********************************************")
show_fail_list(datafile.data)
print("*********************************************")
show_high_low_avg(datafile.data)
print("*********************************************")
show_stats_list(datafile.data)
