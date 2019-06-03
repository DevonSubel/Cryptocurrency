from inputReader import *
import random

class TransactionPools(object):
    # Class to keep lists of all transactions input file,
    # unverified and verified trasaction pools 
    # as well as methods for moving transactions from one pool to the other

    # TODO: verified transactions need to be transcation objects. 
    # It might be best to keep all transactions in all pools as transaction objects too
    # If so, convert allTransactionsList to instantiate transation objects for each trans in file

    def __init__(self, inputFile):

        self.inputFile = inputFile
        self.allTransactionsList = reader(self.inputFile)  
        self.unverifiedPool = []
        self.verifiedPool = []
        self.newBlockMined = False; #Flag set when new transaction has been verified. 

    def addTransaction(self):
        # when called, read transaction from file and add it to unverified pool 
        # For each transaction, instantiate transaction object and add it to the pool
        randIndex = random.randint(0,len(TransactionPools.allTransactionsList)-1)
        print(randIndex)
        TransactionPools.unverifiedPool.append(TransactionPools.allTransactionsList[randIndex])
        del TransactionPools.allTransactionsList[randIndex]

    def getTransaction(self):
        # return transaction from unverified pool
        randIndex = random.randint(0, len(TransactionPools.unverifiedPool)-1)
        newTransaction = TransactionPools.unverifiedPool[randIndex]
        return newTransaction

    def markTransactionAsInvalid(self,transaction):
        # Per the spec, nodes should have the ability to mark a transaction as invalid in the pool 
        # so that it gets thrown out
        TransactionPools.unverifiedPool.remove(transaction)

    def verifyTransaction(self,transaction):
        # Once a transaction has been verified, move it to the verified pool
        self.newBlockMined = True; 
        TransactionPools.verifiedPool.append(transaction)
        TransactionPools.unverifiedPool.remove(transaction)

    def newBlockMined(self):
        # Used by nodes to check if new block has been mined by the network
        # and should stop trying to mine new block & should update their blockchain & start mining new block
        return self.newBlockMined; 

    def returnTransactionToUnverifiedPool(self, transaction):
        # TODO:
        # Per the spect, if the transaction is invalid because the input doesn’t yet exist, return it to the UTP
        
    
# Tests:
# TODO: change input. class now takes as argument the input file name 
'''
pool = TransactionPools()

print("_____START_________")
print(TransactionPools.allTransactionsList,len(TransactionPools.allTransactionsList))
print(TransactionPools.unverifiedPool,len(TransactionPools.unverifiedPool))
print(TransactionPools.verifiedPool,len(TransactionPools.verifiedPool))

TransactionPools.addTransaction((pool))

print("______addTrans()________________")
print(TransactionPools.allTransactionsList,len(TransactionPools.allTransactionsList))
print(TransactionPools.unverifiedPool,len(TransactionPools.unverifiedPool))
print(TransactionPools.verifiedPool,len(TransactionPools.verifiedPool))

test = TransactionPools.getTransaction(pool)

print("_____getTrans()_________________")
print(TransactionPools.allTransactionsList,len(TransactionPools.allTransactionsList))
print(TransactionPools.unverifiedPool,len(TransactionPools.unverifiedPool))
print(TransactionPools.verifiedPool,len(TransactionPools.verifiedPool))

TransactionPools.markTransactionAsInvalid(pool,test)

print("______markTrans()_______________")
print(TransactionPools.allTransactionsList,len(TransactionPools.allTransactionsList))
print(TransactionPools.unverifiedPool,len(TransactionPools.unverifiedPool))
print(TransactionPools.verifiedPool,len(TransactionPools.verifiedPool))

TransactionPools.addTransaction((pool))

print("_______addTrans()______________")
print(TransactionPools.allTransactionsList,len(TransactionPools.allTransactionsList))
print(TransactionPools.unverifiedPool,len(TransactionPools.unverifiedPool))
print(TransactionPools.verifiedPool,len(TransactionPools.verifiedPool))

test = TransactionPools.getTransaction(pool)

print("_______getTrans()________________")
print(TransactionPools.allTransactionsList,len(TransactionPools.allTransactionsList))
print(TransactionPools.unverifiedPool,len(TransactionPools.unverifiedPool))
print(TransactionPools.verifiedPool,len(TransactionPools.verifiedPool))

TransactionPools.verifyTransaction(pool,test)

print("_______verify()________________")
print(TransactionPools.allTransactionsList,len(TransactionPools.allTransactionsList))
print(TransactionPools.unverifiedPool,len(TransactionPools.unverifiedPool))
print(TransactionPools.verifiedPool,len(TransactionPools.verifiedPool))
'''
