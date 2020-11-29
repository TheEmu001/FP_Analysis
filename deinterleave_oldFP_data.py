# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:31:56 2020

@author: HP
"""
import pandas as pd

path_name = "C:/Users/AD-AnestNorrislab/Box/Norris Lab shared/Tera Data & Programs/FP Testing/FP 3.9.2020/F2/"
file_name = "VGlut-CreC228F2_avgFluor_testing_Test1_2020-03-09T14_04_43.csv"
data = pd.read_csv(path_name+file_name)


data['Timestamp'] -= 1000
#data['Timestamp'] -= data['Timestamp'][0]

oddData = pd.DataFrame(data['Timestamp'][0:len(data['Timestamp']):2])
print(len(data['Timestamp']))
print(len(oddData))

evenData = pd.DataFrame(data['Timestamp'][1:len(data['Timestamp']):2])
print(len(evenData))




oddData['Unmarked Fiber2G'] = data['Unmarked Fiber2G'][0:len(data['Unmarked Fiber2G']):2]
oddData['Marked Fiber3G'] = data['Marked Fiber3G'][0:len(data['Marked Fiber3G']):2]

evenData['Unmarked Fiber2G'] = data['Unmarked Fiber2G'][1:len(data['Unmarked Fiber2G']):2]
evenData['Marked Fiber3G'] = data['Marked Fiber3G'][1:len(data['Marked Fiber3G']):2]

oddData.reset_index(drop=True, inplace = True)
evenData.reset_index(drop=True, inplace = True)


oddData.to_csv('OddData_TestData.csv',index=False)
evenData.to_csv('EvenData_TestData.csv',index=False)
