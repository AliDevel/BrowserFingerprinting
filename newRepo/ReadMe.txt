Prerequesitions for running automatic testing tool for Hybrid applications:
1.Applications needs to be downloaded. 
 We downloaded our applicatons from Androzoo dataset[https://androzoo.uni.lu/].
2.Frida server needs to installed in a device. 
 Please refer to official site of the frida to install into device[https://frida.re/docs/android/]
3.Change applications folder localation in Automatedtesting.py.
  Variable $path contains, location information of apps which needs to be tested. After testing applications they 
  are moved to $path1. 

After completing prerequesitions, dynamic instrumentation ready to go. 
$ py automatedtesting.py 


It produces user_agents.csv file which contains package names, Urls, custom headers and user agent strings.

The script DatasetAnalyzer.py analyzes obtained dataset, by grouping them to Unencrypted traffic , user agent strings 
by their similarity, and  from how many unique packages we obtained the data.


     