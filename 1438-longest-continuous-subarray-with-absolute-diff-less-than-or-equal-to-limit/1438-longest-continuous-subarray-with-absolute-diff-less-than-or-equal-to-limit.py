class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue = deque()
        max_queue = deque()
        min_queue = deque()

        ans = 0
        left = 0
        for right, num in enumerate(nums):
            queue.append(num)

            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)

            while min_queue and min_queue[-1] > num:
                min_queue.pop()
            min_queue.append(num)

            while max_queue[0] - min_queue[0] > limit:
                left += 1
                delete = queue.popleft()

                if delete == max_queue[0]:
                    max_queue.popleft()
                if delete == min_queue[0]:
                    min_queue.popleft()
            
            ans = max(ans, right - left + 1)

        return ans
