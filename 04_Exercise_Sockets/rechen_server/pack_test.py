from struct import pack, unpack

input = '<1><add><2><1><2>'

#parse input string
cutted = input[1:-1]
splitted_input = cutted.split('><')
id = int(splitted_input[0])
operation = splitted_input[1]
count = int(splitted_input[2])
num_arr = list(map(int, splitted_input[3:]))


print(id)
print(operation)
print(count)
print(num_arr)


#pack input in format: <ID><Rechenoperation><N><z1><z2>...<zN>
print('i' + str(len(operation)) + 'si' + str(count) + 'i')
packed = pack('i' + str(len(operation)) + 'si' + str(count) + 'i', id, operation.encode(), count, *num_arr)
print(packed)
#unpack input with mutable format
unpacked = unpack('i' + str(len(operation)) + 'si' + str(count) + 'i', packed)
print(unpacked)
