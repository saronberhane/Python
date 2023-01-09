#Implement a stack using linked lists


#Creates a node class that will linke the datas 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creates a stack  
class Stack:
    def __init__(self):
        self.head = None
   
#checks to see if stack is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
        
#pushes items into the stack
        
    def push(self, data):
        newNode = Node(data) #creates a node object
        if self.head == None: #checks to see if there is a head(value)
            self.head = newNode
        else:
            newNode.next = self.head #assigns the added data to the next variable of the node
            self.head = newNode #the new head is the data that is added

#Returns the last item in the stack list                     
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.head.data
        
#Deletes the last item in the list
    def pop(self):
        if self.isEmpty():
            print ("Stack is empty nothing to remove")
        else:
            popData = self.head.data
            self.head = self.head.next
            return popData
        
    def printstack(self):
        
        if self.isEmpty():
            print("Stack is empty")
        else:
            nodeData = self.head #refers to node with a temp value
            while(nodeData != None): #will run till iternode is none
                print(nodeData.data, " ", end="")
                nodeData = nodeData.next    
            print()
            
        
q = Stack()
print(q.isEmpty())
q.push(2)
q.push(4)
q.push(1)
q.printstack()
q.pop()
q.printstack()
q.pop()
q.printstack()

this is to commit 
        
