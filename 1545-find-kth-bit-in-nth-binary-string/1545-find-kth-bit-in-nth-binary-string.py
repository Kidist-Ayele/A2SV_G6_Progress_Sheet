class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertReverse(binary):
            arr = [i for i in binary]
            left, right = 0, len(binary) - 1
            while left <= right:
                if binary[left] == binary[right] and binary[left] == '0':
                    arr[left] = arr[right] = '1'
                elif binary[left] == binary[right] and binary[left] == '1':
                    arr[left] = arr[right] = '0'
                left += 1
                right -= 1
            return ''.join(arr)

        s = '0'
        def findString(n, s):
            if len(s) > k:
                return s
            s += '1' + invertReverse(s)
            return findString(n, s)

        result = findString(n, s)
        
        return result[k-1]



        