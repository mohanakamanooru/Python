'''
Python Programming - Program Flow Control

Mohana R Kamanooru - 08/10/2020
'''

##1.	Your program must ask the user for 4 values: 
##	Credit score (0 to 10 inclusive)
##	Address term (months at present address)
##	Income (£s)
##	Request (£s) (loan amount requested) 


#reading inputs from the user
#credit score ranges from 0 to 6
user_credit_score=int(input("Credit Score (between 0 to 10):"))

#user address term in months
user_address_term=int(input("Address Term (in months)      :"))

#income in pounds without separators
user_income=float(input("Income 		             :"))

#amount requested in pounds without separators
user_requested_amount=float(input("Requested Loan amount         :"))
                        


##validate inputs



##decision making for granting the loan

if (user_credit_score == 0 or user_income == 0 or user_address_term < 12):
    loan_approved=False

elif(user_credit_score == 1 and user_requested_amount < (0.2*user_income)):
    loan_approved=True

elif(user_credit_score in(2,5)and user_address_term >60 and user_requested_amount <user_income ):
    loan_approved=True
    
elif(user_credit_score in (7,10) and user_address_term <60 and user_requested_amount <user_income ):
    loan_approved=True

elif(user_requested_amount > user_income and user_requested_amount < 2* user_income and user_address_term >60 and user_credit_score >= 5):
    loan_approved=True
    
else:
    loan_approved=False



    
    
##print the loan approval decision to the user
if(loan_approved):
        print("Congratulations!!.. your loan has been approved")
else:
        print("Sorry!!.. Your loan is rejected")
