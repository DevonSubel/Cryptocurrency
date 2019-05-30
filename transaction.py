

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


# Figure out where to transfer, merge, join transactions

# Example input & output 
# output = [(amount, key), (amount, key)]
# input = [(transaction, index), (transaction, index)]


output = {}
myinput = {}

tra = Transaction("transfer", "id", "input" , "output", "signature")
tra.printFields()








        
    



