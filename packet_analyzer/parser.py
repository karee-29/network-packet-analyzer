try:
 from scapy.all import IP,TCP,UDP,ICMP,DNS,Raw
except ImportError: IP=TCP=UDP=ICMP=DNS=Raw=None
from .models import PacketRecord
def parse_packet(pkt):
 if IP is None: raise RuntimeError("Install dependencies with pip install -r requirements.txt")
 if not pkt.haslayer(IP): return None
 ip=pkt[IP]; proto="IP"; sp=dp=None; flags=None; q=qt=hm=hh=hp=it=ic=None; info=""
 payload=bytes(pkt[Raw].load) if Raw and pkt.haslayer(Raw) else b""
 if pkt.haslayer(TCP):
  sp,dp=int(pkt[TCP].sport),int(pkt[TCP].dport); flags=str(pkt[TCP].flags); proto="TCP"; info=f"TCP flags={flags}"
  try:
   t=payload.decode(errors="replace"); first=t.split("\r\n")[0]; parts=first.split()
   if len(parts)>=2 and parts[0] in {"GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"}:
    proto="HTTP"; hm,hp=parts[0],parts[1]
    for line in t.split("\r\n")[1:]:
     if line.lower().startswith("host:"): hh=line.split(":",1)[1].strip()
    info=f"{hm} {hp}"+(f" Host={hh}" if hh else "")
  except Exception: pass
 elif pkt.haslayer(UDP):
  sp,dp=int(pkt[UDP].sport),int(pkt[UDP].dport); proto="UDP"; info=f"UDP {sp}->{dp}"
  if pkt.haslayer(DNS):
   proto="DNS"; d=pkt[DNS]
   if d.qd and hasattr(d.qd,"qname"):
    q=d.qd.qname.decode(errors="replace").rstrip("."); qt=str(getattr(d.qd,"qtype","")); info=f"Query {q} type={qt}"
 elif pkt.haslayer(ICMP):
  proto="ICMP"; it,ic=int(pkt[ICMP].type),int(pkt[ICMP].code); info=f"ICMP type={it} code={ic}"
 return PacketRecord(float(getattr(pkt,"time",0)),ip.src,ip.dst,proto,sp,dp,len(pkt),int(ip.ttl),flags,q,qt,hm,hh,hp,it,ic,info)
