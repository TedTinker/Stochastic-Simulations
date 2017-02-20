# (a) Generate a sample path of Poisson process {N(t), t >= 0} with intensity 10 .
# Plot the sample path of N(.) for the time interval [0; 10] .
# (b) Generate another random variable T of Pareto distribution with scale parameter 1/3
# and shape parameter 3 , i.e., its probability density function given by
# f(x) = 1 / 9x^4 ; x >= 1/3 ;
# independently of the Poisson process {N(t), t >= 0}. Then find the value of N(T) .
# (c) Repeat this procedure in (b) 10000 times and estimate Cov(T;,N(T)) and Var(N(T)) (cf. (6)).
# (d) Estimate the standard error of each (Monte Carlo) estimate in (c). (Recall the definition of standard error).

import numpy
import random
import statistics

### Part A ###

eventList = []

for i in range(0,numpy.random.poisson(10)*10):
    eventList.append(random.uniform(0,10))

eventList.sort()

#Prints the set of all event times, in order, for making a graph
#This line is currently 'commented out,' only used for testing
#print(eventList) 

### Part B ###

T = numpy.random.pareto(3, 1)
value = 0 
for i in eventList:
  if(i < T):
    value += 1

print("At time T = ", T, ", N(T) = ", value)

### Part C ### 
#Performs the same task as part B, but 1,000 times for data collection

Tlist = []
Tmean = 0
NTlist = []
NTmean = 0

for i in range(0,1000):
  T = numpy.random.pareto(3, 1)
  Tlist.append(T)
  Tmean += T/999
  value = 0 
  for i in eventList:
    if(i < T):
      value += 1
  NTlist.append(value)
  NTmean += value/999
  
print("In 1,000 trials, the average value of N(T) was ", NTmean)

varianceNT = 0
covariance = 0 

for i in range(0,1000):
  varianceNT += (NTmean - NTlist[i])**2
  covariance += (NTmean - NTlist[i])*(Tmean - Tlist[i])
varianceNT /= 999
covariance /= 999

print("Estimated Variance: ", varianceNT)
print("Estimated Covariance: ", covariance)    

### Part D ### 
#Does the same thing as Part C, but 99 more times for data collection

meanList = [NTmean]
varianceList = [varianceNT]
covarianceList = [covariance]

for j in range(0,99): 
  #Resets those variable for iteration
  Tlist = []
  Tmean = 0
  NTlist = []
  NTmean = 0

  for i in range(0,1000):
    T = numpy.random.pareto(3, 1)
    Tlist.append(T)
    Tmean += T/999
    value = 0 
    for i in eventList:
      if(i < T):
        value += 1
    NTlist.append(value)
    NTmean += value/999
  
  meanList.append(NTmean)
  varianceNT = 0
  covariance = 0 

  for i in range(0,1000):
    varianceNT += (NTmean - NTlist[i])**2
    covariance += (NTmean - NTlist[i])*(Tmean - Tlist[i])
  varianceNT /= 999
  covariance /= 999
  
  varianceList.append(varianceNT)
  covarianceList.append(covariance)

mean1 = 0 
mean2 = 0 
mean3 = 0 
standardErrorMean = 0
standardErrorVariance = 0 
standardErrorCovariance = 0 

for i in range(0,100):
  mean1 += meanList[i]/100
  mean2 += varianceList[i]/100 
  mean3 += covarianceList[i]/100 
  
for i in range(0,100):
  standardErrorMean += ((meanList[i] - mean1)**2)/99
  standardErrorVariance += ((varianceList[i] - mean2)**2)/99  
  standardErrorCovariance += ((covarianceList[i] - mean3)**2)/99  
  
print("In 100 trials of 1,000 trials, the standard error of the mean was ", standardErrorMean**.5)
print("In 100 trials of 1,000 trials, the standard error of the variance was ", standardErrorVariance**.5)
print("In 100 trials of 1,000 trials, the standard error of the covariance was ", standardErrorCovariance**.5)
