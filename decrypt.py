import sys

def xor_bytes(chunk,key):
    result = bytearray()
    for i in range(len(chunk)):
        result.append(chunk[i]^key[i])
    return result

key = sys.argv[1]
input_folder = sys.argv[2]
output_folder = sys.argv[3]

key = bytes(key, 'utf-8')
chunk_size = len(key)

f = open(input_folder,'rb')
g = open(output_folder, 'w', encoding='utf-8')
chunk = f.read(chunk_size)
while chunk:
    result = xor_bytes(chunk,key)
    g.write(result.decode('utf-8'))
    chunk = f.read(chunk_size)
g.close()
f.close()