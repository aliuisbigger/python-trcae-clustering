import pm4py as pm
import pandas as pd
import  numpy as np
import copy
from sklearn_som.som import SOM

log1=pm.read_xes('loan/bank loan process.xes')
# log2=pm.read_xes('loan/Commercial loan process.xes')
# log3=pm.read_xes('loan/Housing loan process.xes')
# log4=pm.read_xes('loan/Small loan process.xes')
# log5=pm.read_xes('loan/Student loan process.xes')

def getloglist(log):
    loglist= []
    for trace in log:
        tracelist = []
        for event in trace:
            tracelist.append(event['concept:name'])
        loglist.append(tracelist)
    return loglist

loglist1=getloglist(log1)
# loglist2=getloglist(log2)
# loglist3=getloglist(log3)
# loglist4=getloglist(log4)
# loglist5=getloglist(log5)

# loglist = []
# for i in log1:
#     loglist.append(i)
# def totallist(log1,log2,log3,log4,log5):
#     loglist=[]
#     for i in log1:
#         loglist.append(i)
#     for i in log2:
#         loglist.append(i)
#     for i in log3:
#         loglist.append(i)
#     for i in log4:
#         loglist.append(i)
#     for i in log5:
#         loglist.append(i)
#     return loglist
# loglist=totallist(loglist1,loglist2,loglist3,loglist4,loglist5)

def geteventlist(l):
    eventlist=[]
    for i in l:
        for j in i:
            if j not in eventlist:
                eventlist.append(j)
    return eventlist,len(eventlist)

eventlist,el=geteventlist(loglist1)
# print(eventlist,el)

def getmaxtracelen(log):
    n=0
    for i in log:
        length=len(i)
        if n<length:
            n=length
    return n

maxlength=getmaxtracelen(loglist1)
# print(maxlength)

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
# print(loglist[0])
# print(codelist[0])

npcodelist=np.array(codelist)
som = SOM(m=2, n=2, dim=23, sigma=1.9,lr=0.99)
som.fit(npcodelist,1000,shuffle=False)
predictions = som.predict(npcodelist)
#
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
subprocess3=[]
# subprocess4=[]

# for i in range(len(predictions)):
#     if predictions[i]==0:
#         subprocess0.append(loglist[i])
#     elif predictions[i]==1:
#         subprocess1.append(loglist[i])
#     elif predictions[i] == 2:
#         subprocess2.append(loglist[i])
#     elif predictions[i]==3:
#         subprocess3.append(loglist[i])


# p=tracetostream(loglist)
p0=tracetostream(subprocess0)
p1=tracetostream(subprocess1)
p2=tracetostream(subprocess2)
p3=tracetostream(subprocess3)
# p4=tracetostream(subprocess4)

# p=pd.DataFrame(p)
p0=pd.DataFrame(p0)
p1=pd.DataFrame(p1)
p2=pd.DataFrame(p2)
p3=pd.DataFrame(p3)
# p4=pd.DataFrame(p4)

# p.columns=['caseid','event']
p0.columns=['caseid','event']
p1.columns=['caseid','event']
p2.columns=['caseid','event']
p3.columns=['caseid','event']
# p4.columns=['caseid','event']

p0.to_csv('code11/p0.csv',index=False)
p1.to_csv('code11/p1.csv',index=False)
p2.to_csv('code11/p2.csv',index=False)
p3.to_csv('code11/p3.csv',index=False)
# p4.to_csv('code11/p4.csv',index=False)
# p.to_csv('code11/p.csv',index=False)
