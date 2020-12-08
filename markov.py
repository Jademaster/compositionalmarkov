import numpy as np

def listmax(mats):
    runningmax=np.zeros(mats[0].shape)
    for m in mats:
        runningmax=np.maximum(m,runningmax)
    return runningmax
    

def mult(m1,m2):
    product= np.zeros((m1.shape[0],m2.shape[1]))
    for i in range(m1.shape[0]):
        for j in range(m2.shape[1]):
            product[i,j]= max([m1[i,k] * m2[k,j] for k in range(m1.shape[1])])
    return product
        
def power(m,n):
    powers=[np.identity(m.shape[0])]
    current=m
    for i in range(n):
        powers.append(current)
        current= mult(m,current)
    return powers


class Openmat:

    def __init__(self,array,inp,out):
        self.mat=array
        self.inp=inp
        self.out=out
        self.powers=[]
        
    def precompile(self,maxtime):
        self.powers=power(self.mat,maxtime)

    def blackbox(self,power=1):
        forget= np.zeros((len(self.inp),len(self.out)))
        for a in range(len(self.inp)):
            for b in range(len(self.out)):
                forget[a,b] = self.powers[power][self.inp[a],self.out[b]]
        return forget
 


def compose(openmat1,openmat2):
    assert len(openmat1.out) == len(openmat2.inp), "open matrices have the wrong type and can't be composed"
    size= 2*openmat1.mat.shape[0] - len(openmat1.out)
    #extend the matrices to the pushout of sets
    extend1=np.zeros((size,size))
    extend1[0:openmat1.mat.shape[0],0:openmat1.mat.shape[1]]=openmat1.mat
    extend2=np.zeros((size,size))
    extend2[size-openmat2.mat.shape[0]:size,size-openmat2.mat.shape[1]:size]=openmat2.mat
    #compute the composite
    composite=np.zeros((size,size))
    composite=np.maximum(extend1,extend2)
    return composite

def partitions(n):
    if n==0:
        return [(0,0)]
    else:
        partition=[(j[0]+1,j[1]) for j in partitions(n-1)]
        partition.append((0,n))
        return partition
      
def nmostlikely(m1,m2,n):
    return listmax([mult(m1.blackbox(power=p[0]),m2.blackbox(power=p[1])) for p in partitions(n)])
   




