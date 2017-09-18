
L1=[]

from math import *
import sys

with open('Dataset') as f:
    
    for line in f:
        #Removing end Character
        s=line[:-1]
        L=s.split(',')
        L1.append(L)


avg=[0.0,0.0,0.0,0.0,0.0]
cnt=[0,0,0,0,0]

for i in range(len(L1)):
    for j in range(len(L1[i])-1):
        if(L1[i][j]=='?'):
            continue
        cnt[j]=cnt[j]+1
        avg[j]=avg[j]+int(L1[i][j])

for i in range(5):
    avg[i]=avg[i]/cnt[i]

for i in range(len(L1)):
    for j in range(len(L1[i])-1):
        if(L1[i][j]=='?'):
            L1[i][j]=str(int(avg[j]))


Y=[]

for i in range(len(L1)):
    k=int(L1[i][-1])
    Y.append(k)
    L1[i]=L1[i][:-1]
    for j in range(len(L1[i])):
        L1[i][j]=int(L1[i][j])


Dataset=L1


#Creating Test Data and Train Data
TestData=[]
TestValues=[]
TrainData=[]
TrainValues=[]

for i in range(200):
    xx=Dataset[i][:]

    TestData.append(xx)
    TestValues.append(Y[i])

for i in range(200,len(Dataset)):
    xx=Dataset[i][:]
    TrainData.append(xx)
    TrainValues.append(Y[i])

sys.stdout.write("TrainData = ")
print(TrainData)
sys.stdout.write("TrainValues = ")
print(TrainValues)

sys.stdout.write("TestData = ")
print(TestData)

sys.stdout.write("TestValues = ")
print(TestValues)




            
   
    

    
