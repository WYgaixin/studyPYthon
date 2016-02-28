# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:13:04 2015

@author: ssw
"""


timeset={}
data=[]
timeminset={}
newmovie={}
oldmovie={}

for line in open('u1.data'):
    user,item,record,time=line.split()
    data.append([user,item,float(record),int(time)])
#print data[0:1]
for user,item,record,time in data:
    timeset.setdefault(item,[])
    timeset[item].append(time)
    #print timeset
 
for item in timeset:
    timeminset[item] = sorted(timeset[item])[0]
#print timeminset

for user,item,record,time in data:
    if time-timeminset[item]<60*24*60*60:
        newmovie.setdefault(user,{})
        newmovie[user][item]=record
        print newmovie
    else:
        oldmovie.setdefault(user,{})
        oldmovie[user][item]=record
        print oldmovie
        

    
   
    
#        timeminset[item]=time
   # for time in sorted(timeset, key=lambda x:x[0])[0:1]:
     
#    print timeset[item]
#    print timeset
#    print timeset.values()
     
     
     #   timeminset[item]=time       
#print timeminset
#for user,item,record,time in data:
    #if time-timeminset[item]

    
 