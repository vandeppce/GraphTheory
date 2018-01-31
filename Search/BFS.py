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
node_queue.put('a')

list = []

while node_queue.qsize() != 0:
    tmp = trans[node_queue.get()]
    list.append(retrans[tmp])
    for j in range(9):
        if G[tmp][j] == 1:
            if node[retrans[j]] == 0:
                node[retrans[j]] = 1
                node_queue.put(retrans[j])

print(list)


