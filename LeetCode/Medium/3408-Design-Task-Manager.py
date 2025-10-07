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