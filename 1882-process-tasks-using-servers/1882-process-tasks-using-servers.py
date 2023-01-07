class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = [0] * len(tasks)
        
        available = [(servers[i], i) for i in range(len(servers))] #weight, ith server
        heapq.heapify(available)
        
        unavailable = [] #time server becomes free, weight, ith server
        
        time = 0
        for i in range(len(tasks)):
            time = max(time, i)
            
            #in case all servers are being used, advance time
            if len(available) == 0:
                time = unavailable[0][0]
                
            while unavailable and time >= unavailable[0][0]:
                _, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
                
            weight, index = heapq.heappop(available)
            ans[i] = index
            heapq.heappush(unavailable, (time + tasks[i], weight, index))
            
        return ans