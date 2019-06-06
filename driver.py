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

        genesisKey = ''

        for elem in trans_list:
            print("--------------------------------")
            if elem.tinput == ["NULL"]:
                self.verifiedTransactionPool[elem.tid] = elem
                genesisKey = elem.tid
                continue
            self.unverifiedPool[elem.tid] = elem

        print(len(self.unverifiedPool))
        return genesisKey


    def run(self):
        # Initiate a simulation with n numNodes 

        genesisKey = self.initializePools()
        genesisTrans = self.verifiedTransactionPool[genesisKey]
        print(genesisTrans)
        
        genesisBlock = Block(genesisTrans)
        genesisBlock.proofOfWork = hashlib.sha256(genesisBlock.blockToStr()).hexdigest()
        self.ledger = Blockchain(genesisBlock)

        # for node in range(self.numNodes):
        print("Driver launching nodes...")
        if __name__ == "__main__":
            
            for t in range(3):
                thread1 = Thread(target=Node(self.verifiedTransactionPool, self.unverifiedPool, self.ledger).mineBlock(), name=str(t))
                thread2 = Thread(target=Node(self.verifiedTransactionPool, self.unverifiedPool, self.ledger).mineBlock(), name=str(t))
                thread1.start()
                

driver = Driver("sampleInput.json", 3)

driver.run()
