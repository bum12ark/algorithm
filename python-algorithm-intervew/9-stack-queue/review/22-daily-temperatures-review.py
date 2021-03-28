"""
url: https://leetcode.com/problems/daily-temperatures/
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
        answer = [0] * len(T)
        stack = []
        for idx, val in enumerate(T):
            while stack and val > T[stack[-1]]:
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        return answer


if __name__ == '__main__':
    T1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T1), [1, 1, 4, 2, 1, 1, 0, 0])
"""
[시작 체크 리스트]
[] 1시간 지났으나 발상 불가 또는 아예 다른 길
[✓] 코드 50% 정도 완성
[] 1시간 보다 더 걸려서 코드 완성
[] 코드는 다 돌아가는데 효율성에서 걸림
[] 코드 완성

[완료 후 체크 리스트]
[] 아예 모르겠음
[] 중간 정도 이해함
[✓] 완벽히 이해함
"""