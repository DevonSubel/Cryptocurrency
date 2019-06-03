class Transaction(object):
    # Note: per the spec, it seems like a transaction is an actual block in the blockchain
    # If so, we probably don't need a separate block class. 

    def __init__(self, ttype, tid, tinput, toutput, signatures, prevTransHash):
        self.ttype = ttype
        self.tid = tid #Transation ID: SHA256 Hash 
        self.tinput = tinput #Pointer to one or more prior transaction outputs
        self.toutput = toutput #A set of public key-coin values
        self.signatures = signatures #1 or more signatures, signed by whoever is spending coins
        self.prevTransHash = prevTransHash #Hash pointer to a previous transaction
 

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








        
    



