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

tinput0 = ['NULL']
toutput0 = [[25, vk1.to_string().encode('hex')]]
ttype0 = 'TRANS'
sig0 = ["NULL"]

number0 = hashlib.sha256(str(tinput0[0]) + str(toutput0) + str(sig0)).hexdigest()

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
message = str(tinput1[0]) + str(toutput1) + ttype1
print message
print message.encode("hex")
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
sig2 = [sk1.sign(str(tinput2[0]) + str(toutput2) + ttype2).encode("hex")] 

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
sig3 = [sk2.sign(str(tinput3[0]) + str(toutput3) + ttype3).encode("hex")] 

number3 = hashlib.sha256(str(tinput3) + str(toutput3) + str(sig3)).hexdigest()

data[3].append({
   'NUMBER': number3,
   'TYPE': ttype3,
   'INPUT': tinput3,
   'OUTPUT': toutput3,
   "SIGNATURE": sig3
})

# TRANSFER: VK3 MERGES TRANS 2 + 3, GIVES VK4 3, VK3 has 4 left

data[4] = []
tinput4 = [[number2, 0], [number3, 0]]
toutput4 = [[3, vk4.to_string().encode('hex')], [4, vk3.to_string().encode('hex')]]
ttype4 = 'MERGE'
sig4 = [sk3.sign(str(tinput4[0]) + str(toutput4) + ttype4).encode("hex"), sk3.sign(str(tinput4[1]) + str(toutput4) + ttype4).encode("hex")] 

number4 = hashlib.sha256(str(tinput4) + str(toutput4) + str(sig4)).hexdigest()

data[4].append({
   'NUMBER': number4,
   'TYPE': ttype4,
   'INPUT': tinput4,
   'OUTPUT': toutput4,
   "SIGNATURE": sig4
})

#TRANSFER: VK3 and VK2 JOINS (7) to give VK5 3, VK2 has 2 left, VK3 has 2 left

data[5] = []
tinput5 = [[number4, 1], [number3, 1]]
toutput5 = [[3, vk5.to_string().encode('hex')], [2, vk2.to_string().encode('hex')], [2, vk3.to_string().encode('hex')]]
ttype5 = 'JOIN'
sig5 = [sk3.sign(str(tinput5[0]) + str(toutput5) + ttype5).encode("hex"), sk2.sign(str(tinput5[1]) + str(toutput5) + ttype5).encode("hex")] 

number5 = hashlib.sha256(str(tinput5) + str(toutput5) + str(sig5)).hexdigest()

data[5].append({
   'NUMBER': number5,
   'TYPE': ttype5,
   'INPUT': tinput5,
   'OUTPUT': toutput5,
   "SIGNATURE": sig5
})

# TRANSFER: VK1 GIVES 3 -> VK2, HAS 12 LEFT

data[6] = []
tinput6 = [[number2, 1]]
toutput6 = [[3, vk2.to_string().encode('hex')], [12, vk1.to_string().encode('hex')]]
ttype6 = 'TRANS'
sig6 = [sk1.sign(str(tinput6[0]) + str(toutput6) + ttype6).encode("hex")] 

number6 = hashlib.sha256(str(tinput6) + str(toutput6) + str(sig6)).hexdigest()

data[6].append({
   'NUMBER': number6,
   'TYPE': ttype6,
   'INPUT': tinput6,
   'OUTPUT': toutput6,
   "SIGNATURE": sig6
})

# TRANSFER: VK1 GIVES 3 -> VK3, HAS 9 LEFT (May be double spend)

data[7] = []
tinput7 = [[number6, 1]]
toutput7 = [[3, vk2.to_string().encode('hex')], [9, vk1.to_string().encode('hex')]]
ttype7 = 'TRANS'
sig7 = [sk1.sign(str(tinput7[0]) + str(toutput7) + ttype7).encode("hex")] 

number7 = hashlib.sha256(str(tinput7) + str(toutput7) + str(sig7)).hexdigest()

data[7].append({
   'NUMBER': number7,
   'TYPE': ttype7,
   'INPUT': tinput7,
   'OUTPUT': toutput7,
   "SIGNATURE": sig7
})

# Double spend maybe Gives 3 to vk4, Has 9 left
data[8] = []
tinput8 = [[number6, 1]]
toutput8 = [[3, vk4.to_string().encode('hex')], [9, vk1.to_string().encode('hex')]]
ttype8 = 'TRANS'
sig8 = [sk1.sign(str(tinput8[0]) + str(toutput8) + ttype8).encode("hex")] 

number8 = hashlib.sha256(str(tinput8) + str(toutput8) + str(sig8)).hexdigest()

data[8].append({
   'NUMBER': number8,
   'TYPE': ttype8,
   'INPUT': tinput8,
   'OUTPUT': toutput8,
   "SIGNATURE": sig8
})

#TRANSFER: VK2 GIVES 1 -> VK5, HAS 2 LEFT

data[9] = []
tinput9 = [[number6, 0]]
toutput9 = [[1, vk5.to_string().encode('hex')], [2, vk2.to_string().encode('hex')]]
ttype9 = 'TRANS'
sig9 = [sk2.sign(str(tinput9[0]) + str(toutput9) + ttype9).encode("hex")] 

number9 = hashlib.sha256(str(tinput9) + str(toutput9) + str(sig9)).hexdigest()

data[9].append({
   'NUMBER': number9,
   'TYPE': ttype9,
   'INPUT': tinput9,
   'OUTPUT': toutput9,
   "SIGNATURE": sig9
})

with codecs.open('sampleInput.json','w', 'utf8') as outfile:
    json.dump(data,outfile,indent=2, ensure_ascii=False)

#5b5b2738323531613832343064616139646430386663333765353766316466333564653839346432623537316133316434653132653966343339343832656233663034272c20305d5d5b5b352c2027616136353535616532313463626638643739323233616135316432663034646235313332373832396138376635323430633338316633353164653462313861363732343864626331346162373336373938363362333131373663346136663131275d2c205b32302c2027633939353133653935306164306265393631373563316265346235336534396233616565326639323265653466663033623732333963376464623331393730373234653334303937353133623332316436663763616162383735336437306235275d5d5452414e53
#5b5b752765323861313965626564313039373930663032383632393464656639393864323839636234316637623735343132626661383661326134656432363132356631272c20305d5d5b5b352c207527336361353239353562383635366366343631313563343061356666646237646438313838313638373966323935386330346634383636346463396239396139306335313863303535353930396562613136303038363466313964376535303662275d2c205b32302c207527333539373537396530653538396564653636613332356131383366366636393264373761663431323266643235333931333332316434646466323339303764656165663130376566303236346335633339343634383531386332363636646632275d5d5452414e53
#5b5b752764326132623865353034386662636639363630363865616265346135326230363232353961353861333539336335366364306537613662636261363335343736272c20305d5d5b5b352c207527353165626134326533633838316637316261616232303061343536323863343335666639623733353538623864643135643065326238376161616633383035386539633161633835306439623438386539646131333633643463616437643736275d2c205b32302c207527363164376262653631323062633563656435616233363433623035383837343533656266313239613537353935623664326439316239366361313039363463633739623631306466656631653039346162346638396338393161323637653631275d5d5452414e53
