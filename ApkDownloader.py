#downloading applications from androzoo with given dataset
import requests
import os
import pyandrozoo
import csv
path = 'path/to/the/applications/folder'
path2='path/to/the/tested/applications/folder'
files = os.listdir(path)
files2=os.listdir(path2)
file = open('dataset.txt',mode='r')
reader = csv.reader(file)
apks = []
androzoo = pyandrozoo.pyAndroZoo('1c625022adf1fc4081fd7120d2c61db9f3a82940929c177395a8714e414a3b91')
with open("dataset.txt", "r") as file:
    while True:
        file_eof = file.readline()
        if file_eof == '':
            print('End Of File')
            break
        if(str(file_eof).strip()+".apk" not in files and str(file_eof).strip()+".apk" not in files2):
              apks.append(str(file_eof).strip())    

print(len(apks))

file.close()
androzoo.get(apks)
