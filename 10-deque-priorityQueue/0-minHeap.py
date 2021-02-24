class MinHeap():
    def __init__(self):
        self.q = []

    def _parent(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def _left(self, parent_index: int) -> int:
        return (parent_index * 2) + 1

    def _right(self, parent_index: int) -> int:
        return (parent_index + 1) * 2

    def insert(self, n: int) -> bool:
        # 인덱스의 마지막에 삽입처리
        self.q.append(n)
        pos = len(self.q) - 1
        while pos > 0:
            parent = self._parent(pos)
            if self.q[pos] < self.q[parent]:
                # 스왑
                self.q[pos], self.q[parent] = self.q[parent], self.q[pos]
                pos = parent
            else:
                break
        return True

    def delete(self) -> int:
        if not self.q:
            return -1
        # 루트 노드에 마지막 노드를 삽입
        root_val = self.q[0]
        self.q[0] = self.q[len(self.q) - 1]
        del self.q[len(self.q) - 1]
        pos = 0

        # 왼쪽 노드가 존재한다면.
        while self._left(pos) < len(self.q):
            min_index = self._left(pos)
            # 오른쪽 노드가 존재 하며 왼쪽 노드의 값보다 크다면.
            if self._right(pos) < len(self.q) and self.q[min_index] > self.q[self._right(pos)]:
                min_index = self._right(pos)

            if self.q[pos] > self.q[min_index]:
                # 스왑
                self.q[pos], self.q[min_index] = self.q[min_index], self.q[pos]
                pos = min_index
            else:
                break

        return root_val


if __name__ == '__main__':
    minQ = MinHeap()
    minQ.insert(1)
    minQ.insert(3)
    minQ.insert(6)
    minQ.insert(8)
    print(minQ.q)
    print(minQ.delete())
    print(minQ.q)
    print(minQ.delete())
    print(minQ.q)