import pm4py as pm
import pandas as pd
import  numpy as np
import copy
from sklearn_som.som import SOM

log1=pm.read_xes('borrowing/Library borrowing process.xes')

def getloglist(log):
    loglist= []
    for trace in log:
        tracelist = []
        for event in trace:
            tracelist.append(event['concept:name'].strip())
        loglist.append(tracelist)
    return loglist

loglist1=getloglist(log1)

def geteventlist(l):
    eventlist=[]
    for i in l:
        for j in i:
            if j not in eventlist:
                eventlist.append(j)
    return eventlist,len(eventlist)

eventlist,el=geteventlist(loglist1)
print(eventlist,el)

def getmaxtracelen(log):
    n=0
    for i in log:
        length=len(i)
        if n<length:
            n=length
    return n

maxlength=getmaxtracelen(loglist1)
print(maxlength)

def initbkanktrace(eventistlen):
    l=[]
    for i in range(eventistlen):
        l.append(0)
    return l

blanktrace=initbkanktrace(el)

def getcode(log,eventlist):
    codelist=[]
    bl=copy.deepcopy(blanktrace)
    for trace in log:
        tracecode=copy.deepcopy(bl)
        for element in trace:
            tracecode[eventlist.index(element)]+=1
        codelist.append(tracecode)
    return codelist

codelist=getcode(loglist1,eventlist)

npcodelist=np.array(codelist)
som = SOM(m=3, n=1, dim=30, sigma=1.9,lr=0.99)
som.fit(npcodelist,1000,shuffle=False)
predictions = som.predict(npcodelist)

print(predictions)

def tracetostream(data):
    list=[]
    for i in range(len(data)):
        for j in data[i]:
            l = []
            l.append('case'+str(i))
            l.append(j)
            list.append(l)
    return list

subprocess0=[]
subprocess1=[]
subprocess2=[]

for i in range(len(predictions)):
    if predictions[i]==0:
        subprocess0.append(loglist1[i])
    elif predictions[i]==1:
        subprocess1.append(loglist1[i])
    elif predictions[i] == 2:
        subprocess2.append(loglist1[i])

p0=tracetostream(subprocess0)
p1=tracetostream(subprocess1)
p2=tracetostream(subprocess2)

p0=pd.DataFrame(p0)
p1=pd.DataFrame(p1)
p2=pd.DataFrame(p2)

p0.columns=['caseid','event']
p1.columns=['caseid','event']
p2.columns=['caseid','event']

p0.to_csv('code21/p0.csv',index=False)
p1.to_csv('code21/p1.csv',index=False)
p2.to_csv('code21/p2.csv',index=False)