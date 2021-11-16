import node
import random
import time
import binarySearchTree
import AVLtree
import RBtree

# 기본 설정값 ( 필요시 수정 가능 )
MAX_NUMBER = 100_000_000
EPOCH = 100
DATA_SIZE = [1_000, 5_000, 10_000, 50_000, 100_000]
DATA = []

# 각 트리들
BS = binarySearchTree.binarySearchTree()
AVL = AVLtree.AVL()
RB = RBtree.RedBlackTree()

# 삽입에 소요된 시간
USED_TIME_INSERT = {
    "BS": [0, 0, 0, 0, 0],
    "AVL": [0, 0, 0, 0, 0],
    "RB": [0, 0, 0, 0, 0],
    "T": [0, 0, 0, 0, 0]
}

# 탐색에 소요된 시간
USED_TIME_SEARCH = {
    "BS": [0, 0, 0, 0, 0],
    "AVL": [0, 0, 0, 0, 0],
    "RB": [0, 0, 0, 0, 0],
    "T": [0, 0, 0, 0, 0]
}

print("program start")

print("start inserting data")
# 각 트리에 삽입
for e in range(EPOCH):
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

    # AVL에 삽입
    index = 0
    for i in DATA:
        start = time.time()
        for data in i:
            temp = node.Node(data)
            AVL.insert(temp)
        USED_TIME_INSERT["AVL"][index] += time.time() - start
        index += 1

    # RB에 삽입
    index = 0
    for i in DATA:
        start = time.time()
        for data in i:
            temp = node.Node(data)
            RB.insert(temp)
        USED_TIME_INSERT["RB"][index] += time.time() - start
        index += 1

    # T에 삽입
    index = 0
    for i in DATA:
        start = time.time()
        for data in i:
            pass
        USED_TIME_INSERT["T"][index] += time.time() - start
        index += 1
    print(f"====== {e+1}% complete ======")

print("삽입에 걸린 시간")
print(USED_TIME_INSERT)
