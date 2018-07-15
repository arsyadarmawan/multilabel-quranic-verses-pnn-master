from samba.dcerpc.atsvc import enum_ctr

n = int(raw_input().strip())
candles = map(int,raw_input().strip().split(' '))

a = [0,1,2,3,4,5,6,7,8,9]

for x in range(a):
    print x

for x in range(len(a)):
    print x

for x in enumerate(a):
    print x