class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(num):
            count = 1
            cur_position = position[0]

            for i in range(1, len(position)):
                if position[i] - cur_position >= num:
                    count += 1
                    cur_position = position[i]
                if count == m:
                    return True
            return False 
        
        left, right = 1, position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1

        return ans
        