class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.k = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        #0, 5/ 1, 0/ 
        print("enqueue", self.p1, self.p2)
        if self.q[self.p2] != None:
            return False
        else:
            self.q[self.p2] = value
            self.p2 = (self.p2+1) % self.k
            return True


    def deQueue(self) -> bool:
        print(self.p1, self.p2)
        if self.q[self.p1] == None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.k
            return True
        

    def Front(self) -> int:
        print(self.p1, self.p2)
        if self.q[self.p1]!=None:
            return self.q[self.p1]
        else:
            return -1
        

    def Rear(self) -> int:
        print(self.p1, self.p2)
        if self.q[self.p2-1]!=None:
            return self.q[self.p2-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.p1==self.p2 and self.q[self.p1]==None:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.p1==self.p2 and self.q[self.p1]!=None:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()