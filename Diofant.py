import random as r
import numpy as np
class DiofantEquation:
    def __init__(self,coefs,answer):
        self.coefs=np.array(coefs)
        self.answer=answer
        self.args=np.zeros(len(coefs))
    def try_args(self,args):
        return np.dot(self.coefs,np.array(args).transpose())
    def mistake(self,args):
        return abs(self.try_args(args)-self.answer)
    def solve(self,generation=5):  
        e = 0
        length = len(self.coefs)
        variants = [[r.randint(1,self.answer) for i in range(length)] for i in range(generation)]  
        bin = lambda: r.randint(0,1)
        def parent(res):
            rt = r.randint(0,10000)
            if rt<res[0]: return 0
            for i in range(1,len(res)):
                if res[i-1]<rt<res[i]:
                    return i     
        while True:
            mistakes = [self.mistake(i) for i in variants]
            sum = 0.0
            for m in range(len(mistakes)):
                if mistakes[m] == 0: 
                    self.args=np.array(variants[m])
                    return variants[m]
                sum +=1/mistakes[m]
            alives = [int((1/m)/sum*10000) for m in mistakes]
            res = [0 for i in range(generation)]
            res[0]=alives[0]
            for i in range(1,len(alives)):
                res[i]=res[i-1]+alives[i]
            parents = []
            for i in range(generation):
                first = parent(res)
                while first is None: first=parent(res)
                second = first
                while second==first: 
                    second = parent(res)
                    while second is None: second = parent(res)
                parents.append((first,second))
            s=variants[np.argmax(alives)]
            variants = [[variants[f[j%2]][j] for j in range(length) ] for f in parents]
            for v in variants:
                if bin() == 1: v[r.randint(0,length-1)] = r.randint(1,self.answer)
            variants[0]=s
            e+=1
        
a = DiofantEquation([1,2,3,4,5,6],100)
print(a.solve())
