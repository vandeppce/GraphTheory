import numpy as np
G = [
    [0, 6, 9999, 4, 9999, 1],
    [5, 0, 7, 7, 9999, 9999],
    [9999, 9999, 0, 2, 4, 9999],
    [9999, 3, 5, 0, 1, 7],
    [2, 9999, 9999, 3, 0, 9999],
    [9999, 3, 4, 9999, 4, 0]
]
node_begin = ['a']

trans = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5
}
retran = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f'
}

G0 = G[trans['a']]
str = 'abcdef'

node = [i for i in str]
node_tran = list(set(str) - set(node_begin))     #遍历除出发节点外所有节点


while (len(node_tran) > 0):     #终止条件为待遍历节点集合为空
    tmp = np.argsort(G0)        #按照路径长度排序
    for i in tmp:
        if retran[i] in node_tran:   #若该节点未遍历
            node_del = [retran[i]]
            for j in range(6):
                if G0[j] > G0[i] + G[i][j]:
                    G0[j] = G0[i] + G[i][j]   #更新
            node_tran = list(set(node_tran) - set(node_del))  #删除已遍历节点
            break
print(G0)




