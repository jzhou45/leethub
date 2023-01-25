class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = deque(sorted(people))
        boats = 0
        
        curr_limit = limit
        count = 0
        
        while people:
            if curr_limit >= people[-1]:
                curr_limit -= people.pop()
                count += 1
            elif curr_limit >= people[0]:
                curr_limit -= people.popleft()
                count += 1
            else:
                boats += 1
                curr_limit = limit
                count = 0
            if count == 2:
                count = 0
                boats += 1
                curr_limit = limit
        
        return boats if curr_limit == limit else boats + 1