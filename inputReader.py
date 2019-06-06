import json
from transaction import *
from collections import OrderedDict

def reader(filename):
   tansaction_list = []
   with open(filename) as json_file:
      data = json.load(json_file, object_pairs_hook = OrderedDict)
      for field in data:
         one_trans = data[field][0]
         trans = Transaction(one_trans['TYPE'],one_trans['NUMBER'],one_trans['INPUT'],one_trans['OUTPUT'],one_trans['SIGNATURE'])
         tansaction_list.append(trans)
   return tansaction_list

#print(reader("sampleInput.json"))

