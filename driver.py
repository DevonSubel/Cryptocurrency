import os
from threading import Thread
from inputReader import reader
from transaction import *
from transactionPool import *
from blockChain import *
from node import *

class Driver(object):
    
    def __init__(self, inputfile, numNodes):
        self.numNodes = numNodes
        self.inputfile = inputfile
        self.numNodes = numNodes

    def initializePools(self):
        # Load transactions from input file
        # Put genesis transaction into verified pool
        # Put the rest of the transactions into unverified pool
        trans_list = reader(self.inputfile)
        self.unverifiedPool = {}
        self.verifiedTransactionPool = {}

        for elem in trans_list:
            print("--------------------------------")
            if elem.tinput == ["NULL"]:
                self.verifiedTransactionPool[elem.tid] = elem
                continue
            self.unverifiedPool[elem.tid] = elem

        print(len(self.unverifiedPool))


    def run(self):
        # Initiate a simulation with n numNodes 

        self.initializePools()
        
        # for node in range(self.numNodes):
        if __name__ == "__main__":
            nd = node(self.verifiedTransactionPool, self.unverifiedPool)
            for t in range(self.numNodes):
                t1 = Thread(target=nd.mineBlock(), name='t1')
                t2 = Thread(target=nd.mineBlock(), name='t2')

                t1.start()
                t2.start()

        # Launch numNodes number of nodes. pass in pool reference
        # Make sure that pool reference can be modified by the nodes. 
        # Figure out how first node will get ledger. probably pass in genesis block to every node
        # Per the spec, we might need to be able to set the intent of a node: malicious vs cooperative
        # Per the spec, we might need to be able to set the speed of each node


        # while True:
            # Call pool.newTransaction() at random times to add transactions to unverified pool
            # Print out state of blockchain by reading verified transaction pool which holds
            # verified blocks 2661b5b6f0153409c6401b82dd55b33c1f67840a4cb6661123cd8494d4cc9b64c612158c1ba45c2199a0eaee193daf90
            # maybe communicate with nodes in order to print out current status of blockchain
            # and to print out when new blocks have been solved 


# pool = Transaction(transactionFile)

driver = Driver("sampleInput.json", 3)

driver.run()
