
import os
import csv
url={}
useragent={}
<<<<<<< HEAD
packages={"1"}
with open('user_agents.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
         if len(row["header"])>0:
          print(row["header"])
         packages.add(row["packageName"])
=======

with open('user_agents.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
         #Grouped unencrypted traffic by packages       
>>>>>>> 414a6760c0444e92aa0baf1d577b5dec3aa10892
         if row["packageName"] not in url:
          if "http://" in row["url"]:
           url[row["packageName"]]=[]
           url[row["packageName"]].append(row["url"])
         elif "http://" in row["url"] :
          url[row["packageName"]].append(row["url"])
         #Grouped user agents by  packages  
         if  row["user agent"] not in useragent:
           useragent[row["user agent"]]=[]
           useragent[row["user agent"]].append(row["packageName"])
         else:
           useragent[row["user agent"]].append(row["packageName"])       
      
  
<<<<<<< HEAD
=======
       
>>>>>>> 414a6760c0444e92aa0baf1d577b5dec3aa10892
       
        file = open('url.csv', 'a')
        writer = csv.writer(file)  
        header = ["packageName","url"] 
        writer.writerow(header)        
        for key, value in url.items():
            data=[key,value]
            writer.writerow(data)
<<<<<<< HEAD
            
=======
                
                
>>>>>>> 414a6760c0444e92aa0baf1d577b5dec3aa10892
        file = open('useragents1.csv', 'a')
        writer = csv.writer(file)  
        header = ["useragents","package","size", "useragentlength"]
        writer.writerow(header)
        sums=0
                
        for key, value in useragent.items():
<<<<<<< HEAD
            useragents=list(dict.fromkeys(value))
            sums=sums+len(useragents)
            if len(key)<180 or len(key)>222:
             print(key)
            data=[key, useragents, len(useragents), len(key)]
            writer.writerow(data)        
        print(sums)

        file = open('packages.csv', 'a')
        writer = csv.writer(file)  
        header = ["packageName"] 
        writer.writerow(header) 
        packages=list(packages)
        for item in packages:
         data=[item]
         writer.writerow(data)    
         
=======
            data=[key,"|",value]
            writer.writerow(data)        
>>>>>>> 414a6760c0444e92aa0baf1d577b5dec3aa10892
