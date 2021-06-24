# Python Programming - EligibleVoters
# Mohana Kamanooru 06/10/2020

# ask the user for their name, age and country of citizenship
name = input("Enter name :").title()
age = int(input("Enter age :"))
country = input("Enter country:").upper()

# If the person is under 18, they are not allowed to vote
if(age < 18):
    print(name, ",", country, " .You are not entitled to vote!!")

# If the person is over 18 and their country of citizenship is the UK or Britain
elif(age >= 18):
    if(country == "UK" or country == "BRITAIN"):
        print(name, ",", country, " .You are entitiled to vote!!")
else:
    print(name, ",", country, ".You are not entitled to vote!!")

