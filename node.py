class node(object):
    
    def getLedgerFromNetwork(self):
        print("getting current ledger from network")
        # Each node will have to get a copy of the ledger
        # Figure out how to get current ledger for new node entering network
        # detect any forks in the ledger. atuomatically switch to longest chain 
        # detect any forks 
    
    def validTransaction(self):
        # Make sure that a transaction has not been double-spent ie been used as the input to other transactions more than once. 
        # run through ledger to verify that transaction is valid and input has not been already spent

        # return true if transaction is valid

    def getTransactionFromPool(self):
        # get a transactiosn at random from pool 
        # verify the transaction calling validTransaction()
        # if transaction is invalid, mark it using the method in TransactionPools object
        # repeat until transaction is valid and return it
    

    
    def solvedPuzzle(block, nonce):
        # Run proof of work
        # hash the block with randomVal until the hash has n number of zeroes. denoted by difficulty argument
        # if the puzzle is solved, return the block + iterator value and the hash. this is the new block

    def createBaseBlock(transaction):
        # creates base block from transaction to run it through the puzzle 

    def newBlockSolvedByNetwork(self):
        # Check the node network to see if a block  has aleady been solved. 
        # will  probably get updated ledger or maybe just new block

        # return true if new block
        # detect forks 

    def broadcastNewBlock(self):
        # Broadcast the blocks to other nodes since theyre threads in same program
        # Figure out how to do this
        


    # Receive blocks from other nodes and update local ledger to 
    def receiveNewBlocks(self):
        print("checking for new solved blocks broadcast to newtwork")

    # infinite loop that calls mineBlock 


    def mineBlock(self):
        transaction = getTransactionFromPool(self)

        if(validTransaction(transaction) != "TRUE"):
            return 

        # Begin mining block
        block = createBaseBlock(transaction)
        while True:
            random = random.random()
            if(solvedPuzzle(block, random)):
                broadcastNewBlock()
            
            if(newBlockSolvedByNetwork()):
                # Check the newtwork for new blocks that have been solved. stop the current mining 
                receiveNewBlocks()
                return 

    