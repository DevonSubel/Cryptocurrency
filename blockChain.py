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
    def __init__(self, genesis): 
        # TODO: figure out if genesis should be passed in or created here
        # self.tinput = tinput
        self.blockCount = 0
        self.blockchain = Tree()
        self.genesis = genesis
        self.addGenesisBlock(genesis) #Add the genesis block to chain 

    def addGenesisBlock(self, genesis):
        self.blockchain.create_node("Block " + str(self.blockCount) + " ID: " + genesis.ID[:8], genesis.ID, data=genesis)
    
    def printBlockchain(self):
        self.blockchain.show()
    
    def addBlock(self, block):
        # TODO: run proof of work verification before adding block
        # Add block to chain & return true if POW valid 
        # Else return false
        self.blockCount += 1
        self.blockchain.create_node("Block " + str(self.blockCount) + " ID: " + block.ID[:8], block.ID, parent=block.prevID, data=block)

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
    


def blockchainTest():
    from transaction import *
    transaction = Transaction("merge", "tid", "input", "output", "signatures", "prevHash", )




