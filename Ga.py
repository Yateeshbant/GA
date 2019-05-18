import numpy 
import random 
class Model():
    def __init__(self):
        self.size=[]

    def add(self,x,y):
        self.size.append([x,y])

class Population():
    def __init__(self,rewards=0,genes=None):
        self.reward=rewards
        self.genes=genes 

    def initialize(self,sizes):
        self.genes=[]
        for i in sizes.size:
            self.genes.append(numpy.random.rand(i[0],i[1]))
        
        

class Ga():
    def __init__(self,popsize,model):
        self.model=[]
        self.selection=10
        self.mutation=0.001
        self.popsize=popsize
        self.newbreed=[]
        self.initpopulation(popsize,model)

    def initpopulation(self,popsize,modelsize):  #int model()
        self.population=[]
        
        for i in range(popsize):
            x=Population(0)
            x.initialize(modelsize)
            self.population.append(x)
        
    
    def naturalselection(self):
        self.b=[]
        for i in self.population:
            self.b.append(i.reward)
        
        self.b=sorted(range(len(self.b)),key=self.b.__getitem__)[0:self.selection]
         

    def crossover(self):
        for i in range(self.popsize):
            self.cross(self.population[self.b[random.randint(0,(self.selection-1))]],self.population[self.b[random.randint(0,(self.selection-1))]])

    def cross(self,a,b):
        self.model=[]
        for x,y in zip(a.genes,b.genes):
            gene=[]
            temp=numpy.empty((x.shape))
            temp.T[0:int(x.shape[1]/2)]=x.T[0:int(x.shape[1]/2)]
            temp.T[int(x.shape[1]/2):x.shape[1]]=y.T[int(x.shape[1]/2):x.shape[1]]
            temp=self.mutate(temp)
            gene.append(temp)
        self.newbreed.append(Population(0,gene))
        
    def mutate(self,temp):
        a,b=temp.shape
        b-=1
        for i in range(a):
            temp[i][random.randint(0,b)]+=self.mutation*random.randint(-1,1)
        return temp
            
    def predict(self,popnum,theta):
        genes=self.population[popnum].genes
         
        for i in genes:
            theta=numpy.dot(theta,i)
        return theta
    
    def run(self,x):
        self.predict(i)
    def setreward(self,x,y):
        self.population[x].reward=y
        
    def breed(self):
        self.naturalselection()
        self.crossover()
        self.population=self.newbreed
        self.newbreed=[]

    def config(self,reward_func=None,selection=3,mutation_rate=0.001):
        self.reward_func=reward_func
        self.selection=selection
        self.mutation=mutation_rate
    
         

