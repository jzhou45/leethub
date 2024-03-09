from collections import deque 

class Solution:    
    def kthFactor(self, n: int, k: int) -> int:
        firstHalf = deque()
        secondHalf = deque()
        
        for i in range(1, n + 1):
            if len(secondHalf) and secondHalf[0] == i: break
            
            if n % i == 0:
                firstHalf.append(i)
                div = int(n/i)
                if i != div:
                    secondHalf.appendleft(div)
        
        dequeLen = len(firstHalf)
        if k > dequeLen:
            k -= dequeLen
        else:
            return firstHalf[k - 1]
        
        if k > len(secondHalf):
            return -1
        
        return secondHalf[k - 1]