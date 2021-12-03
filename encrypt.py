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

f = open(input_folder,'r', encoding='utf-8')
g = open(output_folder, 'wb')
chunk = bytes(f.read(chunk_size), 'utf-8')
while chunk:
    result = xor_bytes(chunk,key)
    g.write(result)
    chunk = bytes(f.read(chunk_size), 'utf-8')
g.close()
f.close()