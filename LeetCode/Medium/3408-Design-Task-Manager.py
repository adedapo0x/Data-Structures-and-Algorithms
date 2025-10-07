'''
Optimal approach here uses a hashmap and a priority queue. We use a priority queue implemented by a heap because of the execTop method
so when we initialize with the constructor, we store in dict like this: {taskId: [priority, userId]},
also we store in our heap, [-priority, -taskId] since python natively supports only minheap and here what we need is a maxheap

when we add, we update both the dict and the heap, when we want to edit, we edit the value in the dict and push it with it new value to the heap, remember that, that 
particular task Id would already exists in the heap since we are editing, but since there is no way to aaccess it, it becomes stale data in the heap
to remove also, we only delete from the hashmap, no way to remove from heap, so we leave that task in the heap also allowing it to become stale data

so now to perform execTop, which is the reason we have been maintaining a heap in the first place. Note that we store in the heap the priority and then the task ID because
we are trying to get the highest priority, if multiple have same, the higher task ID serves as the tie breaker. so why we store priority then taskID in that order.
so we run a while loop while the heap is not empty. what we want to get is the task with the highest priority that still exists in the hashmap and that contains the up to date value of what is in the hashmap
ie we do not want stale data that is in the heap. we check safely for if the task still exists by using the get method, and put a default of [-1, -1] if it doesn't. we also check that it is not outdated
priority that is there by comparing the priority popped with what is in the hashmap. we would keep popping until we find a task that is not stale and then we can return. return -1 if not possible

if n is the number of tasks at initialization, and m is the number of subsequent tasks
TC: O(N) to instantiate - heapify is O(N) cause of bottom up buildup.
    add and edit are both O(log(N + M)) due to the heap operation in both methods. the heap contains N + M number of tasks
    rmv is O(1)
    execTop is O(log(N + M)) cause of the popping from the heap
SC: O(N + M) due to the heap and the hashmap
'''

import heapq
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.taskDict = {}
        self.taskHeap = []
        for userId, taskId, priority in tasks:
            self.taskDict[taskId] = [priority, userId]
            self.taskHeap.append([-priority, -taskId])
        heapq.heapify(self.taskHeap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskDict[taskId] = [priority, userId]
        heapq.heappush(self.taskHeap, [-priority, -taskId])
        
    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskDict[taskId][0] = newPriority
        heapq.heappush(self.taskHeap, [-newPriority, -taskId])
        
    def rmv(self, taskId: int) -> None:
        del self.taskDict[taskId]
        
    def execTop(self) -> int:
        while self.taskHeap:
            priority, taskId = heapq.heappop(self.taskHeap)
            priority, taskId = -priority, -taskId # since we had to store as negative to get maxheap behaviour

            if self.taskDict.get(taskId, [-1, -1])[0] == priority:
                userId = self.taskDict[taskId][1]
                del self.taskDict[taskId]
                return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()




'''
gives TLE on Leetcode
Bruteforce approach, uses only a hashmap, we store { taskID: [userID, priority] }
so we only update the hashmap when each operation is called

TC: to instantiate O(N), add, edit and delete is O(1), execTop is O(N + M)
where N is the initial number of tasks given to initialize with and M is the number of subsequent tasks added
the reason why this is inefficient is because of the execTop method, the (N + M) can grow up to 2 * 10^5 which is pretty expensive
'''
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.taskDict = {}
        for task in tasks:
            self.taskDict[task[1]] = [task[0], task[2]]
    
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskDict[taskId] = [userId, priority]
        
    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskDict[taskId][1] = newPriority
        
    def rmv(self, taskId: int) -> None:
        del self.taskDict[taskId]
        

    def execTop(self) -> int:
        maxPriority = -1
        maxId = -1
        maxUser = -1
        for key, val in self.taskDict.items():
            if val[1] > maxPriority:
                maxPriority = val[1]
                maxId = key
                maxUser = val[0]
            elif val[1] == maxPriority:
                if key > maxId:
                    maxPriority = val[1]
                    maxId = key
                    maxUser = val[0]
        if maxId != -1:
            del self.taskDict[maxId]
        return maxUser



# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()