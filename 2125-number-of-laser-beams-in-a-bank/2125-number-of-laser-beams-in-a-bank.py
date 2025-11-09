class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = []

        for char in bank:
            cnt = char.count("1")
            if cnt != 0:
                count.append(cnt)

        # print(count)

        if len(count) <= 1:
            return 0

        ans = 0
        temp = count[0]

        for num in count[1:]:
            ans += temp * num
            temp = num
        return ans
