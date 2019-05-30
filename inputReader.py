import json
from transaction import *

def reader(filename):
   tansaction_list = []
   with open(filename) as json_file:
      data = json.load(json_file)
      for transaction in data:
         one_trans = data[transaction][0]
         transaction = Transaction(one_trans['TYPE'],one_trans['HASH'],one_trans['INPUT'],one_trans['OUTPUT'],one_trans['SIGNATURE'])
         transaction.printFields()
         tansaction_list.append(one_trans)
   return tansaction_list
 
data = {}
data[0] = []
data[0].append({
   'HASH': 12345678,
   'TYPE': 'TRANS',
   'INPUT': [(0,1)],
   'OUTPUT': [(10,'A'),(50,'B')],
   "SIGNATURE": 34626634
})
data[1] = []
data[1].append({
   'HASH': 12345278,
   'TYPE': 'TRANS',
   'INPUT': [(1,0)],
   'OUTPUT': [(2,'B'),(30,'A')],
   "SIGNATURE": 346234
})

with open('sampleInput.json','w') as outfile:
   json.dump(data,outfile)

reader("sampleInput.json")
