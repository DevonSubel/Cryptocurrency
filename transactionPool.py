class TransactionPools(self):

    # Holds unverified and verified trasaction pools 
    # Once a transaction has been verified, move it to the verified pool

    # allTransactionsList = () //list of all transactions 
    # unverifiedPool = () //list for holding verified transactions
    # verifiedPool = ()   //list for holding verified transactions
    
    def newTransaction(self):
        # when called, read transaction from file and add it to unverified pool 
        # For each transaction, instantiate transaction object and add it to the pool

    
    def getTransaction(self):
        # return transaction from unverified pool
    
    def markTransactionAsInvalid(self):
        # Per the spec, nodes should have the ability to mark a transaction as invalid in the pool 
        # so that it gets trown out
        
    # def verifyTransaction -> maybe. mark certain transaction as verified. 
    # & move it to the verified pool 
