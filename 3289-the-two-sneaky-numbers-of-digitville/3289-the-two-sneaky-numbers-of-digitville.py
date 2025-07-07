class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        result = []
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                result.append(num)
        return result

        