class Queue:
    def __init__(self):
        self.items = {}
        self.tail = 0
        self.head = 0
    
    def isEmpty(self):
        return self.tail - self.head == 0

    def enqueue(self, value):
        self.items[str(self.tail)] = value
        self.tail += 1
    
    def dequeue(self):
        if (self.isEmpty()):
            return 
        item = self.items[str(self.head)]
        del self.items[str(self.head)]
        self.head += 1
        return item
    
    def printQueue(self):
        print(self.items)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.printQueue()
queue.dequeue()
queue.printQueue()