import random
import hashlib

def main():
    val = hashlib.sha256(str(random.random())).hexdigest()
    print(val)
    while(val[0:5] != '00000'):
        val = hashlib.sha256(str(random.random())).hexdigest()
        print(val)
main()