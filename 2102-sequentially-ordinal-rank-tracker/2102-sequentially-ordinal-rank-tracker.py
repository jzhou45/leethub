from sortedcontainers import SortedList

class SORTracker:

    def __init__(self):
        self.arr = SortedList([])
        self.k = -1
        
    def add(self, name: str, score: int) -> None:
        self.arr.add((-score, name))

    def get(self) -> str:
        self.k += 1
        return self.arr[self.k][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()