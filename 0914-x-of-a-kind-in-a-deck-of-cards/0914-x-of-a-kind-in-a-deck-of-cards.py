class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        count = Counter(deck)
        temp = count[deck[0]]
        
        for key, val in count.items():
            temp = math.gcd(temp, val)
        return temp >= 2
