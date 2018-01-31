G = [
     [0, 10, 9999, 9999, 9999, 11, 9999, 9999, 9999],  # a的邻居表
     [10, 0, 18, 9999, 9999, 9999, 12, 12, 9999],  # b的邻居表
     [9999, 18, 0, 22, 9999, 9999, 9999, 8, 9999],  # c的邻居表
     [9999, 9999, 22, 0, 20, 9999, 24, 21, 16],  # d的邻居表
     [9999, 9999, 9999, 20, 0, 26, 9999, 9999, 7],  # e的邻居表
     [11, 9999, 9999, 9999, 26, 0, 17, 9999, 9999],  # f的邻居表
     [9999, 12, 9999, 24, 9999, 17, 0, 9999, 19],  # g的邻居表
     [9999, 12, 8, 21, 9999, 9999, 9999, 0, 9999],  # h的邻居表
     [9999, 9999, 9999, 16, 7, 9999, 19, 9999, 0]   # i的邻居表
]

E = []

str = "abcdefghi"
for i in range(len(str)):
    for j in range(i, len(str)):
        if i is not j:
            E.append((str[i], str[j], G[i][j]))

E = sorted(E, key=lambda x: x[2])

T = set()
V = [[i] for i in str]

#print(E)

def connected(element):                  #返回元素所在的连通子图
    for e in V:
        if element in e:
            return V.index(e)

for element in E:
    if connected(element[0]) != connected(element[1]):        #判断是否为同一连通子图
        tmp = connected(element[1])
        V[connected(element[0])].extend(V[connected(element[1])])       #将两个子图连通
        V.remove(V[tmp])                       #删除另一个子图
        T.add(element)                   #加入最小生成树

T = sorted(T, key=lambda x: x[2])
cost = 0
for item in T:
    cost += item[2]

print(T)
print("cost is: ",cost)



