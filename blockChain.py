import Crypto 
import hashlib


class block(object):
    # Block contains:
    # single transaction 
    
    def __init__(self, transaction):
        self.transaction = transaction



class blockChain(object):

    # add blocks to some data structure. list is probably best 
    