import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

jobs = pd.read_csv('data\OtherData\datacamp_job_postings.csv')
jobs = jobs.dropna(subset=['Minimum Pay', 'Maximum Pay', 'Job Skills'])

jobs['Salary'] = (jobs['Minimum Pay'] + jobs['Maximum Pay']) / 2

print(jobs['Job Skills'].dtype)

skills = []
for index, row in jobs.iterrows():
    for skill in row['Job Skills'].split(','):
        skills.append([row['Job Posting ID'], skill.strip()])

skills = pd.DataFrame(skills, columns=['Job Posting ID', 'Skill'])

data = pd.merge(skills, jobs, left_on='Job Posting ID', right_on='Job Posting ID', how='left')

counts = data['Skill'].value_counts()
data = pd.merge(data, counts, left_on='Skill', right_on='Skill', how='left')
data = data[data['count'] > 10]

data = data[['Job Posting ID', 'Skill', 'Salary']]

data = pd.get_dummies(data, columns=['Skill'], dtype=int)

aggregator = {'Salary': 'mean'}
columns = list(data.columns)
for column in columns:
    if column.startswith('Skill_'):
        aggregator[column] = 'sum'



data = data.groupby('Job Posting ID').agg(aggregator)


X = data.drop(columns=['Salary']) 
y = data['Salary'] 

model = LinearRegression()
model.fit(X, y)

SalaryImpact = pd.DataFrame({'Skill': X.columns, 'Coefficient': model.coef_})
SalaryImpact['SalaryImpact'] = SalaryImpact['Coefficient'] / model.intercept_

print(SalaryImpact.sort_values('Coefficient', ascending=False))
SalaryImpact.sort_values('Coefficient', ascending=False).to_csv('outputs\Impacts.csv', index=False)


sample = {}
for column in X.columns:
    sample[column] = 0
sample['Skill_Tableau'] = 1
predict = pd.DataFrame(sample, index=[0])
print(predict.head())

print(model.predict(predict).reshape(-1)[0])