class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [(i) for i in range(1, 1001)]
        self.arr = set(self.arr)

    def popSmallest(self) -> int:
        res = min(self.arr)
        self.arr.remove(res)
        return res

    def addBack(self, num: int) -> None:
        self.arr.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)