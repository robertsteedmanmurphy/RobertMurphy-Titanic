import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.read_csv("C:/Users/robert.murphy/Downloads/titanic-data.csv")

print df.head()
print df.describe()


num_women_men = df.groupby('Sex').count()['PassengerId']
plt.style.use('ggplot')
plt.pie(num_women_men, labels= num_women_men.index)
plt.title('Women and men passengers')
plt.show()
print num_women_men

survivors = df[df['Survived'] == 1]
male_female_survivors = survivors.groupby('Sex').count()['PassengerId']
plt.style.use('ggplot')
plt.pie(male_female_survivors, labels= male_female_survivors.index)
plt.title('Women and men survivors')
plt.show()
print male_female_survivors

class_by_gender_Survived = df.groupby(['Pclass','Sex']).describe()['Survived']
print class_by_gender_Survived
all_ages = df[np.isfinite(df['Age'])]
plt.hist(all_ages['Age'], bins= 20)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('#Passengers')
plt.show()

children_under_16 = df[df['Age'] <= 16]
print children_under_16.groupby('Sex').describe()['Survived']

def random_sample_of_dataset(x, n):
    return x.ix[random.sample(x.index, n)]

female_passengers = df[df['Sex'] == 'female']
women_total_sample = []
for i in range(100):
    woman_pick = random_sample_of_dataset(female_passengers, 25)['Survived']
    women_total_sample.append(np.mean(woman_pick))

print df.Survived.mean()
print df['Survived'].std()
print np.mean(women_total_sample)
print df.Survived.std()/16
