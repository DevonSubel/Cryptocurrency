from threading import Thread
import os
# from node import *
# from transaction import *
# from transactionPool import *
# from blockChain import *
class testNode(object):    
    def run(self, arr):
        for a in arr: 
            print(a)   

        for i in range(len(arr)):
            arr[i] = 11
        

class Driver(object):
    
    def __init__(self, numNodes, transactionsFile):
        self.numNodes = numNodes
        self.transactionsFile = transactionsFile
        # self.pool = TransactionPools(transactionsFile

    
    def run(self):
        # Initiate a simulation with n numNodes 


        # instantiate transaction pools
        # Make sure that unverified pool data struct can be read by all nodes
        # pools = TransactionPools()

        
        # create genesis block ie initial blockchain 
        # add genesis block to Verified Transaction Pool 
        
        # for node in range(self.numNodes):
        array = [10] * 10

        testND = testNode()

        print("hello world")

        if __name__ == "__main__": 
            for t in range()
            t1 = Thread(target=testND.run(array), name='t1')
            t2 = Thread(target=testND.run(array), name='t2')

            t1.start()
            t2.start()

        # Launch numNodes number of nodes. pass in pool reference
        # Make sure that pool reference can be modified by the nodes. 
        # Figure out how first node will get ledger. probably pass in genesis block to every node
        # Per the spec, we might need to be able to set the intent of a node: malicious vs cooperative


        # while True:
            # Call pool.newTransaction() at random times to add transactions to unverified pool
            # Print out state of blockchain by reading verified transaction pool which holds
            # verified blocks 
            # maybe communicate with nodes in order to print out current status of blockchain
            # and to print out when new blocks have been solved 


# pool = Transaction(transactionFile)

driver = Driver(10, "transaction file")

driver.run()
