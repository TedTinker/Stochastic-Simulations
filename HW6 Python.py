# Consider an M/M/2 queue in which customers arrive in accordance with a Poisson pro-
# cess having rate 1 and are served by any one of 2 servers — each having an exponentially
# distributed service time with rate lambda. Let us denote by X(t) the number of customers in the
# system at time t. Also, let us denote by Y(t) the number of customers departing by time t.
# For simplicity let us consider two cases lambda = 1 and lambda = 1/3 , and compare them, in order
# the effect of different service rate lambda.
#(a) Simulate the sample path of {X(t), Y(t), 0 <= t <= 100} with lambda = 1 .
#(b) Simulate the sample path of {X(t), Y (t), 0 <= t <= 100} with lambda = 1/3 . Does
# the behavior of the sample path of {X(t), Y (t), t >= 0} look different from the sample path in (a)?
#(c) Simulate the sample path long enough to estimate the stationary distribution of
# {X(t), t >= 0} with lambda = 1 .

import numpy 

### Part A ###
print("Part A")
print(" ")

time = 0
timeList=[0]
X = 0
XList=[0]
Y = 0
YList = [0]

while(time < 100):
  if(X == 0): 
    time += numpy.random.exponential(1)
    X = 1 
  elif(X == 1):
    time += numpy.random.exponential(1/(1+1))
    if(numpy.random.uniform(0,1) < 1/(1+1)):
      X = 2
    else:
      X = 0
      Y += 1
  else:
      time += numpy.random.exponential(1/(1+2))
      if(numpy.random.uniform(0,1) < 1/(1+2)):
        X += 1
      else:
        X -= 1 
        Y += 1
  timeList.append(time)
  XList.append(X)
  YList.append(Y)
  
for i in range(0,len(timeList)):
  print(timeList[i], ", ", XList[i])
  
print(" ")

for i in range(0,len(timeList)):
  print(timeList[i], ", ", YList[i])
  
print(" ")  
### Part B ###
print("Part B")
print(" ")

time = 0
timeList=[0]
X = 0
XList=[0]
Y = 0
YList = [0]

while(time < 100):
  if(X == 0): 
    time += numpy.random.exponential(1)
    X = 1 
  elif(X == 1):
    time += numpy.random.exponential(1/(1+1/3))
    if(numpy.random.uniform(0,1) < 1/(1+1/3)):
      X = 2
    else:
      X = 0
      Y += 1
  else:
      time += numpy.random.exponential(1/(1+2/3))
      if(numpy.random.uniform(0,1) < 1/(1+2/3)):
        X += 1
      else:
        X -= 1 
        Y += 1
  timeList.append(time)
  XList.append(X)
  YList.append(Y)
  
for i in range(0,len(timeList)):
  print(timeList[i], ", ", XList[i])
  
print(" ")

for i in range(0,len(timeList)):
  print(timeList[i], ", ", YList[i])
  
print(" ")  
### Part C ###
print("Part C")
print(" ")

time = 0
timeList=[]
X = 0
XList=[]

while(time < 1000):
  if(X == 0): 
    time += numpy.random.exponential(1)
    X = 1 
  elif(X == 1):
    time += numpy.random.exponential(1/(1+1))
    if(numpy.random.uniform(0,1) < 1/(1+1)):
      X = 2
    else:
      X = 0
  else:
      time += numpy.random.exponential(1/(1+2))
      if(numpy.random.uniform(0,1) < 1/(1+2)):
        X += 1
      else:
        X -= 1 
        
while(time < 2000):
  if(X == 0): 
    time += numpy.random.exponential(1)
    X = 1 
  elif(X == 1):
    time += numpy.random.exponential(1/(1+1))
    if(numpy.random.uniform(0,1) < 1/(1+1)):
      X = 2
    else:
      X = 0
  else:
      time += numpy.random.exponential(1/(1+2))
      if(numpy.random.uniform(0,1) < 1/(1+2)):
        X += 1
      else:
        X -= 1 
  timeList.append(time)
  XList.append(X)
  
XList.sort()
total = len(XList)
while(len(XList) > 0):
  state = XList[0]
  print("State: ", state, ", Frequency: ", XList.count(state)/total)
  XList[:] = [x for x in XList if x != state]
