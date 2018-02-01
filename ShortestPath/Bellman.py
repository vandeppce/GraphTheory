#coding=utf-8
import numpy as np
G = [
    [0, 1, 4, 9999, 9999],
    [9999, 0, 3, 2, 2],
    [9999, 9999, 0, -5, 9999],
    [9999, 1, 5, 0, 9999],
    [9999, 9999, 9999, -3, 0]
]
'''
G = [
    [0, 1, 4, 9999, 9999],
    [9999, 0, 4, 2, 2],
    [9999, 9999, 0, -5, 9999],
    [9999, 1, 5, 0, 9999],
    [9999, 9999, 9999, -3, 0]
]
'''
node_begin = ['a']
trans = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
}
retran = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
}

G0 = G[trans['a']]
str = 'abcde'

node = [i for i in str]
cnt = 0
for i in range(5):
    cnt += 1
    node_tran = list(set(str) - set(node_begin))     #遍历除出发节点外所有节点
    flag = 0           #本次迭代是否有更新
    while (len(node_tran) > 0):     #终止条件为待遍历节点集合为空
        tmp = np.argsort(G0)        #按照路径长度排序
        for i in tmp:
            if retran[i] in node_tran:   #若该节点未遍历
                node_del = [retran[i]]
                for j in range(5):
                    if G0[j] > G0[i] + G[i][j]:
                        G0[j] = G0[i] + G[i][j]   #更新
                        flag = 1     #有更新
                node_tran = list(set(node_tran) - set(node_del))  #删除已遍历节点
                break
    if flag == 0:       #若无更新，说明已经达到最短路径
        print("ShortestPath: ", G0)
        break

if cnt == 5:       #若迭代N次仍然未收敛，说明有负权环
    print("有负权环，无解")