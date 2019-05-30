

class Transaction(object):
    
    def __init__(self, ttype, tid, tinput, toutput, signature):
        self.type = ttype
        self.id = tid
        self.input = tinput
        self.output = toutput
        self.signature = signature


    def printFields(self):
        print(self.ttype)
        print(self.tid)
        print(self.tinput)
        print(self.toutput)

    def transfer(self):


output = {}
myinput = {}

tra = Transaction("transfer", "id", myinput , output, "signature")
tra.printFields()








        
    



