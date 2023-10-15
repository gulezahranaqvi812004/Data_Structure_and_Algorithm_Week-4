# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:42:09 2023

@author: Dell 7490
"""
import matplotlib.pyplot as plt 
import pandas as pd

#Line chart
# df = pd.read_csv('D:\\Semester3\\DSALab\\Week4\\2\\dailySteps_merged.csv')
# print(df.dtypes)
# l1 = df['ActivityDay'].values.tolist()
# l2 = df['StepTotal'].values.tolist()
# plt.vlines(l1, l2,ymax=  1, color = ['blue', 'green'])
# plt.show()

#Bar chart
# df = pd.read_csv('D:\\Semester3\\DSALab\\Week4\\2\\dailyActivity_merged.csv' )
# print(df.dtypes)
# l1 = df['ActivityDate'].values.tolist()
# l2 = df['TotalDistance'].values.tolist()
# plt.bar(l1, l2,width=1, color = ['red', 'green'])
# plt.show()

#Scatter chart
# df = pd.read_csv('D:\\Semester3\\DSALab\\Week4\\2\\sleepDay_merged.csv')
# print(df.dtypes)
# l1 = df['SleepDay'].values.tolist()
# l2 = df['TotalTimeInBed'].values.tolist()
# plt.scatter(l1, l2, color = 'purple')
# plt.xlabel('Sleep Day')
# plt.ylabel('Total Time In Bed')
# plt.show()

#Scatter chart
df = pd.read_csv('D:\\Semester3\\DSALab\\Week4\\2\\hourlySteps_merged.csv')
slices = df.groupby('ActivityHour')['StepTotal'].sum()
lbl = slices.index.tolist()  # Convert index (ActivityHour) to list for labels
values = slices.values.tolist()  # Convert values to list for pie chart slices
plt.figure(figsize=(8, 8))
plt.pie(values, labels=lbl, shadow=True, autopct='%1.1f%%')
plt.title('Distribution of StepTotal by ActivityHour')
plt.show()

