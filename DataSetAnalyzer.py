
import os
import csv
url={}
useragent={}
httpl={"3"}
with open('user_agents.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
         if row["packageName"] not in url:
          if "http://" in row["url"]:
           url[row["packageName"]]=[]
           url[row["packageName"]].append(row["url"])
         elif "http://" in row["url"] :
          url[row["packageName"]].append(row["url"])
         if  row["user agent"] not in useragent:
           useragent[row["user agent"]]=[]
           useragent[row["user agent"]].append(row["packageName"])
         else:
           useragent[row["user agent"]].append(row["packageName"])       
      
         if "http://" in row["url"]:
           httpl.add(row["url"])
       
        
        file = open('url.csv', 'a')
        writer = csv.writer(file)  
        header = ["packageName","url"] 
        writer.writerow(header)        
        for key, value in url.items():
            data=[key,value]
            writer.writerow(data)
        file = open('useragents1.csv', 'a')
        writer = csv.writer(file)  
        header = ["useragents","package"]
        writer.writerow(header)   
        for key, value in useragent.items():
            data=[key,"|",value]
            writer.writerow(data)        