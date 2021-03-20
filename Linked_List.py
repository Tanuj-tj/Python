class Node:
    data = None
    next_node = None
    
    def __init__(self,data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" %self.data
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while(current):  # current != 0
            count+=1
            current=current.next_node
        return count
        
    def add(self,data):
        """
        Adds new node containing data at the head of list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self,key):
        """
        Search for the first node containing data that matches the key 
        """
        current = self.head
        
        while(current):   # current != None
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
        
    def insert(self,data,index):
        """
        Insert a new Node containing data at index position 
        Takes O(N) => finding the index and the inserting
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
            
            
    def remove(self,key):
        """ 
        Removes Node containing data that matches the key
        Returns the node or None if Key does't exist
        Complexity => O(N)
        """
        current = self.head
        previous = None
        found = False
        
        while(current and not found):
            if(current.data==key and current is self.head):
                found = True
                self.head = current.next_node
                
            elif(current.data==key):
                found=True
                previous.next_node = current.next_node
                
            else:
                previous = current
                current = current.next_node
        return current
        
    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """
        
        nodes = []
        current = self.head
        
        while(current):
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '->'.join(nodes)
        
l = LinkedList()
#N1 = Node(10)
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
print(l)
l.remove(2)
print(l)