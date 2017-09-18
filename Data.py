
L1=[]

from math import *

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


print(L1)


            
   
    

    
