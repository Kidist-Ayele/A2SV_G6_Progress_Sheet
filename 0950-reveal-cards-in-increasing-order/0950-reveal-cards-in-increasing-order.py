class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        queue = deque([deck[0]])

        for num in deck[1:]:
            x = queue.pop()
            queue.appendleft(x)
            queue.appendleft(num)
        return list(queue)


            
        