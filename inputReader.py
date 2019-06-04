import json
from transaction import *

def reader(filename):
   tansaction_list = []
   with open(filename) as json_file:
      data = json.load(json_file)
      print(data)
      for transaction in data:
         one_trans = data[transaction][0]
         transaction = Transaction(one_trans['TYPE'],one_trans['NUMBER'],one_trans['INPUT'],one_trans['OUTPUT'],one_trans['SIGNATURE'])
         transaction.printFields()
         tansaction_list.append(one_trans)
   return tansaction_list

reader("sampleInput.json")
