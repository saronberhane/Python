#Implement a queue using linked lists

#Creates a node class that will linke the datas 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None#Creates a node class that will linke the datas 


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

#checks to see if stack is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode #updates the reference tail node
        
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            newNode = self.head
            self.head = newNode.next
            
        if(self.head == None):
            self.tail = None
            
    def printqueue(self):
        
        if self.isEmpty():
            print("Queue is empty")
        else:
            nodeData = self.head #refers to node with a temp value
            while(nodeData != None): #will run till iternode is none
                print(nodeData.data, " ", end="")
                nodeData = nodeData.next    
            print()     
    
    
        
q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(2)
q.printqueue()
q.dequeue()
q.printqueue()
q.dequeue()
q.enqueue(5)
q.printqueue()
