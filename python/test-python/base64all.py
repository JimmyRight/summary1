#encoding:utf8

import base64

s0='R1pDVE1NWlhHUTNETU4yQ0dZWkRNTUpYR00zREtNWldHTTJES1JSV0dJM0RDTlpUR1kyVEdNWlRHSTJVTU5SUkdaQ1RNTkJWSVkzREVOUlJHNFpUTU5KVEdFWlRNTjJF'
print s0+'\r\n'
s1=base64.b64decode(s0)
print s1+'\r\n'
s2=base64.b32decode(s1)
print s2+'\r\n'
#s3=binascii.a2b_hex(s2).decode("utf8")
s3=base64.b16decode(s2)
print s3
