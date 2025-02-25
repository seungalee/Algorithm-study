class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None]*k
        self.k = k
        self.p1 = 0
        self.p2 = 0

    def insertFront(self, value: int) -> bool:
        if self.q[(self.p1-1)%self.k] == None:
            self.p1 = (self.p1-1) % self.k
            self.q[self.p1] = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.q[self.p2] == None:
            self.q[self.p2] = value
            self.p2 = (self.p2+1) % self.k
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.q[self.p1] != None:
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.k
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.q[self.p2-1] != None:
            self.p2 = (self.p2-1) % self.k
            self.q[self.p2] = None
            return True
        else:
            return False
        
    def getFront(self) -> int:
        if self.q[self.p1] != None:
            return self.q[self.p1]
        else:
            return -1
        
    def getRear(self) -> int:
        if self.q[self.p2-1] != None:
            return self.q[self.p2-1]
        else:
            return -1
        
    def isEmpty(self) -> bool:
        return (self.p1 == self.p2 and self.q[self.p1] == None)

    def isFull(self) -> bool:
        return (self.p1 == self.p2 and self.q[self.p1] != None)
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()