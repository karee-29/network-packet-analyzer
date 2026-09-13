import argparse
from .capture import read_pcap,live_capture
from .analytics import protocol_summary,conversations,traffic,flags
from .export import write_csv,write_json
def main():
 p=argparse.ArgumentParser(description="Advanced Wireshark-inspired packet analyzer")
 g=p.add_mutually_exclusive_group(required=True);g.add_argument("--pcap");g.add_argument("--live")
 p.add_argument("--count",type=int,default=50);p.add_argument("--filter",default="ip");p.add_argument("--limit",type=int,default=100);p.add_argument("--csv");p.add_argument("--json")
 a=p.parse_args();rs=read_pcap(a.pcap) if a.pcap else live_capture(a.live,a.count,a.filter)
 print("Source IP | Destination IP | Protocol | Port | Packet Size | Info")
 for r in rs[:a.limit]:print(f"{r.source_ip} | {r.destination_ip} | {r.protocol} | {r.source_port or '-'}->{r.destination_port or '-'} | {r.packet_size} | {r.info}")
 print("\nPROTOCOLS",protocol_summary(rs));print("\nTRAFFIC",traffic(rs));print("\nCONVERSATIONS",conversations(rs)[:10])
 print("\nHEURISTIC FLAGS",[(r.source_ip,r.destination_ip,x) for r,x in flags(rs)[:20]])
 if a.csv:write_csv(rs,a.csv)
 if a.json:write_json(rs,a.json)
if __name__=="__main__":main()
