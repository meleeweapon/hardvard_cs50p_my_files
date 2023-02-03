# almost finished
class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value

        self.next = next

class LinkedList:
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.len = 0

        headNotNone = head is not None

        if headNotNone:
            temp = head
            self.len = 1
            while temp.next is not None:
                self.len += 1
                temp = temp.next
        
        self.tail = temp if headNotNone else self.head
    
    def append(self, value) -> None:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        
        self.len += 1
    
    def validIndex(self, ind):
        if ind >= self.len or ind < 0:
            raise IndexError
            return False
        return True

    def get(self, ind):
        self.validIndex(ind)
        temp = self.head
        while ind > 0:
            temp = temp.next
            ind -= 1
        return temp
    
    def getValue(self, ind):
        return self.get(ind).value
    
    def set(self, ind, value):
        temp = self.get(ind)
        temp.value = value
    
    def unshift(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        if self.head.next is None:
            self.tail = self.head
        self.len += 1
    
    def shift(self):
        if self.len < 1:
            raise IndexError
        ret = self.head.value
        self.head = self.head.next
        self.len -= 1
        return ret
    
    def remove(self, ind):
        self.validIndex(ind)
        if ind == 0:
            return self.shift()
        temp = self.get(ind - 1)
        ret = temp.next.value
        temp.next = temp.next.next
        if ind == self.len - 1:
            self.tail = temp
        self.len -= 1
        return ret
    
    def insert(self, ind, value):
        self.validIndex(ind)
        if ind == 0:
            self.unshift(value)
        else:
            temp = self.get(ind - 1)
            temp2 = temp.next
            temp.next = Node(value)
            temp.next.next = temp2
        self.len += 1
    
    def pop(self):
        if self.len == 1:
            ret = self.get(0).value
            self.head = None
            self.tail = self.head 
        else:
            temp = self.get(self.len - 2)
            ret = temp.next.value
            temp.next = None
            self.tail = temp
        self.len -= 1
        return ret
    
    def arr(self) -> list:
        result = []
        temp = self.head
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        return result

def linkedListFromArr(arr) -> LinkedList:
    if(len(arr) < 1):
        return LinkedList()
    
    head = None
    for x in range(len(arr) - 1, -1, -1):
        head = Node(arr[x], head)
    
    return LinkedList(head)

def linkedListFromArr2(arr) -> LinkedList:
    if(len(arr) < 1):
        return LinkedList()
    
    temp = LinkedList()
    for x in range(len(arr)):
        temp.append(arr[x])
    
    return temp