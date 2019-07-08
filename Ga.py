import numpy 
import random ,pickle
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
            self.genes.append(numpy.random.uniform(low=-1, high=1, size=(i[0],i[1])))
                     
                

class Ga():
    def __init__(self,popsize,model):
        self.model=[]
        self.selection=10
        self.mutation=0.001
        self.popsize=popsize
        self.newbreed=[]
        self.initpopulation(popsize,model)
        self.max_mut=0.05
        self.min_mut=0.0005
        self.max_rev=500

    def save(self,name="data.sv"):
        savedata={}
        savedata["model"]=self.model
        savedata["selection"]=self.selection
        savedata["mutation"]=self.mutation
        savedata["popsize"]=self.popsize
        savedata["newbreed"]=self.newbreed
        with open(name , 'wb') as f:
            pickle.dump(savedata, f, pickle.HIGHEST_PROTOCOL)
        

    def load(self,name="data.sv"):
        with open(name , 'rb') as f:
            loaded= pickle.load(f)
        self.model=loaded["model"]
        self.selection=loaded["selection"]

        self.mutation=loaded["mutation"]
        self.popsize=loaded["popsize"]
        self.newbreed=loaded["newbreed"]

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
        gene=[]
        for x,y in zip(a.genes,b.genes):
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
            temp[i][random.randint(0,b)]+=self.mutation*random.uniform(-1,1)
        return temp
            
    def predict(self,popnum,theta):
        genes=self.population[popnum].genes
        for i in genes:
            theta=numpy.dot(theta,i)+numpy.dot(numpy.ones(theta.shape),i)
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
    
         

