import queue

G = [
    [0, 1, 1, 9999, 9999, 9999, 9999, 9999, 9999],
    [1, 0, 9999, 1, 1, 9999, 9999, 9999, 9999],
    [1, 9999, 0, 9999, 9999, 1, 1, 9999, 9999],
    [9999, 1, 9999, 0, 9999, 9999, 9999, 1, 9999],
    [9999, 1, 9999, 9999, 0, 9999, 9999, 1, 9999],
    [9999, 9999, 1, 9999, 9999, 0, 9999, 1, 1],
    [9999, 9999, 1, 9999, 9999, 9999, 0, 9999, 1],
    [9999, 9999, 9999, 1, 1, 1, 9999, 0, 9999],
    [9999, 9999, 9999, 9999, 9999, 1, 1, 9999, 0]
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

node_queue = queue.Queue(0)
node_queue.put('a')       #从a开始遍历

list = []

while node_queue.qsize() != 0:      #终止条件，队列为空
    tmp = trans[node_queue.get()]   #返回队列头元素
    list.append(retrans[tmp])
    for j in range(9):
        if G[tmp][j] == 1:          #查找所有和该元素构成边都顶点
            if node[retrans[j]] == 0:   #如果该顶点未遍历
                node[retrans[j]] = 1    #打上标记
                node_queue.put(retrans[j])  #送入队列

print(list)


