class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=defaultdict(int)
        for i in range(len(numbers)):
            val=target-numbers[i]
            if val in seen:
                return [seen[val],i+1]
            else:
                seen[numbers[i]]=i+1
        return []