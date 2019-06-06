class node(object):

    import hashlib
    import random
    from ecdsa import SigningKey, VerifyingKey, BadSignatureError
    import blockChain

    def __init__(self, verifiedTransactionPool, unverifiedTransactionPool):
        self.verifiedTransactionPool = verifiedTransactionPool
        self.unverifiedTransactionPool = unverifiedTransactionPool

    def __init__(self, transactionPool):
        self.pool = transactionPool


    def getLedgerFromNetwork(self):
        print("getting current ledger from network")
        # Each node will have to get a copy of the ledger
        # Figure out how to get current ledger for new node entering network
        # detect any forks in the ledger. atuomatically switch to longest chain 
        # detect any forks 
        return 0

    def validTransaction(self, transaction):
        # Make sure that a transaction has not been double-spent ie been used as the input to other transactions more than once. 
        # run through ledger to verify that transaction is valid and input has not been already spent

        # return true if transaction is valid

        totalInput = 0
        totalOutput = 0
        tinput = transaction.tinput
        toutput = transaction.toutput
        ttype = transaction.ttype
        signatures = transaction.signatures

        print("###")
        print(len(signatures))
        print(len(tinput))
        print("###")
        transaction.printFields()
        if len(signatures) != len(tinput):
            return False
        
        for i in range(len(signatures)):
            sig = signatures[i]
            key = tinput[i][0]
            outpIndex = tinput[i][1]
            if not key in self.verifiedTransactionPool:
                print("No reference")
                return "No reference"
            pointedTrans = self.verifiedTransactionPool[key]
            pointedOutput = pointedTrans.toutput
            pubkey = pointedOutput[outpIndex][1]
            inp = pointedOutput[outpIndex][0]
            if inp < 0.1:
                return 1
            totalInput += inp
            vk =  self.VerifyingKey.from_string(pubkey.decode("hex"))
            print("Index" + str(i))
            print(len(pointedTrans.tinput))
            print(pointedTrans.tinput)
            message = str(tinput[i]) + str(toutput) + str(pointedTrans.ttype)
            print(message)
            print(message.encode("hex"))
            try:
                vk.verify(sig.decode("hex"), message)
                print("Good sig")
            except self.BadSignatureError:
                print("Bad sig")

        # for outp in toutput:
        #     totalOutput += outp[0]

        # if totalInput != totalOutput: # Check that output and input are the same
        #     return False
                    
        return True # If this point has been reached the transaction is verified       
        
        # # Verify 
        # for tTinput in tinput: # For each Input do:
        #     if tTinput[1] < 0.1: # Check that it's not less than min amount
        #         return False

        #     vOutput = self.verifiedTransactionPool[tTinput[0]].toutput[0] # Get The Output pointed to
        #     if vOutput == tTinput[1]: # Check that value is equal
        #         totalInput += vOutput # Add the amount to the cumulative input in case input is from different places
        #         self.verifiedTransactionPool[tTinput[0]].toutput[0] = -1 # Change Output so no future transaction can point to it
        #     else:
        #         return False # If they are not equal return false
        
        # for output in toutput: # Accumulate all output
        #     totalOutput += output[0]

        # if totalInput != totalOutput: # Check that output and input are the same
        #     return False
                    
        # return True # If this point has been reached the transaction is verified

    def getTransactionFromPool(self):
        index = self.random.choice(list(self.unverifiedTransactionPool))
        transaction = self.unverifiedTransactionPool[index]
        
        return transaction
    
    def verifyMinedBlock(self, block):
        print("verifiying node")
        # check that new block mined by network has valid transactions and 
        # that the proof is work is correct ie it has the right hash
        # To do that, hash the transaction (with some fields blanked out) to check that
        # the hash matches 
    
    def solvedPuzzle(self, block, nonce):
        # Run proof of work
        # hash the block with randomVal until the hash has n number of zeroes
        # if the puzzle is solved, return the block + iterator value and the hash. this is the new block
        hval = self.hashlib.sha256(block.blockToStr() + str(nonce))
        if(hval < 0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF):
            return block, nonce, hval 
        else:
            return "", "", ""

    def createBaseBlock(self, transaction):
        # creates base block from transaction to run it through the puzzle 
        return self.blockChain.block(transaction)


    # # infinite loop that calls mineBlock 


    def mineBlock(self):
        print("Sup")
        while len(self.unverifiedTransactionPool) > 0:
            print (len(self.unverifiedTransactionPool))
            verlen = len(self.verifiedTransactionPool)
            transaction = self.getTransactionFromPool()

            if self.validTransaction(transaction) == "No reference":
                continue

            # Begin mining block
            block = self.createBaseBlock(transaction)
            while True:
                newlen = len(self.verifiedTransactionPool)
                if(newlen > verlen):
                    break 
                randint = self.random.random()
                block, nonce, hval = self.solvedPuzzle(block, randint)
                if(block, nonce, hval != "", "", ""):
                    del self.unverifiedTransactionPool[transaction.tid]
                    self.verifiedTransactionPool[transaction.tid] = transaction
                    break
                
    def run(self):
        print("running node")
