import node
import random
import time
import binarySearchTree
import AVLtree
import RBtree
import treaps

# 기본 설정값 ( 필요시 수정 가능 )
MAX_NUMBER = 100_000_000
EPOCH = 100
DATA_SIZE = [1_000, 5_000, 10_000, 50_000, 100_000]
DATA = []

# 각 트리들
BS = binarySearchTree.binarySearchTree()
AVL = AVLtree.AVL()
RB = RBtree.RedBlackTree()
T = treaps.treaps()

# 삽입에 소요된 시간
USED_TIME_INSERT = {
    "BS": [0, 0, 0, 0, 0],
    "AVL": [0, 0, 0, 0, 0],
    "RB": [0, 0, 0, 0, 0],
    "T": [0, 0, 0, 0, 0]
}

# 탐색에 소요된 시간
USED_TIME_SEARCH = {
    "BS": 0,
    "AVL": 0,
    "RB": 0,
    "T": 0
}

print("program start")

print("start inserting data")
# 각 트리에 삽입
for e in range(1):
    DATA = [random.sample(range(0, MAX_NUMBER), i) for i in DATA_SIZE]

    # BS에 삽입
    index = 0
    for i in DATA:
        start = time.time()
        for data in i:
            temp = node.Node(data)
            BS.insert(temp)
        USED_TIME_INSERT["BS"][index] += time.time() - start
        index += 1

        if i != DATA[-1]:
            BS.root = None
    print(BS.root)

    # AVL에 삽입
    index = 0
    for i in DATA:
        start = time.time()
        for data in i:
            temp = node.Node(data)
            AVL.insert(temp)
        USED_TIME_INSERT["AVL"][index] += time.time() - start
        index += 1
        if i != DATA[-1]:
            AVL.root = None

    # RB에 삽입
    index = 0
    for i in DATA:
        start = time.time()
        for data in i:
            temp = node.Node(data)
            RB.insert(temp)
        USED_TIME_INSERT["RB"][index] += time.time() - start
        index += 1
        if i != DATA[-1]:
            RB.root = None

    # T에 삽입
    index = 0
    for i in DATA:
        start = time.time()
        for data in i:
            temp = node.Node(data)
            T.insert(temp)
        USED_TIME_INSERT["T"][index] += time.time() - start
        index += 1
        if i != DATA[-1]:
            T.root = None

    print(f"====== INSERT {e+1}% COMPLETE ======", flush=True)

# 각 트리에서 특정한 값 탐색 ( 마지막 데이터 리스트에서 한 값을 추출해서 탐색 )
for e in range(EPOCH):

    SEARCH = random.choice(DATA[-1])

    # BS에 삽입
    start = time.time()
    BS.root.search(SEARCH, BS.root)
    USED_TIME_SEARCH["BS"] += time.time() - start

    # AVL에 삽입
    start = time.time()
    AVL.root.search(SEARCH, AVL.root)
    USED_TIME_SEARCH["AVL"] += time.time() - start

    # RB에 삽입
    start = time.time()
    RB.root.search(SEARCH, RB.root)
    USED_TIME_SEARCH["RB"] += time.time() - start

    # T에 삽입
    start = time.time()
    T.root.search(SEARCH, T.root)
    USED_TIME_SEARCH["T"] += time.time() - start

    print(f"====== SEARCH {e+1}% COMPLETE ======")

print("삽입에 걸린 시간")

index = 0
for key in USED_TIME_INSERT:
    print(key)
    for i in USED_TIME_INSERT[key]:
        print(f"{DATA_SIZE[index]}개 : {i} 초")
        index += 1
    index = 0

print("탐색에 걸린 시간")
for key in USED_TIME_SEARCH:
    print(f"{key} : {USED_TIME_SEARCH[key]}")
