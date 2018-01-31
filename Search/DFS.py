
G = [
    [0, 1, 9999, 9999, 9999, 9999, 9999, 1, 9999],
    [1, 0, 1, 9999, 1, 9999, 9999, 9999, 9999],
    [9999, 1, 0, 1, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 1, 0, 1, 1, 9999, 9999, 9999],
    [9999, 1, 9999, 1, 0, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 1, 9999, 0, 1, 1, 9999],
    [9999, 9999, 9999, 9999, 9999, 1, 0, 9999, 9999],
    [1, 9999, 9999, 9999, 9999, 1, 9999, 0, 1],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 1, 0]
]

str = "abcdefghi"
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
retrans = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i'
}

node = {}
for i in str:
    node[i] = 0
node['a'] = 1
node_list = []
node_list.append('a')          #从a开始遍历

order = set()
while len(node_list) != 0:    #栈不为空
    tmp = trans[node_list[-1]]  #查看栈顶元素
    #print(tmp)
    order.add(retrans[tmp])
    tmp_node = []
    cnt = 0
    for j in range(9):
        if G[tmp][j] == 1:      #和栈顶元素组成边的顶点
            tmp_node.append(retrans[j])
            if node[retrans[j]] == 0:  #若未标记
                cnt += 1
                node_list.append(retrans[j])   #取返回的第一个未标记顶点入栈
                node[retrans[j]] = 1  #设为已标记
                break
    if cnt == 0:      #若全部顶点都标记
        node_list.pop()  #则该元素出栈

print(order)

