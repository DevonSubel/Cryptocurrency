import Crypto 
import hashlib
from transaction import *
from graphviz import Digraph, Source
from treelib import Node, Tree

class Block(object):
    # Block contains
        # single transaction
        # hash of previous block
        # proof of work
    
    def __init__(self, transaction):
        self.transaction = transaction
        self.prevBlockHash = ''
        self.proofOfWork = '' #Hash of 
        self.nonce = '' #Nonce that solved the puzzle

    def blockToStr(self):
        transactionStr = self.transaction.toString()
        fieldsStr = self.prevBlockHash + self.proofOfWork
        blockStr = transactionStr + fieldsStr
        return(blockStr)

    def hashBlock(self):
        blockStr = self.blockToStr()
        blockHash = hashlib.sha256(blockStr).digest()
        return blockHash
        
        

class Blockchain(object):
    def __init__(self, genesis): 
        # TODO: figure out if genesis should be passed in or created here
        # self.tinput = tinput
        self.blockCount = 0
        self.blockchain = Tree()
        self.genesis = genesis
        self.addGenesisBlock(genesis) #Add the genesis block to chain 

    def addGenesisBlock(self, genesis):
        self.blockchain.create_node("Block " + str(self.blockCount) + " ID: " + genesis.proofOfWork[:8], genesis.proofOfWork, data=genesis)
    
    def printBlockchain(self):
        self.blockchain.show()
    
    def addBlock(self, block):
        # TODO: run proof of work verification before adding block
        # Add block to chain & return true if POW valid 
        # Else return false
        self.blockCount += 1
        self.blockchain.create_node("Block " + str(self.blockCount) + " ID: " + block.proofOfWork[:8], block.proofOfWork, parent=block.prevBlockHash, data=block)

    def getGenesisID(self):
        return self.blockchain.root

    def getLongestChainBlocks(self):
        allNodes = self.blockchain.all_nodes()
        forkNum = 0 #number of leaves at longest branch
        treeDepth = self.blockchain.depth()
        longestPathLeaves = [] #WIll hold leaves with treeDepth depth ie longest branch(es)
        for node in allNodes:
            currentDepth = self.blockchain.depth(node)
            if(currentDepth == treeDepth):
                forkNum += 1
                longestPathLeaves.append(node)        

        return forkNum, longestPathLeaves
      
            
    def blockchainLength(self):
        # returns the depth of the tree ie the length of 
        #  the longest chain
        return self.blockchain.depth()

    def numBlocks(self):
        return self.blockchain.size()

    def printChain(self, chain):
        chain.show(data_property="humanID")

    def tailBlocks(self, chain):
        leaves = chain.leaves()
        print("Num leaves" + str(len(leaves)))
        print(leaves)

    def checkBlock(self):
        # Check the proof work work
        # return true if proof of work is valid
        # else rerturn false 
        print("printing block")

    def createBlockchainGraph(self, outfilename):
        print("creating graph")
        self.blockchain.to_graphviz(filename= outfilename + '.gv', shape=u'box', graph=u'digraph')
        g = Source.from_file(outfilename + '.gv')
        g.render()

    def createBlockchainImg(self, outfilename):
        print("creating graph")
        self.blockchain.to_graphviz(filename= outfilename + '.gv', shape=u'box', graph=u'digraph')
        g = Source.from_file(outfilename + '.png')
        g.render()
    


def blockchainTest():
    transaction = Transaction("Gen", "1", ['NULL'], [[40, 'abc']], ['NULL'])

    gen = Block(transaction)
    gen.prevBlockHash = "11"
    gen.proofOfWork = "GenProof"

    blockchain = Blockchain(gen)
    blockchain.printBlockchain()

    transaction = Transaction("Transfer", "2", [[1, 0]], [[20, 'fgh'], [20, 'abc']], ['sig1'])
    block = Block(transaction)
    block.prevBlockHash = "GenProof"
    block.proofOfWork = "1Proof"
    blockchain.addBlock(block)

    transaction = Transaction("Transfer", "3", [[2, 0]], [[5, 'xyz'], [15, 'fgh']], ['sig2'])
    block2 = Block(transaction)
    block2.prevBlockHash = "GenProof"
    block2.proofOfWork = "2Proof"
    blockchain.addBlock(block2)

    blockchain.printBlockchain()
    #blockchain.createBlockchainImg('blockchainImg')

    # JSON Test
    return blockchain.blockchain.to_json()



json = blockchainTest()
print(json)

