
from math import *
from random import *
from ListData1 import TrainData
from ListData1 import TrainValues
from ListData1 import TestData
from ListData1 import TestValues


def Sigmoid(z):
    return 1.0/(1+pow(e,-z))

def Multiply(Theta,X):
    return sum([i*j for i,j in zip(Theta,X)])

def Cost(y,Theta,X):
    hx=Sigmoid(Multiply(Theta,X))
    if(y==1):
        return -log(hx,2)
    return -log(1-hx,2)

def CostFunction(Theta,L,Lambda,Y):
    sumi=0.0

    for i in range(len(L)):
        sumi=sumi+Cost(Y[i],Theta,L[i])
    sumi = sumi/len(L)

    SecondTerm=Multiply(Theta,Theta) - Theta[0]*Theta[0]
    sumi = sumi + ((Lambda+0.0)/(2*len(L)))*SecondTerm
    return sumi

def GradientDescentUtil(Alpha,L,index,Theta,Y):
    sumi=0.0

    for i in range(len(L)):
        X=L[i]
        hx=Sigmoid(Multiply(Theta,X))
        k=(hx-Y[i])*X[index]
        sumi=sumi+k
    return (Alpha*sumi/len(L))

def GradientDescent(Alpha,L,Theta,Y,Lambda):
    temp=[]
    for i in range(len(Theta)):
        k=GradientDescentUtil(Alpha,L,i,Theta,Y)
        xx=Theta[i]-k
        if(i!=0):
            xx=xx+(Lambda/len(L))*Theta[i]
        temp.append(xx)
    Theta=temp[:]
    return Theta

Alpha=0.1
Lambda=0
Theta=[]
Avg=[0.0,0.0,0.0,0.0,0.0,0.0]
def initialize():
    
    for i in range(6):
        k=random()
        Theta.append(k)
    for i in range(len(TrainData)):
        TrainData[i].insert(0,1)
        for j in range(len(TrainData[i])):
            Avg[j]=Avg[j]+TrainData[i][j]

    for i in range(6):
        Avg[i]=Avg[i]/len(TrainData)
        
    return


def normalize():
    for i in range(len(TrainData)):
        for j in range(len(TrainData[i])):
            TrainData[i][j]=TrainData[i][j]-Avg[j]

def predict(X,Theta):
    xx=Sigmoid(Multiply(X,Theta))
    if(xx>=0.5):
        return 1
    return 0

initialize()
normalize()

print(Alpha)
print(CostFunction(Theta,TrainData,Lambda,TrainValues))

for i in range(500):
    Theta=GradientDescent(Alpha,TrainData,Theta,TrainValues,Lambda)
    #print(Theta)
    
    print(CostFunction(Theta,TrainData,Lambda,TrainValues))

ans=0

#Accuracy
TruePostives=0
ActualPostive=0
PredictedPostives=0
ans=0
for i in range(len(TestData)):
    X=TestData[i]
    X.insert(0,1)
    for j in range(len(X)):
        X[j]=X[j]-Avg[j]
    
    k=predict(X,Theta)
    if(k==1):
        PredictedPostives=PredictedPostives+1
        if(TestValues[i]==1):
            TruePostives=TruePostives+1
            ActualPostive=ActualPostive+1
            ans=ans+1
    
    else:
        if(TestValues[i]==1):
            ActualPostive=ActualPostive+1
        else:
            ans=ans+1

        
print(TruePostives)
print(ActualPostive)
print(PredictedPostives)
print((ans+0.0)/200)







    
    




