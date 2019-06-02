class Transaction(object):
    
    def __init__(self, ttype, tid, tinput, toutput, signature):
        self.ttype = ttype
        self.tid = tid
        self.tinput = tinput
        self.toutput = toutput
        self.signature = signature


    def printFields(self):
        print(self.ttype)
        print(self.tid)
        print(self.tinput)
        print(self.toutput)
    
    def toString(self):
        return str(self.ttype) + str(self.tid) + str(self.tinput) + str(self.toutput) + str(self.signature)

# Figure out where to transfer, merge, join transactions
#   # Transferring - one input to another input
    # Merging: putting two inputs from the same person into a single transaction
    # Joining: putting two inputs from different people into a single transction

# Example input & output 
# output = [(amount, key), (amount, key)]
# input = [(transaction, index), (transaction, index)]


output = {}
myinput = {}

tra = Transaction("transfer", "id", "input" , "output", "signature")
tra.printFields()








        
    



