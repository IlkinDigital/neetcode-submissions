class MinStack:

    def __init__(self):
        self.mins = deque([])
        self.buffer = deque([]) 
        

    def push(self, val: int) -> None:
        self.buffer.append(val)
        if len(self.mins) == 0 or self.mins[-1] > val:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.buffer.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.buffer[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
