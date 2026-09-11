class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = []


    def get(self, i: int) -> int:
        return self.storage[i]

    def set(self, i: int, n: int) -> None:
        self.storage[i] = n

    def pushback(self, n: int) -> None:
        self.storage.append(n)
        if len(self.storage) > self.capacity:
            print(self.capacity, self.storage)
            self.resize()

    def popback(self) -> int:
        return self.storage.pop()

    def resize(self) -> None:
        self.capacity = self.capacity*2

    def getSize(self) -> int:
        return len(self.storage)
    
    def getCapacity(self) -> int:
        return self.capacity
