f=open("flag.txt", "r")
flag = f.read()

g = open("key.txt" , "r")
key = g.read()

key = key[0:4]

def enc(text,key):
    encrypted = []
    for i in range(int(round(len(text)/4))):
        shifted = spicy(text[i*4:(i+1)*4],i,key)
        encrypted.append(shifted)
    return encrypted



def spicy(text,offset,key):
    res = []
    for p in range(len(text)):
        res.append(int((ord(text[p])+offset)^ord(key[p])))
    return res

flat_list = []
for sublist in enc(flag,key):
    for item in sublist:
        flat_list.append(item)

f=open("enc.txt","w+")
f.write(str(flat_list))

