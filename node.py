class node(object):

    import hashlib
    import random

    def __init__(self, verifiedTransactionPool, unverifiedTransactionPool):
        self.verifiedTransactionPool = verifiedTransactionPool
        self.unverifiedTransactionPool = unverifiedTransactionPool

    def getLedgerFromNetwork(self):
        print("getting current ledger from network")
        # Each node will have to get a copy of the ledger
        # Figure out how to get current ledger for new node entering network
        # detect any forks in the ledger. atuomatically switch to longest chain 
        # detect any forks 
        return 0
    
    def validTransaction(self, transaction):
        # Make sure that a transaction has not been double-spent ie been used as the input to other transactions more than once. 
        # run through ledger to verify that transaction is valid and input has not been already spent

        # return true if transaction is valid

        totalInput = 0
        totalOutput = 0
        tinput = transaction.tinput
        toutput = transaction.toutput
        signature transaction.signature

        # Verify 
        for tTinput in tinput: # For each Input do:
            if tTinput[1] < 0.1: # Check that it's not less than min amount
                return False

            vOutput = self.verifiedTransactionPool[tTinput[0]].toutput[0] # Get The Output pointed to
            if vOutput == tTinput[1]: # Check that value is equal
                totalInput += vOutput # Add the amount to the cumulative input in case input is from different places
                self.verifiedTransactionPool[tTinput[0]].toutput[0] = -1 # Change Output so no future transaction can point to it
            else:
                return False # If they are not equal return false
        
        for output in toutput: # Accumulate all output
            totalOutput += output[0]

        if totalInput != totalOutput: # Check that output and input are the same
            return False
                    
        return True # If this point has been reached the transaction is verified


    def getTransactionFromPool(self):
        index = self.random.randint(0, len(self.unverifiedTransactionPool)-1)
        transaction = self.unverifiedTransactionPool[index]
        
        return transaction
    

    
    def solvedPuzzle(self, block, nonce):
        # Run proof of work
        # hash the block with randomVal until the hash has n number of zeroes. denoted by difficulty argument
        # if the puzzle is solved, return the block + iterator value and the hash. this is the new block
        hval = self.hashlib.sha256(block + str(nonce))
        if(hval < 0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF):
            return block, nonce, hval 
        else:
            return "", "", ""



    def createBaseBlock(self, transaction):
        # creates base block from transaction to run it through the puzzle 
        return 0


    # # infinite loop that calls mineBlock 


    def mineBlock(self):
        while len(self.unverifiedTransactionPool) > 0:
            verlen = len(self.verifiedTransactionPool)
            transaction = self.getTransactionFromPool()

            if(self.validTransaction(transaction) != "TRUE"):
                return 

            # Begin mining block
            block = self.createBaseBlock(transaction)
            while True:
                newlen = len(self.verifiedTransactionPool)
                if(newlen > verlen):
                    break 
                randint = self.random.random()
                block, nonce, hval = self.solvedPuzzle(block, randint)
                if(block, nonce, hval != "", "", ""):
                    self.unverifiedTransactionPool.remove(transaction)
                    self.verifiedTransactionPool.append(transaction)
                    break
                

    