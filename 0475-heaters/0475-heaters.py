class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(radius):
            prev = houses[0] - 1

            for heater in heaters:
                prev_house = heater - radius
                next_house = heater + radius

                if prev_house > prev and prev_house - prev > 1:
                    return False
                prev = next_house

            
            return prev >= houses[-1]

        left, right = 0, max(max(houses), max(heaters))
        ans = right

        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

        