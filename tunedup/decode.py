# DTMF tone table
maps = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
# manually recorded tones, 1 being lowest frequency and 7 being highest
code = "35 47 37 47 27 27 47 17 17 47 17 47 17 47 36 47 27 47 17 17 17 47 36 47 27 27 27 47 27 27 47 17 17 47 35 35 " \
       "35 35 47 16 47 35 35 35 47 17 17 47 16 16 16 47 27 27 27 47 27 27 27 47 26 26 26"

# transform code to dtmf tones
def trans(x):
    return maps[int(x[0]) - 1][int(x[1]) - 5]

code = code.split(' ')

result = map(lambda x: trans(x), code)
print(''.join(result))
