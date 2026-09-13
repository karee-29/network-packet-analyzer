from scapy.all import IP,TCP,UDP,ICMP,DNS,DNSQR,Raw
from packet_analyzer.parser import parse_packet
def test_tcp(): assert parse_packet(IP(src="1.1.1.1",dst="2.2.2.2")/TCP(sport=1,dport=443,flags="S")).protocol=="TCP"
def test_http():
 r=parse_packet(IP(src="1.1.1.1",dst="2.2.2.2")/TCP(sport=1,dport=80)/Raw(load=b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"))
 assert r.protocol=="HTTP" and r.http_host=="example.com"
def test_dns(): assert parse_packet(IP()/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="example.com"))).protocol=="DNS"
def test_icmp(): assert parse_packet(IP()/ICMP(type=8)).protocol=="ICMP"
