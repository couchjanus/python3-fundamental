from struct import *

out = open("123.bin", "wb")    
format = "if5s"                

data = pack(format, 24, 12.48, b"12345")
out.write(data)
out.close()

input = open("123.bin", "rb")
data = input.read()
input.close()

format = "if5s"     # one integer

value,value2,value3 = unpack(format, data) # note the ',' in 'value,': 

# unpack apparently returns a n-uple
print(value)
print(value2)
print(value3)
print(calcsize(format))
