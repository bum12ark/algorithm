"""
* 일일 온도
매일 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
- 입력
T = [73, 74, 75, 71, 69, 72, 76, 73]
- 출력
[1, 1, 4, 2, 1, 1, 0, 0]
- 설명
화씨 73도인 첫째 날에서 더 따뜻한 날을 위해서는 하루만 기다리면 된다.
바로 다음날인 둘째 날은 화씨 74도다. 마찬가지로 더 따뜻한 날을 위해서는 셋째 날까지 하루만 기다리면된다.
셋째 날은 화씨 75도이며 더 따뜻한 날을 위해서는 4일을 더 기다려야 일곱째 날 화씨 76도가 된다.
일곱째 날과 여덟째 날은 더 이상 따뜻한 날이 없으므로 각각 0이다.
"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(T)
        for i, current in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and current > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer




if __name__ == '__main__':
    solution = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    # T = [75, 71, 76]
    print(solution.dailyTemperatures(T))