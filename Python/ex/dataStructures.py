class Node:
    def __init__(self, data):
        self.data = data
        self.Llink = None
        self.Rlink = None


def add_after(prevNode, newNode):
    nextNode = prevNode.Rlink  # 기존 오른쪽 노드 저장

    # 1) NewNode 오른쪽 연결
    newNode.Rlink = nextNode

    # 2) prevNode 오른쪽을 NewNode로
    prevNode.Rlink = newNode

    # 3) NewNode 왼쪽 연결
    newNode.Llink = prevNode

    # 4) nextNode가 있다면 nextNode 왼쪽을 NewNode로
    if nextNode:
        nextNode.Llink = newNode


# 테스트
A = Node("A")
B = Node("B")
C = Node("C")

A.Rlink = C
C.Llink = A

# A 오른쪽에 B 삽입
add_after(A, B)
