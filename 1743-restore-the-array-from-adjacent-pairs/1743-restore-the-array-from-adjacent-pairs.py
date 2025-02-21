class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = defaultdict(list)

        for a, b in adjacentPairs:
            pairs[a].append(b)
            pairs[b].append(a)

        result = []
        
        for key in pairs:
            if len(pairs[key]) == 1:
                start = key
                break

        prev = None
        curr = start

        for _ in range(len(adjacentPairs) + 1):
            result.append(curr)
            next_val = pairs[curr][0] if len(pairs[curr]) == 1 or pairs[curr][0] != prev else pairs[curr][1]

            prev, curr = curr, next_val

        return result
        