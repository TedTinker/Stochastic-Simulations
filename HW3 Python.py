import numpy

### Part A ###

def mFunction(t):
  return(4*numpy.log(1+t))

n = numpy.random.poisson(10)

process1 = []
for i in range(0, n):
  process1.append(numpy.random.uniform(0, 10))

def N_1(t):
  value = 0 
  for i in process1:
    if(i < t):
      value +=1 
      
  return value
  
def Nt(t):
  return N_1(mFunction(t))
  
print("N(t) represents the number of events before time t in a non-homogeneous Poisson process with mean function m(t) = 4 log(1 + t).")
print()
  
print("N(0) = ", Nt(0)) 
print("N(1) = ", Nt(1)) 
print("N(2) = ", Nt(2)) 
print("N(3) = ", Nt(3)) 
print("N(4) = ", Nt(4)) 
print("N(5) = ", Nt(5)) 
print("N(6) = ", Nt(6)) 
print("N(7) = ", Nt(7)) 
print("N(7) = ", Nt(7))
print("N(8) = ", Nt(8)) 
print("N(9) = ", Nt(9)) 
print("N(10) = ", Nt(10)) 
print()

### Part B ###

firstEventTimes = []

for i in range(0,10000):

  n = numpy.random.poisson(10)

  process1 = []
  for i in range(0, n):
    process1.append(numpy.random.uniform(0, 10))
  
  for j in range(0, 10000):
    if(Nt(j/10) >= 1 and Nt(j/10 -.1) == 0):
      firstEventTimes.append(j/10)
      break

print("In 10,000 trials, the average time of the first event was ", numpy.mean(firstEventTimes), ".")
print("The variance seems to be ", numpy.var(firstEventTimes), ".")
print()

### Part C ###

def mFunction_2(t):
  return(t**2 + 2*t)
  
n = numpy.random.poisson(120)

process1 = []
for i in range(0, n):
  process1.append(numpy.random.uniform(0, 120))
  
def Nt_2(t):
  return N_1(mFunction_2(t))
  
print("N(t) represents the number of events before time t in a non-homogeneous Poisson process with mean function m(t) = t^2 + 2t.")
print()
  
print("N(0) = ", Nt_2(0)) 
print("N(1) = ", Nt_2(1)) 
print("N(2) = ", Nt_2(2)) 
print("N(3) = ", Nt_2(3)) 
print("N(4) = ", Nt_2(4)) 
print("N(5) = ", Nt_2(5)) 
print("N(6) = ", Nt_2(6)) 
print("N(7) = ", Nt_2(7)) 
print("N(7) = ", Nt_2(7))
print("N(8) = ", Nt_2(8)) 
print("N(9) = ", Nt_2(9)) 
print("N(10) = ", Nt_2(10)) 
print()
  
### Part D ###

fourAndFive = 0

for i in range(0,10000):

  n = numpy.random.poisson(120)

  process1 = []
  for i in range(0, n):
    process1.append(numpy.random.uniform(0, 120))
  
  if(Nt_2(5) - Nt_2(4) == 5):
    fourAndFive += 1

print("In 10,000 trials, ", fourAndFive, " processes had exactly 5 events between time 4 and time 5. That's ", fourAndFive/10000, " of the trials.")