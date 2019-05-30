class driver(self):
    

    def __init__(self, numNodes, transactionsFile):
        self.numNodes = numNodes
        self.transactionsFile = transactionsFile


    # create genesis block ie initial blockchain 


    # instantiate transaction pools
    # Make sure that unverified pool data struct can be read by all nodes
    pools = TransactionPools()

    
    # Launch numNodes number of nodes. pass in pool reference
    # Make sure that pool reference can be modified by the nodes. 
    # Figure out how first node will get ledger. probably pass in genesis block to every node
    # Per the spec, we might need to be able to set the intent of a node: malicious vs cooperative


    while True:
        # Call pool.newTransaction() at random times to add transactions to unverified pool
        # maybe communicate with nodes in order to print out current status of blockchain
        # and to print out when new blocks have been solved 



pool = Transaction(transactionFile)

driver(, pool )

