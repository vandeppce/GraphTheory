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

str = "abcdefghi"
V = [i for i in str]
str_ori = ['a']
trans = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8
}
T = set()
while (set(str_ori) != set(str)):
    E = []
    tmplist = list(set(V) - set(str_ori))         #补集
    for i in str_ori:
        for j in tmplist:
            if G[trans[i]][trans[j]] < 9999 :
                E.append((i, j, G[trans[i]][trans[j]]))     #查找所有U和V-U构成的边
    E = sorted(E, key = lambda x: x[2])           #添加最小边
    T.add(E[0])
    str_ori.append(E[0][1])                       #更新U集合
    str_ori = sorted(str_ori)

T = sorted(T, key=lambda x: x[2])
cost = 0
for item in T:
    cost += item[2]
print(T)
print("cost is: ", cost)
