class MedianFinder:
    def __init__(self):
        self.values = []
    
    def addNum(self, num: int) -> None:
        self.values.append(num)

    def findMedian(self) -> float:
        self.values.sort()
        n = len(self.values)
        if n % 2 == 0:
            first = int(n / 2)
            second = int(n / 2 - 1)
            ans = (self.values[first] + self.values[second]) / 2
            return ans
        else:
            index = math.floor(n / 2) 
            return self.values[index]
