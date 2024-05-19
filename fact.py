import itertools as it
import pandas as pd
import numpy as np

class First():

    def __init__(self, r, p, d) -> None:
        self.k = len(r)
        self.rpd = pd.DataFrame(np.array([r,p,d]).T, columns=['r', 'p', 'd'])
        self.best = None


    def first_algos(self) -> int:
        result = np.inf
        for i in it.permutations(list(range(self.k))):
            r = self.graphic(list(i))
            if result > r:
                result = r
                self.best = np.array(i) + 1
        return result


    def graphic(self, perm) -> int:
        r_s = self.rpd['r'][perm].to_numpy()
        d_s = self.rpd['d'][perm].to_numpy()
        p_s = self.rpd['p'][perm].to_numpy()
        t_s = []
        t = 0
        for i in range(len(r_s)):
            t = max(t, r_s[i])
            t = t + p_s[i]
            t_s.append(t)
        t_s = np.array(t_s)
        ans = t_s - d_s
        ans[ans<0]=0
        return np.max(ans)




def main():
    r = list(map(int,input().split()))
    p = list(map(int,input().split()))
    d = list(map(int,input().split()))
    res = First(r,p,d)
    print("Целевая функция:",res.first_algos())
    print("Расписание:", res.best)
if __name__=="__main__":
    main()
