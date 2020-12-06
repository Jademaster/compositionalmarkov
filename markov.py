import numpy as np

class Openmat:

    def __init__(self,array,inp,out):
        self.mat=array
        self.inp=inp
        self.out=out

    def blackbox(self):
        forget= np.zeros((len(self.inp),len(self.out)))
        for a in range(len(self.inp)):
            for b in range(len(self.out)):
                forget[a,b] = self.mat[self.inp[a],self.out[b]]
        return forget


def mult(m1,m2):
    product= np.zeros((m1.shape[0],m2.shape[1]))
    for i in range(m1.shape[0]):
        for j in range(m2.shape[1]):
            product[i,j]= max([m1[i,k] * m2[k,j] for k in range(m1.shape[1])])
    return product
        
def compose(openmat1,openmat2):
    assert len(openmat1.out) == len(openmat2.inp), "open matrices have the wrong type and can't be composed"
    size= 2*openmat1.mat.shape[0] - len(openmat1.out)
    #extend the matrices to the pushout
    extend1=np.zeros((size,size))
    extend1[0:openmat1.mat.shape[0],0:openmat1.mat.shape[1]]=openmat1.mat
    print(extend1)
    extend2=np.zeros((size,size))
    extend2[size-openmat2.mat.shape[0]:size,size-openmat2.mat.shape[1]:size]=openmat2.mat
    print(extend2)
    #compute the composite
    composite=np.zeros((size,size))
    composite=np.maximum(extend1,extend2)
    return composite

#compute the most likely path which occurs in n-steps
   
a=np.random.rand(3,3)
b=np.random.rand(3,3)

in1= [0,1] 
out1=[0,1]
in2=[2]
out2=[0,1]
m1=Openmat(a,in1,out1)
m2=Openmat(b,in2,out2)
print(m1.blackbox())


