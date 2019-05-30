# Devon making the input files. reading input files
# For every transaction in file, instantiate transaction object
# Add object to unverified transaction pool


# Figure out how to launch threads 

class node(object):

    def getLedgerFromNetwork():
        print("getting current ledger from network")
        # Each node will have to get a copy of the ledger
        # Figure out how to get current ledger for new node entering network
        # detect any forks in the ledger. atuomatically switch to longest chain 

    def getTransactionFromPool(self):
        # get a transactiosn at random from pool 
        # verify the transaction by running trhough the ledger to check balance
    
    
    def validTransaction(self):
        # Make sure that a transaction has not been double-spend ie been used as the input to other transactions more than once. 
        # run through ledger to verify that transaction is valid and input has not been already spent

        # return true if transaction is valid

    
    def solvedPuzzle(block, iterator, difficulty):
        # Run proof of work
        # hash the block with iterator until the hash has a certain number of zeroes. denoted by difficulty
        # if the puzzle is solved, return the block + iterator value and the hash. this is the new block

    def createBaseBlock(transaction):
        # creates base block from transaction to run it through the puzzle 

    def blockSolved():
        # Check the node network to see if a block  has aleady been solved. 


    def mineBlock(self):
        transaction = getTransactionFromPool(self)

        if(validTransaction(transaction) != "TRUE"):
            return 

        # Begin mining block
        block = createBaseBlock(transaction)
        for iterator in range(5000):

            if(solvedPuzzle(block, iterator)):
                broadcastNewBlock()
            
            if(newBlockSolvedByNetwork()):
                # Check the newtwork for new blocks that have been solved. stop the current mining 
                receiveNewBlocks()
                continue

    # need to broadcast the blocks to other nodes 
    def broadcastNewBlock(self):
        print("SOlved puzzle. Broadcasting new block")


    # Receive blocks from other nodes and update local ledger to 
    def receiveNewBlocks(self):
        print("checking for new solved blocks broadcast to newtwork")




















    


arr = [1] * 10

nd = node()

nd.printArr()

for c in arr:
    print(c)

arr = [3] * 10

nd.printArr()





