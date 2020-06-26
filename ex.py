import pandas as pd
import statistics
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt
dosya = pd.read_csv("sat.csv")



print(dosya.info())


print((dosya['Mathematics Mean'].values)-(dosya['Critical Reading Mean'].values))
a = dosya['Critical Reading Mean'].mean()
b = dosya['Mathematics Mean'].mean()
c = dosya['Writing Mean'].mean()
print(a)
print(b)
print(c)


sns.countplot(dosya['Mathematics Mean'],label="count of Mathematics")

plt.show()
b = sns.countplot(dosya['Critical Reading Mean'],label="count of Reading")
plt.show()
c = sns.countplot(dosya['Writing Mean'],label="count of Writing")
plt.show()






"""
# school name is 460 but number of test takers is 386.
#1. answer is 460.
#2.answer is 460-386=74.cause number of test takers is 386.Some lines are empty.
#3.answer is  	BARD HIGH SCHOOL EARLY COLLEGE ,STUYVESANT HIGH SCHOOL e.g
#4.answer is Lower East Side Preparatory High School.result is 218.Some result's output were nan.
Because  lines are empty.



"""