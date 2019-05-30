

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
        # 

    # def verifyTransaction -> maybe. mark certain transaction as verified. 
    # & move it to the verified pool 



class driver(self):
    

    def __init__(self, numNodes, transactionsFile):
        self.numNodes = numNodes
        self.transactionsFile = transactionsFile


    # create genesis block ie initial blockchain 


    # instantiate transaction pools
    # Make sure that unverified pool data struct can be read by all nodes
    pools = TransactionPools()

    
    # Launch numNodes number of nodes. pass in initial difficulty, pool reference
    # Make sure that pool reference can be modified by the nodes. 
    # Figure out how first node will get ledger. probably pass in genesis block to every node
    # Per the spec, we might need to be able to set the intent of a node: malicious vs cooperative


    while True:
        # Call pool.newTransaction() at random times to add transactions to unverified pool
        # maybe communicate with nodes in order to print out current status of blockchain
        # and to print out when new blocks have been solved 




class node(object):

    def getLedgerFromNetwork(self):
        print("getting current ledger from network")
        # Each node will have to get a copy of the ledger
        # Figure out how to get current ledger for new node entering network
        # detect any forks in the ledger. atuomatically switch to longest chain 
        # detect any forks 

    def getTransactionFromPool(self):
        # get a transactiosn at random from pool 
        # verify the transaction by running trhough the ledger to check balance
    
    
    def validTransaction(self):
        # Make sure that a transaction has not been double-spend ie been used as the input to other transactions more than once. 
        # run through ledger to verify that transaction is valid and input has not been already spent

        # return true if transaction is valid

    
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

    
arr = [1] * 10

nd = node()

nd.printArr()

for c in arr:
    print(c)

arr = [3] * 10

nd.printArr()





