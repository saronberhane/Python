#Implement a deque using linked lists

#Creates a node class that will linke the datas
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    

class Deque:
    def __init__(self):
        self.front = None
        self.size = 0
    
    def isEmpty(self):
        if self.size == 0:
           return True
        else:
            return False
    
    def size(self):
        return self.size
    
    def addFront(self, data):
        newNode = Node(data)
        if self.front == None:
            self.front = newNode
            self.size = self.size + 1
        else:
            newNode.next = self.front
            self.front = newNode
            self.size = self.size + 1
        
    def addRear(self, data):
        newNode = Node(data)
        if self.front == None:
            self.front = newNode
            self.size = self.size + 1
        else:
            currNode = self.front
            while currNode.next != None:
                currNode = currNode.next
            currNode.next = newNode
            self.size = self.size + 1
    
    def removeFront(self):
        if self.size == 0:
            print("Deque is empty")
        else:
            newNode = self.front
            self.front = newNode.next
            self.size = self.size + 1
            
        if(self.front == None):
            self.rear = None
    
    def removeRear(self):
        if self.size == 0:
            print("Deque is empty")
        else:
            currNode = self.front
            prev = None
            while currNode.next != None:
                prev = currNode
                currNode = currNode.next
            prev.next = currNode.next
            self.size = self.size + 1  
            
        if(self.front == None):
            self.rear = None
    
    def printdeque(self):
        
        if self.size == 0:
            print("Deque is empty")
        else:
            nodeData = self.front #refers to node with a newNode value
            while(nodeData != None): #will run till iternode is none
                print(nodeData.data, " ", end="")
                nodeData = nodeData.next    
            print() 
    
        
q = Deque()
print(q.isEmpty())
q.addFront(1)
q.addFront(2)
q.addRear(5)
q.addRear(7)
q.printdeque()
q.removeRear()
q.removeFront()
q.printdeque()
  
        