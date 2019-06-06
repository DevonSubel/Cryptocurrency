class Transaction(object):
    # Note: per the spec, it seems like a transaction is an actual block in the blockchain
    # If so, we probably don't need a separate block class. 

    def makeReady(self, arr, index):
        if arr == u"NULL":
            return ["NULL"]
        for elem in arr:
            elem[index] = str(elem[index])
        return arr

    def __init__(self, ttype, tid, tinput, toutput, signatures):
        self.ttype = ttype
        self.tid = tid #Transation ID: SHA256 Hash 
        self.tinput = self.makeReady(tinput, 0) #Pointer to one or more prior transaction outputs
        self.toutput = self.makeReady(toutput, 1) #A set of public key-coin values
        self.signatures = [str(signatures[i]) for i in range(len(signatures))] #1 or more signatures, signed by whoever is spending coins
        
       

    def printFields(self):
        print(self.ttype)
        print(self.tid)
        print(self.tinput)
        print(self.toutput)
        print("Sig: " + str(self.signatures))
    
    def toString(self):
        return str(self.ttype) + str(self.tid) + str(self.tinput) + str(self.toutput) + str(self.signatures)

    # Figure out where to transfer, merge, join transactions
    #   # Transferring - one input to another input
        # Merging: putting two inputs from the same person into a single transaction
        # Joining: putting two inputs from different people into a single transction

    # Example input & output 
    # output = [(amount, key), (amount, key)]
    # input = [(transaction, index), (transaction, index)]











        
    



