class minQueue:
    def __init__(self):
        self.q = []

    def push(self, value: int) -> bool:
        self.q.append(value)
        value_index = len(self.q) - 1
        # 인덱스가 루트일 때 까지 비교
        while value_index > 0:
            parent_index = (value_index - 1) // 2
            if self.q[value_index] < self.q[parent_index]:
                # 스왑
                self.q[value_index], self.q[parent_index] = self.q[parent_index], self.q[value_index]
                value_index = parent_index
            else:
                break

    def pop(self):
        ret_val = self.q[0]
        self.q[0] = self.q[len(self.q) - 1]
        del self.q[len(self.q) - 1]
        value_index = 0
        while value_index < len(self.q) - 1:
            left = (value_index * 2) + 1
            right = (value_index + 1) * 2
            if self.q[value_index] > self.q[left]:
                self.q[value_index], self.q[left] = self.q[left], self.q[value_index]
                value_index = left
            elif self.q[value_index] > self.q[right]:
                self.q[value_index], self.q[right] = self.q[right], self.q[value_index]
                value_index = right
            else:
                break
        return ret_val



if __name__ == '__main__':
    minQ = minQueue()
    minQ.push(1)
    minQ.push(3)
    minQ.push(6)
    minQ.push(8)
    print(minQ.q)
    minQ.pop()
    print(minQ.q)