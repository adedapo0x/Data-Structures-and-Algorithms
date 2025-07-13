class MedianFinder:
    '''
    Get the median by doing normal calculations, here we use an array as the data structure. So when we initialize the class, we initialize 
    the values array in it, then to add we simply append and to findMedian we do normal median calculation. 

    This is the naive solution and here, our findMedian function has a time complexity of O(nlogn)

    '''
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
