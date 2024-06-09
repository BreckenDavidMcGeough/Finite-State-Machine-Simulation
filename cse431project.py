class Enumerator:
	def __init__(self,m):
		self.current = None
		self.allGraphs = []
		self.m = m
	def SetCurrent(self,current):
		self.current = current
		self.allGraphs.append(current)
	def generate2digraph(self):
		newGraph = []


	def Next():
		copy = self.current
		self.current = self.generate2digraph()
		return copy

class SGraph(object):
	def __init__(self,V,E):
		self.V = V 
		self.E = E 
		self.switches = {v:0 for v in self.V}
	def reset(self):
		self.switches = {v:0 for v in self.V}
	def Move(self,initpos,inputString):
		if len(inputString) == 0:
			return initpos
		bin_ab = (inputString[0]=="a")*0 + (inputString[0]=="b")*1
		nextNode = self.E[bin_ab][initpos]
		if self.switches[nextNode] == 1:
			self.switches[nextNode] = 0
		else:
			self.switches[nextNode] = 1
		cpy = inputString
		inputString = inputString[1:]
		#print(str(initpos)+cpy+"to ->"+str(nextNode)+inputString+str(self.switches[nextNode]))
		return self.Move(nextNode,inputString)

#generate binary tree where add 'a' to nodes on left and add 'b' to nodes on right. Creates every single permutation of a and b of n length
#
#Example for n=3:
#
#			 aaa   aab aba  abb    baa   bab bba   bbb
#			   \	/   \    /       \    /   \    /
#				\aa/     \ab/	      \ba/     \bb/
#				   	\   /			   	  \   /
#					 \a/                   \b/
#					   \	         	   /
#						\     			  /
#						 \               /
#						  \ 			/
#						   \emptystring/
#
#this recursive binary tree is an example for n=3, and thus we get [aaa,aab,aba,abb,baa,bab,bba,bbb]							

	def generatePerms(self,n,currentstring,arr):
		if len(currentstring) == n:
			arr.append(currentstring)
			return currentstring
		updated_left = currentstring+"a"
		updated_right = currentstring+"b"
		left = self.generatePerms(n,updated_left,arr)
		right = self.generatePerms(n,updated_right,arr)

	def Count(self,initpos,dest,n):
		permutations = []
		self.generatePerms(n,"",permutations)
		num = 0
		for i in permutations:
			newG = SGraph(self.V,self.E)
			if newG.Move(initpos,i) == dest:
				#print("Count "+str(i))
				num += 1
		return num

	def SCount(self,initpos,dest,n,states):
		permutations = []
		self.generatePerms(n,"",permutations)
		num = 0
		for i in permutations:
			newG = SGraph(self.V,self.E)
			if newG.Move(initpos,i) == dest:
				if states == [newG.switches[key] for key in newG.switches]:
					#print("SCount:"+str(i))
					num += 1
		return num

	def Solve(self,initpos,states):
		match = False
		n = 1
		while match == False:
			permutations = []
			self.generatePerms(n,"",permutations)	
			for i in permutations:
				newG = SGraph(self.V,self.E)
				dest = newG.Move(initpos,i)
				newGstates = newG.switches
				if [newGstates[key] for key in newGstates] == states:
					match = True
					return i
			n+=1
			if n>50:
				match = True
		return n




V = [1,2,3,4,5,6]
E = [{1:2,2:3,3:4,4:5,5:6,6:1},{1:3,2:4,3:5,4:6,5:1,6:2}]


o = SGraph(V,E)
print(o.Move(1,"aabbab"))
print(o.switches)


print(o.Count(1,1,3))

#arr = []
#m.generatePerms(5,"",arr)
#print(len(arr))

print(o.Count(1,4,6))

print(o.SCount(1,4,6,[1,0,1,1,1,0]))

print(o.Solve(1,[1,0,1,1,1,0]))

print(o.Solve(1,[1,1,0,0,0,0]))

V2 = [1,2,3,4]
E2 = [{1:4,2:1,3:1,4:3},{1:3,2:3,3:2,4:2}]

q = SGraph(V2,E2)
print("")
print(q.Move(1,"abbab"))
print(q.switches)

print(q.Count(1,4,2))

print(q.SCount(1,4,2,[1,1,1,1]))

print(q.Solve(1,[1,0,0,1]))

print(q.Solve(1,[1,0,0,0]))


#m = SGraph(V,E)
#print(m.Move(1,"aabbab"))

#print(m.switches)

#print(m.Count(1,1,3)) #=1

#arr = []
#m.generatePerms(5,"",arr)
#print(len(arr))

#print(m.Count(1,6,6)) #=6

#print(m.SCount(1,4,6,[1,0,1,1,1,0])) #=1

#print(m.Solve(1,[1,0,1,1,1,0]))#=baab

#E = [[2,3,4,5,6,1],[3,4,5,6,1,2]]

#def Move(self,initpos,inputString):
	#if len(inputString) == 0:
		#return initpos
	#bin_ab = (inputString[0]=="a")*0 + (inputString[0]=="b")*1
	#nextNode = self.E[bin_ab][initpos-1]
	#if self.switches[nextNode] == 1:
		#self.switches[nextNode] = 0
	#else:
		#self.switches[nextNode] = 1
	#cpy = inputString
	#inputString = inputString[1:]
	#print(str(initpos)+cpy+"to ->"+str(nextNode)+inputString+str(self.switches[nextNode]))
	#return self.Move(nextNode,inputString)


