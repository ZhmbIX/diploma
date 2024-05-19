import numpy as np

class Second():
    def __init__(self, r, p, d) -> None:
        self.k = len(r)
        vers = np.arange(1,self.k+2)
        r = np.append(r, np.inf)
        p = np.append(p, 0)
        d = np.append(d, 0)
        self.x = np.array([vers, r, p, d])
        self.best = None
        self.best2 = None
        self.ans1 = None
        self.ans2 = None
    
    def algos2(self):
        """Основной алгоритм"""
        pi = []
        t = 0
        i=0
        y = self.x
        while len(y.T)>1 and i<10:
            min_r = min(y[1])
            t = max(t,min_r)
            N_1 = np.copy(y.T[y[1]<=t].T)
            #print(N_1)
            N_1u = np.copy(y.T[y[1]>t].T)
            #print(N_1u)
            m = N_1.T[N_1[3]==min(N_1[3])][0].copy()
            #print(t, m[2], min(N_1u[1]))
            if t+m[2]<=min(N_1u[1]) and len(N_1.T)==1: 
                pi.append(m)
                t = min(N_1u[1])
                y = N_1u.copy()
                continue
            if t+m[2]<=min(N_1u[1]) and len(N_1.T)>1:
                pi.append(m)
                t = t + m[2]
                y = y.T[y[0]!=m[0]].T.copy()
                continue
            if t+m[2]>min(N_1u[1]):
                prev_m2 = m[2]
                m[2] = t + m[2] - min(N_1u[1])
                y = np.concatenate((y.T[y[0]!=m[0]] , np.array([m])), axis=0).T
                m[2] = prev_m2 - m[2]
                pi.append(m)
                t = min(N_1u[1])
                continue
        fst = self.stick(np.array(pi))
        scd = self.complicated(np.array(pi))
        self.ans1 = self.ans(fst)
        self.ans2 = self.ans(scd)
        return np.array(pi)
        

    def stick(self, ar):
        """[[1,2,2],             [[1,2],\n
            [1,2,2], = = = = >   [1,4],\n
            [1,2,2]]             [1,2]\n
            совмещает 2 "станка" в 1, если подряд идут в расписании один и тот же станок то просто в 1 совмещаются"""             
        m = 0
        new_ar = []
        j = -1
        for i in ar:
            if i[0]==m:
                new_ar[j] = new_ar[j] + i*np.array([0,0,1,0])
                continue
            else:
                new_ar.append(i)
                j+=1
                m=i[0]
        self.best = np.array(new_ar).T[0]
        return np.array(new_ar)


    def complicated(self, ar):
        """Усложнённый алгоритм"""
        dct = {}
        j=0
        for i in ar:
            if i[0] in dct.keys():
                dct[i[0]].append(tuple([j,i[1:]]))
            else:
                dct[i[0]] = [tuple([j,i[1:]])]
            j+=1
        n_d = []
        for i in dct.items():
            n_d.append(self.combine(i))
        d = dict(n_d)
        lst = []
        for i in sorted(d.keys()):
            lst.append(d[i])
        self.best2 = np.array(lst).T[0]
        return np.array(lst)


    def combine(self,tup):
        """Реализация переноса в усложнённом алгоритме"""
        ind, lst = tup
        j = 0
        p = 0
        ar = lst[0][1]*np.array([1,0,1])
        for i in lst:
            if p<i[1][1]:
                j = i[0]
            ar = ar + np.array([0,1,0])*i[1]
        return (j, np.concatenate(([ind],ar)))


    def ans(self,ar):
        """Считает целевую функцию"""
        a = 0
        t = 0
        for i in ar:
            t = max(t, i[1])
            a = max(a, t+i[2]-i[3])
            t = t + i[2]
        return a


    def prepare():
        n = int(input("Введите количество вершин: "))
        vers = np.arange(1,n+2)
        r_s = np.array(list(map(int, input("Введите r_i: ").split())))
        p_s = np.array(list(map(int, input("Введите p_i: ").split())))
        d_s = np.array(list(map(int, input("Введите d_i: ").split())))
        r_s = np.append(r_s, np.inf)
        p_s = np.append(p_s, 0)
        d_s = np.append(d_s, 0)
        return np.array([vers, r_s, p_s, d_s])


def main():
    
    a = Second([1,1,2,7],[3,5,2,4],[2,4,1,3])
    a.algos2()
    print(a.best, a.ans1)
    print(a.best2, a.ans2)
    """print(a)
    b = prepare()
    first = stick(algos2(b)) # Просто алгоритм
    second = complicated(algos2(b))# Усложнённый алгоритм
    print("С прерыванием: ", first.T[0], '\n', ans(first), '\n')
    print("Без прерывания: ", second.T[0], '\n', ans(second), '\n')"""

if __name__=="__main__":
    main()
