#алгоритм 1.2
def first_algos(r_p: list) -> int:
    results = []
    for i in range(len(r_p)):
        cop = r_p.copy()    #создаем копию списка 
        cop.pop(i)          #удаляем из этого списка i объект 
        cop.sort()          #сортируем без i объекта 
        results.append(graphic(cop))
    print(results)
    return min(results)


def graphic(r_p:  list) -> int:
    ans = 0
    for i in range(len(r_p)):
        if ans<=r_p[i][0]:
            ans = sum(r_p[i])
        else:
            ans += r_p[i][1]
    return ans

def build(r:list, p:list) -> list:
    """[(r1,p1), (r2,p2), (r3,p3)]"""
    return list(zip(r,p))


def main():
    r = list(map(int,input("Введите r").split()))
    p = list(map(int,input("Введите p").split()))
    res = first_algos(build(r,p))
    print("Целевая функция = ", res)

if __name__=="__main__":
    main()
