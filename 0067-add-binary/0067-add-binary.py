class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        left, right = len(a) - 1, len(b) - 1
        ans = []

        while left >= 0 and right >= 0:
            if a[left] != b[right] and not carry:
                ans.append("1")
            elif a[left] != b[right] and carry:
                ans.append("0")
            else:
                if a[left] == "1":
                    if not carry:
                        ans.append("0")
                    else:
                        ans.append("1")
                    carry = 1
                else:
                    if not carry:
                        ans.append("0")
                    else:
                        ans.append("1")
                    carry = 0
            left -= 1
            right -= 1

        while left >= 0:
            if carry and a[left] == "1":
                ans.append("0")
            elif carry and a[left] == "0":
                ans.append("1")
                carry = 0
            else:
                ans.append(a[left])
            left -= 1

        while right >= 0:
            if carry and b[right] == "1":
                ans.append("0")
            elif carry and b[right] == "0":
                ans.append("1")
                carry = 0
            else:
                ans.append(b[right])
            right -= 1
            
        if carry:
            ans.append("1")

        ans.reverse()

        return ''.join(ans)







        