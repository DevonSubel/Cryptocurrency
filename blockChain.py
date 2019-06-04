import Crypto 
import hashlib
import transaction


class block(object):
    # Block contains
        # single transaction
        # hash of previous block
        # proof of work
    
    def __init__(self, transaction):
        self.transaction = transaction
        self.prevBlockHash = ''
        self.proofOfWork = ''

    def blockToStr(self):
        transactionStr = self.transaction.toString()
        fieldsStr = self.prevBlockHash + self.proofOfWork
        blockStr = transactionStr + fieldsStr
        return(blockStr)

    def hashBlock(self):
        blockStr = self.blockToStr()
        blockHash = hashlib.sha256(blockStr).digest()
        return blockHash
        
        

class blockchain(object):

    # add blocks to some data structure. list is probably best 
    blockchainList = []

    def addToBlockchain(self, block):
        if len(block) != 0:
            prevblock = self.blockchainList[len(self.blockchainList) - 1]
            prevhash = prevblock.proofOfWork
            block.prevBlockHash = prevhash
        self.blockchainList.append(block)

    def getBlockchain(self):
        return self.blockchainList

    def getBlockchainLength(self):
        return len(self.blockchainList)




