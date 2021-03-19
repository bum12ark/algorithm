"""
* 완주하지 못한 선수
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예
- Example 1
Input: participant = ["leo", "kiki", "eden"], completion = ["eden", "kiki"]
Output: "leo"
- Example 2
Input: participant = ["marina", "josipa", "nikola", "vinko", "filipa"], completion = ["josipa", "filipa", "marina", "nikola"]
Output: "vinko"
- Example 3
Input: participant = ["mislav", "stanko", "mislav", "ana"], completion = ["stanko", "ana", "mislav"]
Output: "mislav"

입출력 예 설명
- 예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
- 예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
- 예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
"""
import collections
from typing import List


class Solution:
    def solution(self, participant: List[int], completion: List[int]) -> str:
        result = collections.Counter(participant) - collections.Counter(completion)
        return result.most_common(1)[0][0]


    def programmers_solution(self):
        pass


if __name__ == '__main__':
    solution = Solution()
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(solution.solution(participant, completion))
