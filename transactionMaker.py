import json
import hashlib
from ecdsa import SigningKey, VerifyingKey, NIST384p, BadSignatureError
import codecs

sk1 = SigningKey.generate()
vk1 = sk1.get_verifying_key()
pubkey = vk1.to_string().encode("hex")
vk =  VerifyingKey.from_string(pubkey.decode("hex"))
message = "hello"
sig = sk1.sign(message).encode("hex")
try:
      vk.verify(sig.decode("hex"), message)
      print "Good sig"
except BadSignatureError:
      print "Bad sig"


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
message = str(tinput1) + str(toutput1) + ttype1
print message
sig1 = [sk1.sign(message).encode("hex")] 

number1 = hashlib.sha256(str(tinput1) + str(toutput1) + str(sig1)).hexdigest()

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
sig2 = [sk1.sign(str(tinput2) + str(toutput2) + ttype2).encode("hex")] 

number2 = hashlib.sha256(str(tinput2) + str(toutput2) + str(sig2)).hexdigest()

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
sig3 = [sk2.sign(str(tinput3) + str(toutput3) + ttype3).encode("hex")] 

number3 = hashlib.sha256(str(tinput3) + str(toutput3) + str(sig3)).hexdigest()

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
sig4 = [sk3.sign(str(tinput4) + str(toutput4) + ttype4).encode("hex")] 

number4 = hashlib.sha256(str(tinput4) + str(toutput4) + str(sig4)).hexdigest()

data[4].append({
   'NUMBER': number4,
   'TYPE': ttype4,
   'INPUT': tinput4,
   'OUTPUT': toutput4,
   "SIGNATURE": sig4
})

with codecs.open('sampleInput.json','w', 'utf8') as outfile:
    json.dump(data,outfile,indent=2, ensure_ascii=False)


#5b5b752765323861313965626564313039373930663032383632393464656639393864323839636234316637623735343132626661383661326134656432363132356631272c20305d5d5b5b352c207527336361353239353562383635366366343631313563343061356666646237646438313838313638373966323935386330346634383636346463396239396139306335313863303535353930396562613136303038363466313964376535303662275d2c205b32302c207527333539373537396530653538396564653636613332356131383366366636393264373761663431323266643235333931333332316434646466323339303764656165663130376566303236346335633339343634383531386332363636646632275d5d5452414e53
#5b5b752764326132623865353034386662636639363630363865616265346135326230363232353961353861333539336335366364306537613662636261363335343736272c20305d5d5b5b352c207527353165626134326533633838316637316261616232303061343536323863343335666639623733353538623864643135643065326238376161616633383035386539633161633835306439623438386539646131333633643463616437643736275d2c205b32302c207527363164376262653631323062633563656435616233363433623035383837343533656266313239613537353935623664326439316239366361313039363463633739623631306466656631653039346162346638396338393161323637653631275d5d5452414e53