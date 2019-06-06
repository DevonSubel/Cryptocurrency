import random
import hashlib

def main():
    val = int(hashlib.sha256(str(random.random())).hexdigest(),16)
    print('0x'+str(val))
               #0x2418d2d833b46fd88958b61f06f1a13c38dceb8c02390d3ffd89d26ae7d12a69
    while(val > 0x0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF):
        print(str(hex(val))) #00c5b08c62d17cd85ec51299aa37d99f5bd8dd24b7541a5b6a433b50db4999db
        val = int(hashlib.sha256(str(random.random())).hexdigest(),16)
main()