import json
import hashlib
from ecdsa import SigningKey, VerifyingKey, NIST384p, BadSignatureError

sk1 = SigningKey.generate(curve=NIST384p)
vk1 = sk1.get_verifying_key()

sk2 = SigningKey.generate()
vk2 = sk2.get_verifying_key()

sk3 = SigningKey.generate()
vk3 = sk3.get_verifying_key()

sk4 = SigningKey.generate()
vk4 = sk4.get_verifying_key()

sk5 = SigningKey.generate()
vk5 = sk5.get_verifying_key()


# GENESIS: 25 COINS TO VK1

data = {}
data[0] = []

tinput0 = 'NULL'
toutput0 = [[25, vk1.to_string().encode('hex')]]
ttype0 = 'TRANS'
sig0 = "NULL"

number0 = hashlib.sha256(tinput0 + str(toutput0) + sig0).hexdigest()

data[0].append({
   'NUMBER': number0,
   'TYPE': ttype0,
   'INPUT': tinput0,
   'OUTPUT': toutput0,
   "SIGNATURE": sig0
})

# TRANSFER: VK1 GIVES 5 -> VK2, VK1 HAS 20 LEFT

tinput1 = [[number0, 0]]
toutput1 = [[5, vk2.to_string().encode('hex')], [20, vk1.to_string().encode('hex')]]
ttype1 = 'TRANS'
sig1 = [sk1.sign(str(tinput1) + str(toutput1) + ttype1)] 

number1 = hashlib.sha256(str(tinput1) + str(toutput1) + sig1).hexdigest()

data[1] = []
data[1].append({
   'NUMBER': number1,
   'TYPE': ttype1,
   'INPUT': tinput1,
   'OUTPUT': toutput1,
   "SIGNATURE": sig1
})

# TRANSFER: VK1 GIVES 5 -> VK3, HAS 15 LEFT

data[2] = []
tinput2 = [[number1, 1]]
toutput2 = [[5, vk3.to_string().encode('hex')], [15, vk1.to_string().encode('hex')]]
ttype2 = 'TRANS'
sig2 = [sk1.sign(str(tinput2) + str(toutput2) + ttype2)] 

number2 = hashlib.sha256(str(tinput2) + str(toutput2) + sig2).hexdigest()

data[2].append({
   'NUMBER': number2,
   'TYPE': ttype2,
   'INPUT': tinput2,
   'OUTPUT': toutput2,
   "SIGNATURE": sig2
})

# TRANSFER: VK2 GIVES 2 -> VK3, HAS 3 LEFT

data[3] = []
tinput3 = [[number1, 0]]
toutput3 = [[2, vk3.to_string().encode('hex')], [3, vk2.to_string().encode('hex')]]
ttype3 = 'TRANS'
sig3 = [sk2.sign(str(tinput3) + str(toutput3) + ttype3)] 

number3 = hashlib.sha256(str(tinput3) + str(toutput3) + sig3).hexdigest()

data[3].append({
   'NUMBER': number3,
   'TYPE': ttype3,
   'INPUT': tinput3,
   'OUTPUT': toutput3,
   "SIGNATURE": sig3
})

# TRANSFER: VK3 MERGES TRANS 2 + 3, GIVES VK4 3

data[4] = []
tinput4 = [[number2, 0], [number3, 0]]
toutput4 = [[3, vk4.to_string().encode('hex')], [4, vk3.to_string().encode('hex')]]
ttype4 = 'TRANS'
sig4 = [sk3.sign(str(tinput4) + str(toutput4) + ttype4)] 

number4 = hashlib.sha256(str(tinput4) + str(toutput4) + sig4).hexdigest()

data[4].append({
   'NUMBER': number4,
   'TYPE': ttype4,
   'INPUT': tinput4,
   'OUTPUT': toutput4,
   "SIGNATURE": sig4
})

with open('sampleInput.json','w') as outfile:
    json.dump(data,outfile)