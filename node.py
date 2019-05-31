unverifiedTransactionPool = []
class node(object):

    import hashlib
    import random

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
        return 0

    def getTransactionFromPool(self):
        global unverifiedTransactionPool
        index = self.random.randint(0, len(unverifiedTransactionPool)-1)
        transaction = unverifiedTransactionPool[index]
        
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

    def newBlockSolvedByNetwork(self):
        # Check the node network to see if a block  has aleady been solved. 
        # will  probably get updated ledger or maybe just new block

        # return true if new block
        # detect forks 
        return 0

    def broadcastNewBlock(self):
        # Broadcast the blocks to other nodes since theyre threads in same program
        # Figure out how to do this
        return 0
        


    # Receive blocks from other nodes and update local ledger to 
    def receiveNewBlocks(self):
        print("checking for new solved blocks broadcast to newtwork")

    # # infinite loop that calls mineBlock 


    def mineBlock(self):
        transaction = self.getTransactionFromPool()

        if(self.validTransaction(transaction) != "TRUE"):
            return 

        # Begin mining block
        block = self.createBaseBlock(transaction)
        while True:
            randint = self.random.random()
            if(self.solvedPuzzle(block, randint) != "", "", ""):
                self.broadcastNewBlock()
            
            if(self.newBlockSolvedByNetwork()):
                # Check the newtwork for new blocks that have been solved. stop the current mining 
                self.receiveNewBlocks()
                return 

    