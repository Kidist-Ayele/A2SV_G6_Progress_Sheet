class Solution:
    def intToRoman(self, num: int) -> str:
        romans_dict = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 
            50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 
            900: 'CM', 1000: 'M'
        }
        roman_arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        ans = []

        for i in range(13):
            if num >= roman_arr[i]:
                ans.append((num// roman_arr[i]) * romans_dict[roman_arr[i]])
            num %= roman_arr[i]
        return ''.join(ans)




        