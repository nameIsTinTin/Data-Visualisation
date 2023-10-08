"""
 DATA SCIENCE BATCH-2023     


Project Description

Problem Statement :You are Given the limited HR data from a reputed organization XYZ technologies 
that include relevant information of the employees like id, designation ,performance score ,salary etc.

As a Data Scientist  make necessary visualisation from the data using seaborn/matplotlib.

Try to bring relevant inference from the data by visualizing the charts between multiple columns. 

State your finding with appropriate statements.

An example: 

Which is the most efficient department you find from your study.

 The balance between male and female employees etc.

 Employee_Name,EmpID,MarriedID,
 MaritalStatusID,GenderID,EmpStatusID,
 DeptID,PerfScoreID,FromDiversityJobFairID,Salary,
 Termd,PositionID,Position,State,Zip,DOB,Sex,MaritalDesc,
 CitizenDesc,HispanicLatino,DateofHire,DateofHire,TermReason,
 EmploymentStatus,Department,ManagerName,ManagerID,RecruitmentSource,
 PerformanceScore,EngagementSurvey,EmpSatisfaction,SpecialProjectsCount,
 LastPerformanceReview_Date,DaysLateLast30,Absences

"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sb 


def infer(data):
    df = pd.read_csv(data)
    #res = sb.scatterplot(x="GenderID",data=df)
    uniqueGenders = df.groupby('GenderID').nunique()
    print(uniqueGenders)


    plt.legend(title='Gender Amount', loc='upper right')
    # plt.title('The price of new phones vs their days used')
    # plt.xlabel('Days Used')
    # plt.ylabel('Price')
    plt.show()

    
    print(df.to_string)




if __name__ == '__main__':
    data = "HRDataset_v14.csv"
    infer(data)
