from inputReader import *
import random

class TransactionPools(object):

    # Holds unverified and verified trasaction pools 
    # Once a transaction has been verified, move it to the verified pool

    # allTransactionsList = () //list of all transactions
    allTransactionsList = reader("sampleInput.json")
    # unverifiedPool = () //list for holding verified transactions
    unverifiedPool = []
    # verifiedPool = ()   //list for holding verified transactions
    verifiedPool = []

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
    # & move it to the verified pool
        TransactionPools.verifiedPool.append(transaction)
        TransactionPools.unverifiedPool.remove(transaction)

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