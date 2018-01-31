G = [
    [0, 2, 6, 4],
    [9999, 0, 3, 9999],
    [7, 9999, 0, 1],
    [5, 9999, 12, 0]
]

str = "abcd"
trans = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd'
}
trans_path = [[['' for i in range(1)] for j in range(4)] for k in range(4)]

for k in range(4):       #中转节点遍历：1，1-2，1-2-3，1-2-3-4
    for i in range(4):   #起点
        for j in range(4): #终点
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]     #更新
                trans_path[i][j].append(trans[k]) #添加到中转节点集合

print(G)
print(trans_path)