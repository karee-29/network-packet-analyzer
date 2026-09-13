from .parser import parse_packet
def read_pcap(path):
 from scapy.all import rdpcap
 return [r for p in rdpcap(path) if (r:=parse_packet(p))]
def live_capture(interface,count=50,filter_expr="ip"):
 from scapy.all import sniff
 out=[]
 def f(p):
  r=parse_packet(p)
  if r: out.append(r)
 sniff(iface=interface,filter=filter_expr,prn=f,count=count,store=False)
 return out
