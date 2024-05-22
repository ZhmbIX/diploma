import numpy as np
import pandas as pd
class Third():
    def __init__(self, r, p, d, w, t=0) -> None:
        self.k = len(r)
        vers = np.arange(1,self.k+1)
        self.x = np.array([vers, r, p, d, w])
        self.t = t
        self.best = []
        self.ans = None


    def algos(self):
        t1 = sum(self.x[2]) + self.t
        y = self.x.copy()
        while t1>self.t and y.size>0:
            m = np.argmin((t1 - y[3])*y[4])
            self.best.append(y.T[m])
            y = np.delete(y, m, 1)
            t1-=self.x[2][m]
        self.best = np.array(self.best[::-1]).T
    
    def draw(self):
        self.algos()
        t1 = self.t
        ans = -np.inf
        for i in range(len(self.best[2])):
            ans = max(ans,t1+self.best[2][i] - self.best[3][i])
            t1+=self.best[2][i]
        self.ans = ans

def main():
    a = Third([1,1,1,1,1,1],[3,2,1,4,2,3],[11,3,20,16,2,5],[15,5,20,5,10,8],2)
    a.draw()
    print(a.best)
    print(a.ans)


if __name__=="__main__":
    main()