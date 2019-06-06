import json

data = {}
data[0] = []
data[0].append({
   'HASH': 1,
   'TYPE': 'TRANS',
   'INPUT': [(0,1)],
   'OUTPUT': [(10,'A'),(50,'B')],
   "SIGNATURE": 34626634
})
data[1] = []
data[1].append({
   'HASH': 2,
   'TYPE': 'TRANS',
   'INPUT': [(1,0)],
   'OUTPUT': [(2,'B'),(30,'A')],
   "SIGNATURE": 346234
})
data[2] = []
data[2].append({
   'HASH': 3,
   'TYPE': 'JOIN',
   'INPUT': [(1,1)],
   'OUTPUT': [(2,'B'),(30,'A')],
   "SIGNATURE": 316234
})
data[3] = []
data[3].append({
   'HASH': 4,
   'TYPE': 'JOIN',
   'INPUT': [(1,1)],
   'OUTPUT': [(2,'B'),(30,'A')],
   "SIGNATURE": 316234
})

with open('sampleInput.json','w') as outfile:
   json.dump(data,outfile)

