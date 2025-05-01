class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted((start, end, i) for i, (start, end) in enumerate(tasks))

        processing_heap = []
        time, task_index = 0, 0
        n = len(tasks)
        total = 0
        ans = []
        
        while task_index < n or processing_heap:

            #if no task time will go forward
            if not processing_heap and time < indexed_tasks[task_index][0]:
                time = indexed_tasks[task_index][0]
            
            #Add all tasks available now
            while task_index < n and indexed_tasks[task_index][0] <= time:
                start, process, idx = indexed_tasks[task_index]
                heappush(processing_heap, (process, idx))
                task_index += 1
            
            #pick the next
            if processing_heap:
                p, index = heappop(processing_heap)
                time += p
                ans.append(index)
        return ans

        