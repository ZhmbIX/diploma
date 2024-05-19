import numpy as np


def algos2(x):
    """Основной алгоритм"""
    pi = []
    t = 0
    i=0
    while len(x.T)>1 and i<10:
        min_r = min(x[1])
        t = max(t,min_r)
        N_1 = np.copy(x.T[x[1]<=t].T)
        #print(N_1)
        N_1u = np.copy(x.T[x[1]>t].T)
        #print(N_1u)
        m = N_1.T[N_1[3]==min(N_1[3])][0].copy()
        #print(t, m[2], min(N_1u[1]))
        if t+m[2]<=min(N_1u[1]) and len(N_1.T)==1: 
            pi.append(m)
            t = min(N_1u[1])
            x = N_1u.copy()
            continue
        if t+m[2]<=min(N_1u[1]) and len(N_1.T)>1:
            pi.append(m)
            t = t + m[2]
            x = x.T[x[0]!=m[0]].T.copy()
            continue
        if t+m[2]>min(N_1u[1]):
            prev_m2 = m[2]
            m[2] = t + m[2] - min(N_1u[1])
            x = np.concatenate((x.T[x[0]!=m[0]] , np.array([m])), axis=0).T
            m[2] = prev_m2 - m[2]
            pi.append(m)
            t = min(N_1u[1])
            continue
        
    return np.array(pi)
    

def stick(ar):
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
    return np.array(new_ar)


def complicated(ar):
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
        n_d.append(combine(i))
    d = dict(n_d)
    lst = []
    for i in sorted(d.keys()):
        lst.append(d[i])
    return np.array(lst)


def combine(tup):
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


def ans(ar):
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
    a = np.array([[1,2,3,4,5],[2,2,3,6,np.inf],[1,1,1,1,0],[3,2,1,2,0]])
    print(a)
    b = prepare()
    first = stick(algos2(b)) # Просто алгоритм
    second = complicated(algos2(b))# Усложнённый алгоритм
    print("С прерыванием: ", first.T[0], '\n', ans(first), '\n')
    print("Без прерывания: ", second.T[0], '\n', ans(second), '\n')

if __name__=="__main__":
    main()
