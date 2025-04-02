import pandas as pd
import numpy as np

# from sklearn.linear_model import LinearRegression
from scipy import stats  

jobs = pd.read_csv('Jobs.csv')
SkillsLN = pd.read_csv('LinkedIn Skills.csv')


jobs['Salary'] = (jobs['SalaryMin'] + jobs['SalaryMax']) / 2
jobs['Salary'].fillna(jobs['SalaryMin'], inplace=True)
jobs['Salary'].fillna(jobs['SalaryMax'], inplace=True)

jobs['Salary'] = jobs['Salary'] * np.where(jobs['SalaryPeriod']=='Daily', 200, 1)
jobs['Salary'] = jobs['Salary'] * np.where(jobs['SalaryPeriod']=='Hourly', 200*7.5, 1)

data = pd.merge(SkillsLN, jobs, left_on='JobID', right_on='JobID', how='left')

counts = data['Skill'].value_counts()
data = pd.merge(data, counts, left_on='Skill', right_on='Skill', how='left')

data = data[['JobID', 'Skill', 'Salary']]

data = pd.get_dummies(data, columns=['Skill'], dtype=int)

aggregator = {'Salary': 'mean'}
columns = list(data.columns)
for column in columns:
    if column.startswith('Skill_'):
        aggregator[column] = 'sum'

data = data.groupby('JobID').agg(aggregator)

#Visualisation
Visualisation = data[data['Skill_Visualization'] == 1]['Salary']
NoVisualisation = data[data['Skill_Visualization'] == 0]['Salary']

t_stat, p_val = stats.ttest_ind(Visualisation, NoVisualisation)

print('Visualisation')
print("Vis Average = " + str(Visualisation.mean()))
print("No Vis Average = " + str(NoVisualisation.mean())) 
print("t-statistic = " + str(t_stat))  
print("p-value = " + str(p_val))


#Python
Python = data[data['Skill_Python (Programming Language)'] == 1]['Salary']
NoPython = data[data['Skill_Python (Programming Language)'] == 0]['Salary']

t_stat, p_val = stats.ttest_ind(Python, NoPython)

print('Python')
print("Python Average = " + str(Python.mean()))
print("No Python Average = " + str(NoPython.mean())) 
print("t-statistic = " + str(t_stat))  
print("p-value = " + str(p_val))



#PowerBI
PowerBI = data[data['Skill_Microsoft Power BI'] == 1]['Salary']
NoPowerBI = data[data['Skill_Microsoft Power BI'] == 0]['Salary']

t_stat, p_val = stats.ttest_ind(PowerBI, NoPowerBI)

print('Skill_Microsoft Power BI')
print("Power BI Average = " + str(PowerBI.mean()))
print("No Power BI Average = " + str(NoPowerBI.mean())) 
print("t-statistic = " + str(t_stat))  
print("p-value = " + str(p_val))


#Tableau
Tableau = data[data['Skill_Tableau'] == 1]['Salary']
NoTableau = data[data['Skill_Tableau'] == 0]['Salary']

t_stat, p_val = stats.ttest_ind(Tableau, NoTableau)

print('Tableau')
print("Tableau Average = " + str(Tableau.mean()))
print("No Tableau Average = " + str(NoTableau.mean())) 
print("t-statistic = " + str(t_stat))  
print("p-value = " + str(p_val))


