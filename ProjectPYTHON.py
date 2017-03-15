# As described in the PDF file in the same Repository

import numpy 

class node: # Making a node object lets us easily set up a Markov Chain
  
  def __init__(self): 
    self.me = [[[0,0],[0,0]],[[0,0],[0,0]]] # This will be filled with 0s and 1s
    self.forward = []
    self.back = []
    self.up = []
    self.down = [] # These lists will be populated with each nodes directed edges
    self.left = []
    self.right = []
    
  def myOnes(self): # A quick method to check how many 1s in a node
    total = int(self.me[0][0][0]) + int(self.me[0][0][1]) + int(self.me[0][1][0]) + int(self.me[0][1][1]) + int(self.me[1][0][0]) + int(self.me[1][0][1]) + int(self.me[1][1][0]) + int(self.me[1][1][1])
    return total
          
  def show(self): # Prints the node in a reader-friendly way. The left layer is the 'front'
    print("(", self.me[0][0], " ", self.me[1][0], ")")
    print("(", self.me[0][1], " ", self.me[1][1], ")")    
    print()
    
    
nodeList = [] # A list for all the nodes
    
for i in range(0,256):
  placeholder = node()
  value = str(bin(i))[2:] # i from 0 to 255, value from 00000000 to 11111111 (binary)
  while(len(value)<8):
    value = "0" + value 
  placeholder.me = [[[value[0],value[1]],[value[2],value[3]]],[[value[4],value[5]],[value[6],value[7]]]]
  nodeList.append(placeholder) 
  
for i in nodeList:
  for j in range(0,16):
    value = str(bin(j))[2:]
    while(len(value)<4):
      value = "0" + value
    findMeF = [[[value[0],value[1]],[value[2],value[3]]],[[i.me[0][0][0],i.me[0][0][1]],[i.me[0][1][0],i.me[0][1][1]]]]
    findMeB = [[[i.me[1][0][0],i.me[1][0][1]],[i.me[1][1][0],i.me[1][1][1]]],[[value[0],value[1]],[value[2],value[3]]]]
    findMeU = [[[value[0],value[1]],[i.me[0][0][0],i.me[0][0][1]]],[[value[2],value[3]],[i.me[1][0][0],i.me[1][0][1]]]]
    findMeD = [[[i.me[0][1][0],i.me[0][1][1]],[value[0],value[1]]],[[i.me[1][1][0],i.me[1][1][1]],[value[2],value[3]]]]
    findMeR = [[[i.me[0][0][1],value[0]],[i.me[0][1][1],value[1]]],[[i.me[1][0][1],value[2]],[i.me[1][1][1],value[3]]]]
    findMeL = [[[value[0],i.me[0][0][0],],[value[1],i.me[0][1][0]]],[[value[2],i.me[1][0][0]],[value[3],i.me[1][1][0]]]]
    for k in nodeList:
      if(k.me == findMeF):
        i.forward.append(k)
      if(k.me == findMeB):
        i.back.append(k)
      if(k.me == findMeU):
        i.up.append(k)
      if(k.me == findMeD):
        i.down.append(k)
      if(k.me == findMeR):
        i.right.append(k)
      if(k.me == findMeL):
        i.left.append(k) # That ugly block adds all directed edges, populating those lists
        
# At this point, all nodes and their connections are established

def makeRandomPolicy(): # Relates each state to a random direction
  randomPolicy = []
  for i in nodeList:
    randomPolicy.append(numpy.random.choice(["F","B","U","D","R","L"]))
  return randomPolicy
  
def tedPolicy(): # Relates each state to the direction with the most 1s
  myPolicy = []
  for i in nodeList:
    expectF = 0 
    expectB = 0 
    expectU = 0 
    expectD = 0 
    expectR = 0 
    expectL = 0
    for a in i.forward: 
      expectF += a.myOnes()
    for a in i.back: 
      expectB += a.myOnes()
    for a in i.up: 
      expectU += a.myOnes()
    for a in i.down: 
      expectD += a.myOnes()
    for a in i.right: 
      expectR += a.myOnes()
    for a in i.left: 
      expectL += a.myOnes()
    decision = "F"
    if(expectB > expectF):
      decision = "B"
    if(expectU > expectB):
      decision = "U"
    if(expectD > expectU):
      decision = "D"
    if(expectR > expectD):
      decision = "R" 
    if(expectL > expectR):
      decision = "L"  
    myPolicy.append(decision) # Defaults to L,R,D,U,B (in that order) in case
                              # two directions have equal expectation
  return myPolicy
      

def runProcess(choiceList): # Given a policy, runs the process!
  
  time = 0
  state = nodeList[0] # Start on the all-zero node
  reward = 0
  
  while(time < 1000): # Continues forever. We only observe a portion.
    print("Time: ", time)
    print()
    state.show()
    decision = choiceList[nodeList.index(state)]
    print(decision)
    if(decision == "F"):
      state = numpy.random.choice(state.forward)
    elif(decision == "B"):
      state = numpy.random.choice(state.back)
    elif(decision == "U"):
      state = numpy.random.choice(state.up)
    elif(decision == "D"):
      state = numpy.random.choice(state.down)
    elif(decision == "R"):
      state = numpy.random.choice(state.right)
    elif(decision == "L"):
      state = numpy.random.choice(state.left)
    reward += 2*state.myOnes() - 8 # Total 1s minus total 0s
    print()
    print("Reward this step: ", 2*state.myOnes() - 8)
    print("Total reward: ", reward)
    print()
    time += 1
