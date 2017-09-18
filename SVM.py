from ListData1 import *
from math import *
from random import *

m1 = 10
m0=10
C=1
Theta=[]
B=0.0
K=[]
avg=[0.0]*len(TrainData[0])
Sigma=2

def Multiply(Theta,X):
    return sum([i*j for i,j in zip(Theta,X)])

def cost1(x):
    if(x>=1):
        return 0
    return m1*x-m1

def cost0(x):
    if(x<=-1):
        return 0
    return m0*x+m0


def CostUtil(Theta,X,y):
    return y*cost1(Multiply(Theta,X)) + (1-y)*cost0(Mutiply(Theta,X))

def CostFunction(L,Y):
    sumi=0.0
    for i in range(len(L)):
        sumi=sumi+CostUtil(Theta,X,Y[i])
    k=Multiply(Theta,Theta)-Theta[0]*Theta[0]
    sumi=C*sumi + k/2.0
    return sumi

def LinearKernel(X1,X2):
    return sum([i*j for i,j in zip(X1,X2)])

def GuassianKernel(X1,X2):
    ans=0.0

    for i in range(len(X1)):
        xx=X1[i]-X2[i]
        ans=ans+xx*xx
    ans=ans/(2*Sigma*Sigma)
    
    return pow(e,-ans)


def buildKernel():
    for x1 in TrainData:
        temp=[]
        for x2 in TrainData:
            xx=GuassianKernel(x1,x2)
            temp.append(xx)
        K.append(temp)

    return

def CalculateError(alphas,b,index):
    prediction=[i*j for i,j in zip(alphas,TrainValues)]

    for i in range(len(TrainData)):
        prediction[i]=prediction[i]*K[i][index]

    return b+ sum(prediction)-TrainValues[index]

def initialize():
    for i in range(len(TrainValues)):
        if(TrainValues[i]==0):
            TrainValues[i]=-1
    for i in range(len(TestValues)):
        if(TestValues[i]==0):
            TestValues[i]=-1

    for i in range(len(TrainData)):
        for j in range(len(TrainData[i])):
            avg[j]=avg[j]+TrainData[i][j]

    for i in range(len(TrainData[0])):
        avg[i]=avg[i]/len(TrainData)


    for i in range(len(TrainData)):
        for j in range(len(TrainData[i])):
            TrainData[i][j]=TrainData[i][j]-avg[j]

    for i in range(len(TestData)):
        for j in range(len(TestData[i])):
            TestData[i][j]=TestData[i][j]-avg[j]

            
    return

def optimizeSMO():
    #Initailize
    b=0.0
    m=len(TrainData)
    alphas=[0.0]*m
    error=[0.0]*m
    passes=0
    maxpasses=10
    eta=0.0
    L=0.0
    H=0.0

    tol=pow(e,-3)
    
    #BuildingKernel

    buildKernel()
    while(passes<maxpasses):

        num_changed_alphas=0

        for i in range(0,m):
            error=CalculateError(alphas,b,i)
            #print(error)
            y=TrainValues[i]
            if((y*error<-tol and alphas[i]<C) or (y*error>tol and alphas[i]>0)):
                #selecting 2nd lanranges variable for subprobem

                j=floor(m*random())

                while(i==j):
                    j=floor(m*random())

                j=int(j)
                error_j=CalculateError(alphas,b,j)

                #print(error_j)
               # print("j")
                
                alphas_i_old=alphas[i]
                alphas_j_old=alphas[j]

                if(TrainValues[i]==TrainValues[j]):
                    L=max(0,alphas[i]+alphas[j]-C)
                    H=min(C,alphas[i]+alphas[j])
                else:
                    L=max(0,alphas[j]-alphas[i])
                    H=min(C,alphas[j]-alphas[i]+C)

                
                if(L==H):
                    continue

                eta=2*K[i][j] - K[i][i]-K[j][j]
                if(eta>=0):
                    continue

                alphas[j]=alphas[j] - (TrainValues[j]*(error-error_j+0.0))/eta
                alphas[j]=min(H,alphas[j])
                alphas[j]=max(L,alphas[j])

                #print(alphas[j])
                
                if(abs(alphas[j]-alphas_j_old)<tol):
                    alphas[j]=alphas_j_old
                    continue

                alphas[i]=alphas[i]+(TrainValues[i]*TrainValues[j]*(alphas_j_old-alphas[j]))
                
                b1=b-error-TrainValues[i]*K[i][i]*(alphas[i]-alphas_i_old)-TrainValues[j]*K[i][j]*(alphas[j]-alphas_j_old)
                b2=b-error_j-TrainValues[i]*K[i][j]*(alphas[i]-alphas_i_old)-TrainValues[j]*K[j][j]*(alphas[j]-alphas_j_old)

                if(alphas[i]>0 and alphas[i]<C):
                    b=b1
                elif(alphas[j]>0 and alphas[j]<C):
                    b=b2
                else:
                    b=(b1+b2)/2

                global B
                B=b
                
                num_changed_alphas=num_changed_alphas+1

                
                
                
                #print("here")
                

            #ends if
        #ends for
        #print(num_changed_alphas)
        if(num_changed_alphas==0):
            passes=passes+1
        else:
            passes=0
        print(passes)
        
    return alphas


initialize()

alphas=optimizeSMO()

Theta=[0.0]*len(TrainData[0])



def CalTheta():
    for i in range(len(TrainValues)):
        for j in range(len(TrainData[0])):
            Theta[j]=Theta[j]+alphas[i]*TrainValues[i]*TrainData[i][j]
    
    return






def predict(X,Theta):
    k=sum([i*j for i,j in zip(X,Theta)])
    k=k+B
    
    if(k>=0):
        return 1
    return -1


def PredictGuassian(X):
    ans=0.0
    for i in range(len(TrainData)):
        ans=ans+alphas[i]*TrainValues[i]*GuassianKernel(TrainData[i],X)
    ans=ans+B
    
    if(ans>=0):
        return 1
    return -1



ans=0.0
ans1=0.0
ans2=0.0

    
for i in range(len(TestData)):
    
    print(PredictGuassian(TestData[i]))
          
    if(PredictGuassian(TestData[i])==TestValues[i]):
        
        ans=ans+1

        if(TestValues[i]==1):
            ans1=ans1+1
        else:
            ans2=ans2+1

print(ans/len(TestData))
print(ans1)
print(ans2)

        

    
    


















