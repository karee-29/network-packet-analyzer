from collections import Counter,defaultdict
def protocol_summary(rs):
 c=Counter(r.protocol for r in rs); n=max(1,len(rs))
 return [{"protocol":p,"packets":v,"share_pct":round(v*100/n,2)} for p,v in c.most_common()]
def conversations(rs):
 c=defaultdict(lambda:[0,0])
 for r in rs:
  k=tuple(sorted([(r.source_ip,r.source_port),(r.destination_ip,r.destination_port)],key=str)); c[k][0]+=1;c[k][1]+=r.packet_size
 return [{"endpoint_a":f"{k[0][0]}:{k[0][1] or '-'}","endpoint_b":f"{k[1][0]}:{k[1][1] or '-'}","packets":v[0],"bytes":v[1]} for k,v in sorted(c.items(),key=lambda x:-x[1][1])]
def traffic(rs):
 c=defaultdict(lambda:[0,0])
 for r in rs: c[r.protocol][0]+=1;c[r.protocol][1]+=r.packet_size
 return [{"protocol":k,"packets":v[0],"bytes":v[1]} for k,v in sorted(c.items(),key=lambda x:-x[1][1])]
def flags(rs):
 out=[]
 for r in rs:
  x=[]
  if r.packet_size>1400:x.append("large-packet")
  if r.protocol=="TCP" and r.tcp_flags and "S" in r.tcp_flags and "A" not in r.tcp_flags:x.append("SYN")
  if r.protocol=="ICMP" and r.icmp_type==8:x.append("echo-request")
  if r.destination_port in {23,445,3389,5900}:x.append("sensitive-port")
  if x:out.append((r,x))
 return out
