import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

jobs = pd.read_csv('./data/Jobs.csv')
SkillsLN = pd.read_csv('./data/LinkedIn Skills.csv')


jobs['Salary'] = (jobs['SalaryMin'] + jobs['SalaryMax']) / 2
jobs['Salary'].fillna(jobs['SalaryMin'], inplace=True)
jobs['Salary'].fillna(jobs['SalaryMax'], inplace=True)

jobs['Salary'] = jobs['Salary'] * np.where(jobs['SalaryPeriod']=='Daily', 200, 1)
jobs['Salary'] = jobs['Salary'] * np.where(jobs['SalaryPeriod']=='Hourly', 200*7.5, 1)

data = pd.merge(SkillsLN, jobs, left_on='JobID', right_on='JobID', how='left')

counts = data['Skill'].value_counts()
data = pd.merge(data, counts, left_on='Skill', right_on='Skill', how='left')
data = data[data['count'] > 10]

data = data[['JobID', 'Skill', 'Salary']]

data = pd.get_dummies(data, columns=['Skill'], dtype=int)

aggregator = {'Salary': 'mean'}
columns = list(data.columns)
for column in columns:
    if column.startswith('Skill_'):
        aggregator[column] = 'sum'



data = data.groupby('JobID').agg(aggregator)
data.to_csv('dataPivot.csv')


X = data.drop(columns=['Salary']) 
y = data['Salary'] 

model = LinearRegression()
model.fit(X, y)

SalaryImpact = pd.DataFrame({'Skill': X.columns, 'Coefficient': model.coef_})
SalaryImpact['SalaryImpact'] = SalaryImpact['Coefficient'] / model.intercept_

print(SalaryImpact.sort_values('Coefficient', ascending=False))



sample = {}
for column in X.columns:
    sample[column] = 0
sample['Skill_Tableau'] = 1
predict = pd.DataFrame(sample, index=[0])
print(predict.head())

print(model.predict(predict).reshape(-1)[0])

# X = sm.add_constant(X) 
# est = sm.OLS(endog=y, exog=X.assign(intercept=1)).fit()
# results = est.summary2().tables[1].sort_values('P>|t|')
# results.to_csv('SalaryImpact.csv')
