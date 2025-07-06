class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(left for left, right in intervals)
        end_times = sorted(right for left, right in intervals)
        end_idx, group_count = 0, 0

        for start in start_times:
            if start > end_times[end_idx]:
                end_idx += 1
            else:
                group_count += 1

        return group_count