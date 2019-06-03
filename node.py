class node(object):

    import hashlib
    import random

    def __init__(self, transactionPool):
        self.pool = transactionPool


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
    
    def verifyMinedBlock(self, block):
        # check that new block mined by network has valid transactions and 
        # that the proof is work is correct ie it has the right hash
        # To do that, hash the transaction (with some fields blanked out) to check that
        # the hash matches 
    
    def solvedPuzzle(self, block, nonce):
        # Run proof of work
        # hash the block with randomVal until the hash has n number of zeroes
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
        # Check the node network to see if a block been solved. If so, stop will stop mining curr block
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


    def mineBlock(self, block):
        # Begin mining block
        while True:
            randint = self.random.random()
            block, nonce, hval = self.solvedPuzzle(block, randint)
            if(block, nonce, hval != "", "", ""):
                self.broadcastNewBlock()
            
            if(self.newBlockSolvedByNetwork()):
                # Check the newtwork for new blocks that have been solved. stop the current mining 
                self.receiveNewBlocks()
                return 
    
    def run(self):
        # main function for node 

        # Get ledger from network
        # verify transactions in ledger

        # while True:
        #     transaction = self.getTransactionFromPool()
        #     if(self.validTransaction(transaction) != "TRUE"):
        #     block = self.createBaseBlock(transaction)
        #     mineBlock(block)
        #     sleep(5) #Per the spec, wait 5 seconds

        # node class test:
        print("hello from node")

    