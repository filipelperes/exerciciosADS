class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFirst(self, item):
        self.items.append(item)

    def addLast(self, item):
        self.items.insert(0, item)

    def removeFirst(self):
        return self.items.pop()

    def removeLast(self):
        return self.items.pop(0)

    def length(self):
        return len(self.items)

d = Deque()

print(bool(d.isEmpty()))

print(d.length())

d.addFirst(1)
print(list(d.items))

d.addFirst(7)
print(list(d.items))

d.addLast(4)
print(list(d.items))

d.addLast(8)
print(list(d.items))

d.removeFirst()
print(list(d.items))

d.removeLast()
print(list(d.items))

print(list(d.items))
