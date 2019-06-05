import sys
sys.stdout.write('.')

class Node(object):
    
    def __init__(self, data):   
        self.left = None
        self.right = None
        self.data = data

    
    def printTree(self):
        if self.left:
            print("left: ")
            self.left.printTree()
        
        print("root: " + str(self.data))
        if self.right:
            print("right: ")
            self.right.printTree()

    
    def insert(self, data):
    # Compare input data value to data value at this node to determine whether it 
    # will on the right or the left side of tree
        
        #If self.data is not empty
        if self.data: 
            if data < self.data:
                if self.left is None:
                    print("New node on left")
                    self.left = Node(data)
                else:
                    print("Curr node on left")
                    self.left.insert(data)
            else: 
                if self.right is None:
                    print("New node on right")
                    self.right = Node(data)
                else:
                    print("Curr node on right")
                    self.right.insert(data)
        
        #Else this is a new node
        else:
            self.data = data




root = Node(10)

# root.printTree()
root.insert(20)
root.insert(5)
root.insert(30)
root.printTree()
