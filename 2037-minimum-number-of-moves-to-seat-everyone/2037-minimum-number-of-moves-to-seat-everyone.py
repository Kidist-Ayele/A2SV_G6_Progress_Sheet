class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()
        count = 0
        for i in range(n):
            count += abs(students[i] - seats[i])
        return count

        