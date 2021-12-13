input = """rf-RL
rf-wz
wz-RL
AV-mh
end-wz
end-dm
wz-gy
wz-dm
cg-AV
rf-AV
rf-gy
end-mh
cg-gy
cg-RL
gy-RL
VI-gy
AV-gy
dm-rf
start-cg
start-RL
rf-mh
AV-start
qk-mh
wz-mh"""

example2 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

example3 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

large = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

small = """start-a
start-b
a-C
b-end
a-end"""

example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

# 19 paths

edges = input.splitlines()

# Get number of nodes
nodes = []
for edge in edges:
    n = edge.split("-")
    if n[0] not in nodes:
        nodes.append(n[0])
    if n[1] not in nodes:
        nodes.append(n[1])

nodes_dict = dict()
idx_to_str = dict()
idx = 0
for node in nodes:
    nodes_dict[node] = idx
    idx_to_str[idx] = node
    idx += 1
#print(nodes_dict)

# Create adjacency matrix
matrix = [[0 for x in range(len(nodes))] for y in range(len(nodes))] 

for edge in edges:
    n = edge.split("-")
    left = n[0]
    right = n[1]
    left_idx = nodes_dict[left]
    right_idx = nodes_dict[right]
    matrix[left_idx][right_idx] = 1
    matrix[right_idx][left_idx] = 1

#for row in matrix:
#    print(row)

# Start/End node index
start_idx = nodes_dict["start"]
end_idx = nodes_dict["end"]

count = []
# Breadth first search with visited set only for small letters and recursion to distinguish same paths
def bfs1(node: str, count : list(), path):
    #print("bfs on node:", node_str, "and count =", len(count))
    node_idx = nodes_dict[node]
    path.append(node)
    neighbor_idx = 0
    for has_conn in matrix[node_idx]:
        neighbor = idx_to_str[neighbor_idx]
        if (has_conn and (neighbor not in path or neighbor[0].isupper())):
            if (neighbor == "end"):
                count.append(0)
                p = path.copy()
                p.append("end")
                #print(p)
            else:
                p = path.copy()
                bfs1(neighbor, count, p)
        neighbor_idx += 1


# Breadth first search with visited set only for small letters and recursion to distinguish same paths
def bfs2(node: str, count : list(), path, visited_twice: str):
    #print("bfs on node:", node_str, "and count =", len(count))
    node_idx = nodes_dict[node]
    path.append(node)
    neighbor_idx = 0
    for has_conn in matrix[node_idx]:
        neighbor = idx_to_str[neighbor_idx]
        # Großbuchstaben
        if (has_conn and neighbor[0].isupper()):
            p = path.copy()
            bfs2(neighbor, count, p, visited_twice)
        # Kleinbuchstaben und nicht "start"
        elif (has_conn and neighbor != "start"):
            if (neighbor == "end"):
                count.append(0)
                p = path.copy()
                p.append("end")
                #print(p)
            elif (neighbor in path and visited_twice == ""):
                p = path.copy()
                bfs2(neighbor, count, p, neighbor)
            elif(neighbor not in path):
                p = path.copy()
                bfs2(neighbor, count, p, visited_twice)
        neighbor_idx += 1

path = []
#print("----------------")
bfs2("start", count, path, "")
#print("----------------")

#bfs(start_idx, list(), count)

print(len(count))