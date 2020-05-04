#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()
#Plotting bar plot
plt.bar(loan_status.index,loan_status)

# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False,figsize=(10,5))
#Changing the x-axis label
plt.xlabel('Property Area')
#Changing the y-axis label
plt.ylabel('Loan Status')
#Rotating the ticks of X-axis
plt.xticks(rotation = 45)

# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(10,5))
#Changing the x-axis label
plt.xlabel('Education Status')
#Changing the y-axis label
plt.ylabel('Loan Status')
#Rotating the ticks of X-axis
plt.xticks(rotation=45)

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education']=='Graduate']
#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education']=='Not Graduate']
#Plotting density plot for 'Graduate'
graduate.plot(kind='density',label='Graduate')
#Plotting density plot for 'Not Graduate'
not_graduate.plot(kind='density',label='Not Graduate')
#For automatic legend display
plt.legend()

# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1, figsize=(10,5))

#Plotting scatter plot
data.plot.scatter(x='ApplicantIncome',y='LoanAmount')
#Setting the subplot axis title
ax_1.set_title('Applicant Income')
#Plotting scatter plot
data.plot.scatter(x='CoapplicantIncome',y='LoanAmount')
#Setting the subplot axis title
ax_2.set_title('Coapplicant Income')
#Creating a new column 'TotalIncome'
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
#Plotting scatter plot
data.plot.scatter(x='TotalIncome',y='LoanAmount')
#Setting the subplot axis title
ax_3.set_title('Total Income')
